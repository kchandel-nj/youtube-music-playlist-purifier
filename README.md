# YouTube Music Playlist Purifier 🧹

A secure, interactive Python automation pipeline utilizing `ytmusicapi` to connect directly to your YouTube Music account, scan your library catalog, and scrub selected playlists clean of duplicate entries and unavailable/dead tracks.

## ✨ Features
* **🔒 Env Vaulting:** Session tokens are kept out of source code using a secure local configuration context.
* **📂 Automated Handshake Translation:** Automatically extracts raw web signatures into library-compliant profile structures.
* **📋 Dynamic Selection Catalog:** Scans your live profile environment and provides an interactive terminal directory of your playlists.
* **👯 Strict Duplicate Purging:** Discovers recurring tracks and safely filters them out while preserving original layout sequencing.
* **❌ Structural Dead Track Stripping:** Captures and strips out hidden unplayable tracks or entries deleted by original owners.

## 🚀 Getting Started

### 1. Installation & Environment Setup
Install the core API library alongside the environment engine wrapper:
```powershell
pip install ytmusicapi python-dotenv
```

### 2. Configure Credentials (`.env`)
1. Create a file named `.env` in the root folder of your project.
2. Open **YouTube Music** in your browser and verify you are logged into your target profile account.
3. Open your browser Developer Tools (`F12`), head to the **Network** tab, and filter by `browse` or `search` actions.
4. Click on a successful request entity header item, scroll down to **Request Headers**, and copy the complete raw text layout block.
5. Paste it inside your `.env` target variable. Ensure the full multi-line configuration block is wrapped inside double quotes:

```env
YT_MUSIC_HEADERS="accept
*/*
accept-encoding
gzip, deflate, br, zstd
...[paste the rest of your copied header block here]..."
```

### 3. Usage Pipeline

#### Step A: Build Configuration Core
Execute the layout conversion script to extract your environment variables into an authentication state:
```powershell
python setup.py
```

#### Step B: Execute Playlist Purification
Run the primary purification utility pipeline:
```powershell
python purify.py
```
Follow the interactive prompt directory to choose your target music collection and authorize removals.

## ⚠️ Repository Protection
To prevent secret personal cookies from leaking into public repository records, create a `.gitignore` file mapping these parameters:
```text
.env
browser.json
```
