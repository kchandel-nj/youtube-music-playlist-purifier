import os
import json
from dotenv import load_dotenv
from ytmusicapi.setup import setup_headers

# Load environment configuration variables from the local .env file
load_dotenv()

def main():
    # Fetch the multi-line raw header string securely from your environment variables
    headers_raw = os.getenv("YT_MUSIC_HEADERS")
    
    if not headers_raw:
        print("CRITICAL ERROR: 'YT_MUSIC_HEADERS' environment variable not found in your .env file.")
        print("Please check your .env file formatting and ensure the raw block is wrapped in double quotes.")
        return

    print("Generating official browser.json config layout from environment variables...")
    try:
        # Pass the environment variable directly to the native setup tool
        setup_headers(headers_raw=headers_raw.strip(), filepath="browser.json")
        print("----------------------------------------")
        print("SUCCESS: browser.json has been created!")
        print("----------------------------------------")
    except Exception as e:
        print(f"Error parsing headers: {e}")

    input("Press Enter to close...")

if __name__ == "__main__":
    main()
