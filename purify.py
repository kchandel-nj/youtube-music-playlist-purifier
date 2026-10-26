import ytmusicapi
from ytmusicapi import YTMusic

# The exact raw block from your web browser inspect window
headers_raw = """
accept
*/*
accept-encoding
gzip, deflate, br, zstd
accept-language
en-US,en;q=0.9
authorization
SAPISIDHASH 1793047936_f1e6c34de08f39a572789e26363d07f8c4c4f90e_u SAPISID1PHASH 1793047936_f1e6c34de08f39a572789e26363d07f8c4c4f90e_u SAPISID3PHASH 1793047936_f1e6c34de08f39a572789e26363d07f8c4c4f90e_u
content-encoding
gzip
content-length
2621
content-type
application/json
cookie
LOGIN_INFO=AFmmF2swRQIhAJNUiuNerBtmsiZ9BT_yztvCNYUSB8VdwrETeMLC5dKAAiANEPb-N_X7cq8gqo5K2NUibnlfEQA5ow2u1AFWj122Ow:QUQ3MjNmeUpHMVExNzlxdnFvNzRDYmI4ZGdDNURoNzBSVWdLY25POWZjUlBJV0xCRFdLb0c1ZHhkYklzaFBYRUpuRXdaMF9iWGg2a0dOUzJSbld2SUthRVdaby1wclVrMVhQYzNuZVhwdnZFZnFVYlNpY2VDbHNwZFllMDdFdjNHRWpHUHpBOVRFVTJMWXRPQktMTjNfNktWM2Utc2xGcFNR; VISITOR_INFO1_LIVE=LP2qRCh3Gkw; VISITOR_PRIVACY_METADATA=CgJVUxIEGgAgSg%3D%3D; __Secure-BUCKET=CM4G; HSID=AciFHd1Bo3WHqnBf6; SSID=As0Xt2fR3Fekyqblc; APISID=qoqMRkCFCxLR1Z2k/AvhqHYAbyD2hzv6yG; SAPISID=Lvq-0sY5lGJAytVE/An9utGOBoUbshqb6B; __Secure-1PAPISID=Lvq-0sY5lGJAytVE/An9utGOBoUbshqb6B; __Secure-3PAPISID=Lvq-0sY5lGJAytVE/An9utGOBoUbshqb6B; SID=g.a000DwmJYKBUQ7qeFmsyzSNU1va6v1BmtJkrW7tchWYQUR89dlR2j6dREaoOP-lGeEOFj0674gACgYKAQgSARMSFQHGX2MifJ8kuhK_7Toe631YcGOhZhoVAUF8yKpYe8B9hOJyWKEMosEOmxoj0076; __Secure-1PSID=g.a000DwmJYKBUQ7qeFmsyzSNU1va6v1BmtJkrW7tchWYQUR89dlR2KMrXAHV4T-g0DwSzyejryAACgYKAVoSARMSFQHGX2MiVnPKy6oTSkSWxvNDlR8kUxoVAUF8yKp0Lrm-ZMIQRQC1mKkA3RNX0076; __Secure-3PSID=g.a000DwmJYKBUQ7qeFmsyzSNU1va6v1BmtJkrW7tchWYQUR89dlR2pbI1H6yvf7bcOp7Um2QoagACgYKAZISARMSFQHGX2MiOfFbVECz64QqIMmAeFVGoBoVAUF8yKo-V78FxejEffaPDHitsCFy0076; YSC=_bsfQZPM62Y; PREF=f6=40000080&tz=America.New_York&f7=100&repeat=NONE&autoplay=true&volume=45; __Secure-YNID=CvABCAUSogEB8QZuZiNu_uqMHYzYAc_OGye459U22w0H9j6DQ8w7DQ9LpA-Bfi4NNWGfY6e5zLX-lCoIysAEHOfof-mmz8LTINUavF2mZG6_cespci-MsW22MeZ6CtxHDvcF-7onAGEUp6d9WHrS6tFHy2bK9YyCEE2VVbi2ws-9GLa-Yv_0RVKlPT4pVNI5-AY8nkwmf2DbyxOZsLFXwnNcM2-wex2nJC8oBTJFAd6pnU_jKl6WOYsfx-FQKzDf0BhM1vm__PzTEZRz68G5jqBTW_WmYxtzKQB0S1ngSevkjsSEYD1Va_NGWy66QupdouYP; __Secure-ROLLOUT_TOKEN=CMauzqiXqfe9dRClvauLi_yWAxjt9aby2daXAw%3D%3D; __Secure-1PSIDTS=sidts-CjQBkldj_8fO7Ce6D1Y4PrvphPUB9jfxNax2vuOOll5JSUhSrTbg5_06Tp5wVO9p1ErmCDTOEAA; __Secure-3PSIDTS=sidts-CjQBkldj_8fO7Ce6D1Y4PrvphPUB9jfxNax2vuOOll5JSUhSrTbg5_06Tp5wVO9p1ErmCDTOEAA; SIDCC=APD_SKHHcnFgX2tc_socJUQFawpK4gkoHVfoaSPlk1yMbTYjpp4N4sGoLcxCBntV6k8zQ8qnyw; __Secure-1PSIDCC=APD_SKH4oAKX4ZsBB22T8MRIFFc4yk7S64tKVj492ongp9rRnXndTmH4EtaOgygDt_BMWJGpGw; __Secure-3PSIDCC=APD_SKGerGgS4jUrWzvZXistMQwtwrlzLOvrmJi2u2db36HqoFGbRmPUO6RaQLnj9m9-X4QI5g
origin
https://music.youtube.com
priority
u=1, i
referer
https://music.youtube.com/
sec-ch-ua
"Not:A-Brand";v="8", "Chromium";v="156", "Google Chrome";v="156"
sec-ch-ua-arch
"x86"
sec-ch-ua-bitness
"64"
sec-ch-ua-form-factors
"Desktop"
sec-ch-ua-full-version
"156.0.8078.48"
sec-ch-ua-full-version-list
"Not:A-Brand";v="8.0.0.0", "Chromium";v="156.0.8078.48", "Google Chrome";v="156.0.8078.48"
sec-ch-ua-mobile
?0
sec-ch-ua-model
""
sec-ch-ua-platform
"Windows"
sec-ch-ua-platform-version
"19.0.0"
sec-ch-ua-wow64
?0
sec-fetch-dest
empty
sec-fetch-mode
same-origin
sec-fetch-site
same-origin
user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36
x-browser-channel
stable
x-browser-copyright
Copyright 2026 Google LLC. All Rights Reserved.
x-browser-validation
kExLFzaodIx3FCPz16gbnWIsTHM=
x-browser-year
2026
x-goog-authuser
0
x-goog-visitor-id
CgtMUDJxUkNoM0drdyjo-v7WBjIKCgJVUxIEGgAgSmLHAgrEAkN2QUJDQVVTb2dFQjhRWnVaaU51X3VxTUhZellBY19PR3llNDU5VTIydzBIOWo2RFE4dzdEUTlMcEEtQmZpNE5OV0dmWTZlNXpMWC1sQ29JeXNBRUhPZm9mLW1tejhMVElOVWF2RjJtWkc2X2Nlc3BjaS1Nc1cyMk1lWjZDdHhIRHZjRi03b25BR0VVcDZkOVdIclM2dEZIeTJiSzlZeUNFRTJWVmJpMndzLTlHTGEtWXZfMFRWS2xQVDRwVk5JNS1BWThua3dtZjJEYnl4T1pzTEZYd25OY00yLXdleDJuSkM4b0JUSkZBZDZwblVfaktsNldPWXNmeC1GUUt6RGYwQmhNMXZtX19QelRFWlJ6NjhHNWpxQlRXX1dtWXh0ektRQjBTMW5nU2V2a2pzU0VZRDFWYV9OR1d5NjZRdXBkb3VZUA%3D%3D
x-origin
https://music.youtube.com
x-youtube-bootstrap-logged-in
true
x-youtube-client-name
67
x-youtube-client-version
1.20261025.12.00
"""

