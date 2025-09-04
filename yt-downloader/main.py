import argparse
import logging
import os
import subprocess
from pathlib import Path

# Setup logging
LOG_FILE = "yt_downloader.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube videos or playlists using yt-dlp."
    )
    parser.add_argument(
        "--subs", action="store_true", help="Download subtitles if available"
    )
    args = parser.parse_args()

    DOWNLOAD_DIR = Path.home() / "Downloads" / "yt_downloads"
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

    print("YouTube Downloader\n----------------------")

    while True:
        url_input = input(
            "Paste video URL(s), comma-separated (or 'q' to quit): "
        ).strip()
        if url_input.lower() == "q":
            logging.info("User exited the downloader.")
            break
        if not url_input:
            continue

        urls = [u.strip() for u in url_input.split(",") if u.strip()]

        for url in urls:
            download_video(url, DOWNLOAD_DIR, download_subs=args.subs)


def download_video(url: str, download_dir: Path, download_subs: bool = False):
    # Base yt-dlp command
    cmd = [
        "yt-dlp",
        "-f",
        "bv*[height<=1080]+ba/b[height<=1080]",
        "--cookies-from-browser",
        "firefox",
        "--retries",
        "999999",
        # "--write-subs", "--write-auto-subs", "--sub-langs", "en", "--embed-subs",
    ]

    if download_subs:
        cmd += [
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs",
            "en",
            "--embed-subs",
        ]

    if "playlist" in url.lower():
        output_template = download_dir / "%(playlist_title)s" / "%(title)s.%(ext)s"
        cmd += ["-o", str(output_template), url]
    else:
        cmd += ["-P", str(download_dir), url]

    log_message = f"Running: {' '.join(cmd)}"
    print("\n" + log_message + "\n")
    logging.info(log_message)

    try:
        subprocess.run(cmd, check=True)
        logging.info(f"Successfully downloaded: {url}")
    except subprocess.CalledProcessError as e:
        error_message = f"Download failed for {url}: {e}"
        print(error_message)
        logging.error(error_message)


if __name__ == "__main__":
    main()
