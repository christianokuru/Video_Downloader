import subprocess
import socket
import time
import os

class VideoDownloader:
    def __init__(self):
        self.resolutions = [
            ("144p", "256x144", "Approx. 100 MB"),
            ("240p", "426x240", "Approx. 200 MB"),
            ("360p", "640x360", "Approx. 400 MB"),
            ("480p", "854x480", "Approx. 700 MB"),
            ("720p", "1280x720", "Approx. 1 GB"),
            ("1080p", "1920x1080", "Approx. 2 GB"),
            ("1440p", "2560x1440", "Approx. 4 GB"),
            ("2160p", "3840x2160", "Approx. 8 GB")
        ]
        self.download_folder = "video_downloads"

    def create_download_folder(self):
        if not os.path.exists(self.download_folder):
            os.mkdir(self.download_folder)

    def download_video(self, url):
        self.create_download_folder()
        print("Available resolutions:")
        for i, (resolution, resolution_size, video_size) in enumerate(self.resolutions):
            print(f"{i + 1}. {resolution} ({resolution_size}) - {video_size}")

        choice = int(input("Enter the number corresponding to the desired resolution: "))
        selected_resolution = self.resolutions[choice - 1][0]
        format_string = f"bestvideo[height<={selected_resolution}]+bestaudio/best"
        
        while True:
            try:
                socket.create_connection(("www.google.com", 80), 2)
                print("Internet connection is good, starting download...")
                subprocess.run(["youtube-dl", "-f", format_string, "-o", f"{self.download_folder}/%(title)s.%(ext)s", url])
                break
            except OSError:
                print("Poor network connection detected, pausing download...")
                time.sleep(30)
                print("Resuming download...")

    def download_audio(self, url):
        self.create_download_folder()
        subprocess.run(["youtube-dl", "-f", "bestaudio/best", "-x", "--audio-quality", "0", "-o", f"{self.download_folder}/%(title)s.%(ext)s", url])

video_downloader = VideoDownloader()
url = input("Enter the YouTube video link: ")
video_downloader.download_video(url)
