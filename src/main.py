from youtubedownloader import download_audio
from chatdownloader import download_chat
from speechrecognition import save_speech
from segmenter import save_segment
from urllib.parse import urlparse
from urllib.parse import parse_qs
from os import path

# download_chat("https://www.youtube.com/watch?v=i5x64B_V7YY")
url = input("Enter youtube url: ")
delay = input("Enter delay between chat and response in seconds: ")

url_data = urlparse(url)
query = parse_qs(url_data.query)
basepath = path.dirname(__file__)
chat_output_path = path.abspath(path.join(basepath, "..", "chat", query["v"][0] + ".chat"))
audio_output_path = path.abspath(path.join(basepath, "..", "audio", query["v"][0] + ".wav"))
audio_segment_output_path = path.abspath(path.join(basepath, "..", "audio", query["v"][0] + ".segment.wav"))
speech_output_path = path.abspath(path.join(basepath, "..", "speech", query["v"][0] + ".speech"))

print("Downloading audio...")
download_audio(audio_output_path, url)
print("Downloading chat...")
download_chat(chat_output_path, url)

chat_file = open(chat_output_path, "r")
chat_lines = chat_file.readLines()
for line in chat_lines:
    pass
