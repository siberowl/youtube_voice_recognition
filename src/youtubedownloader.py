from __future__ import unicode_literals
import youtube_dl
from os import path


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting ...")
    if d["status"] == "downloading":
        print(d["filename"], d["_percent_str"], d["_eta_str"])


def download_audio(link):
    basepath = path.dirname(__file__)
    ydl_opts = {
        "outtmpl": path.abspath(path.join(basepath, "..", "audio", "%(id)s.%(ext)s")),
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "logger": MyLogger(),
        "progress_hooks": [my_hook],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