def main():
    print("Generating official browser.json config layout...")
    try:
        # Utilizing the package-level setup method directly with headers_raw parameter
        ytmusicapi.setup(filepath="browser.json", headers_raw=headers_raw.strip())
        print("Configuration file parsed and written natively!")
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
    dead_tracks_found = 0

    print("\nScanning tracks...")
    for track in tracks:
        video_id = track.get('videoId')
        title = track.get('title', 'Unknown Title')
        
        if not video_id or track.get('isAvailable') is False:
            dead_tracks_found += 1
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
    print(f"Dead tracks found: {dead_tracks_found}")

    if duplicates_to_remove:
        confirm = input(f"\nWould you like to auto-delete the {len(duplicates_to_remove)} duplicate(s)? (y/n): ")
        if confirm.lower() == 'y':
            print("Purifying duplicates...")
            yt.remove_playlist_items(playlist_id, duplicates_to_remove)
            print("✨ Purification complete! Duplicates removed successfully.")
        else:
            print("Operation canceled. No changes made.")
    else:
        print("\nYour playlist is clean of duplicate items!")
    if dead_tracks_found > 0:
        confirm = input(f"\nWould you like to auto-delete the {dead_tracks_found} dead track(s)? (y/n): ")
        if confirm.lower() == 'y':
            print("Deleting dead tracks...")
            yt.remove_playlist_items(playlist_id, [track for track in tracks if not track.get('isAvailable')])
            print("✨ Purification complete! Dead tracks removed successfully.")
        else:
            print("Operation canceled. No changes made.")

if __name__ == "__main__":
    main()
