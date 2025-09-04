# youtube-dl-helper

A simple command-line tool to download YouTube videos and playlists using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

- Download single videos or full playlists
- Automatically selects 1080p max resolution
- Optionally download and embed subtitles
- Saves files in organized folders
- Uses your Firefox cookies for auth (e.g. to download private/watch-later videos)

## Installation

1. Clone the repo:

	```bash
	git clone https://github.com/YOUR_USERNAME/youtube-dl-helper.git
	cd youtube-dl-helper
	```

2.	Install dependencies:

	```bash
	pip install -r requirements.txt
	```

3.	Make sure `yt-dlp` is installed (via pip or brew):

	```bash
	brew install yt-dlp
	# or
	pip install yt-dlp
	```

## Usage

```bash
python yt_downloader/main.py [--subs]
```

Use the `--subs` flag to download subtitles (auto-generated if available). Subtitles will be embedded into the video file.

```bash
Paste video URL(s), comma-separated (or 'q' to quit): https://www.youtube.com/watch?v=abc123, https://youtube.com/playlist?list=XYZ
```

## TODO

1.	✅ ~~Logging to a file (yt_downloader.log)~~
2.	✅ ~~Toggle subtitle download via CLI arg~~
3.	Batch input from file
4.	Post-download metadata viewer
5.	✅ ~~Retry logic / progress bar~~