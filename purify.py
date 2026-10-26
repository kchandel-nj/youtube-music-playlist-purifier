import os
import json
import ytmusicapi
from dotenv import load_dotenv
from ytmusicapi import YTMusic

# Load environment configuration variables from the local .env file
load_dotenv()

def main():
    # Fetch the multi-line raw header string securely from your environment variables
    headers_raw = os.getenv("YT_MUSIC_HEADERS")
    
    if not headers_raw:
        print("CRITICAL ERROR: 'YT_MUSIC_HEADERS' environment variable not found in your .env file.")
        print("Please check your .env file formatting and ensure the raw block is wrapped in double quotes.")
        return

    print("Generating official browser.json config layout...")
    try:
        # Utilizing the package-level setup method directly with headers_raw parameter
        ytmusicapi.setup(filepath="browser.json", headers_raw=headers_raw.strip())
        print("Configuration file parsed and written natively from environment variable!")
    except Exception as e:
        print(f"Native setup helper failed: {e}")
        return

    print("\nConnecting to YouTube Music using structured file...")
    try:
        # Load via file string directly so initialization state sets authenticated flag
        yt = YTMusic("browser.json")
    except Exception as e:
        print(f"Authentication structural load failed: {e}")
        return

    print("\nFetching your playlists...")
    try:
        playlists = yt.get_library_playlists()
    except Exception as e:
        print(f"Connection failed: {e}")
        return
    
    if not playlists:
        print("No playlists found in your library.")
        return

    for index, pl in enumerate(playlists):
        print(f"[{index}] {pl['title']} ({pl.get('count', '0')} items)")

    try:
        choice = int(input("\nEnter the number of the playlist you want to purify: "))
        selected_playlist = playlists[choice]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        return

    playlist_id = selected_playlist['playlistId']
    print(f"\nAnalyzing '{selected_playlist['title']}'...")
    
    playlist_details = yt.get_playlist(playlist_id, limit=None)
    tracks = playlist_details.get('tracks', [])
    
    if not tracks:
        print("This playlist has no tracks.")
        return

    seen_video_ids = set()
    duplicates_to_remove = []
    dead_tracks_to_remove = []

    print("\nScanning tracks...")
    for track in tracks:
        video_id = track.get('videoId')
        title = track.get('title', 'Unknown Title')
        
        # Capture tracks that are unplayable or completely missing IDs (deleted videos)
        if not video_id or track.get('isAvailable') is False:
            dead_tracks_to_remove.append(track)
            print(f"❌ Dead/Unavailable Track detected: {title}")
            continue

        if video_id in seen_video_ids:
            duplicates_to_remove.append(track)
            print(f"👯 Duplicate detected: {title}")
        else:
            seen_video_ids.add(video_id)

    print("\n--- Scan Results ---")
    print(f"Total tracks analyzed: {len(tracks)}")
    print(f"Duplicates found: {len(duplicates_to_remove)}")
    print(f"Dead tracks found: {len(dead_tracks_to_remove)}")

    # Handle duplicate removals
    if duplicates_to_remove:
        confirm = input(f"\nWould you like to auto-delete the {len(duplicates_to_remove)} duplicate(s)? (y/n): ")
        if confirm.lower() == 'y':
            print("Purifying duplicates...")
            yt.remove_playlist_items(playlist_id, duplicates_to_remove)
            print("✨ Purification complete! Duplicates removed successfully.")
        else:
            print("Operation canceled. No changes made to duplicates.")
    else:
        print("\nYour playlist is clean of duplicate items!")

    # Handle dead track removals
    if dead_tracks_to_remove:
        confirm = input(f"\nWould you like to auto-delete the {len(dead_tracks_to_remove)} dead track(s)? (y/n): ")
        if confirm.lower() == 'y':
            print("Deleting dead tracks...")
            yt.remove_playlist_items(playlist_id, dead_tracks_to_remove)
            print("✨ Purification complete! Dead tracks removed successfully.")
        else:
            print("Operation canceled. No changes made to dead tracks.")

if __name__ == "__main__":
    main()
