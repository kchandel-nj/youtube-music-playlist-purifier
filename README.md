# YouTube Music Playlist Purifier 🧹

A lightweight Python script utilizing `ytmusicapi` to connect securely to your YouTube Music account, scan your library playlists, and clean them by removing duplicate tracks.

## ✨ Features
* **Natively Parsed Authentication:** Safely initializes authentication directly via browser network session headers.
* **Interactive Selection:** Displays all playlists in your library so you can pick exactly which one to scan.
* **Duplicate Detection:** Scans your track listings and logs every duplicate instance it identifies.
* **Dead Track Identification:** Spots unavailable or deleted tracks that no longer play.
* **Safe Automated Purge:** Deletes duplicate tracks while preserving your original track listing intact.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed on your system. Install the required `ytmusicapi` library package:
```powershell
pip install ytmusicapi
```

### 2. Setup & Authentication
The script uses browser network headers to authenticate as your account. 
1. Open **YouTube Music** in your browser and sign in.
2. Press `F12` (or right-click -> **Inspect**) to open the Developer Tools.
3. Head to the **Network** tab.
4. Interact with the page (e.g., search for a song) to trigger traffic.
5. Find a request named `browse` or `search`, view its **Headers** tab, and copy everything under **Request Headers**.
6. Open `purify.py` and paste your copied text block into the `headers_raw` multi-line string variable.

### 3. Usage
Run the script from your terminal:
```powershell
python purify.py
```
Follow the on-screen terminal prompts to select your target playlist and confirm the duplicate purge.

## 🛠️ Project Structure
* `purify.py` - Core script containing header conversion, library connectivity, scanning algorithms, and the automated removal pipeline.
* `browser.json` - Generated automatically on execution to house structured authentication states.
