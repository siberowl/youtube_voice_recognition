from youtubedownloader import download_audio
from chatdownloader import download_chat
from speechrecognition import get_text
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
speech_output_path = path.abspath(path.join(basepath, "..", "speech", query["v"][0] + ".speech"))

print("Downloading audio...")
download_audio(audio_output_path, url)
print("Downloading chat...")
download_chat(chat_output_path, url)

chat_file = open(chat_output_path, "r")
chat_lines = chat_file.readLines()
speech_file = open(speech_output_path, "w")
for line in chat_lines:
    timestamp = float(line.split(",")[0]) * 1000
    message = line.split(",")[1]
    audio_segment_output_path = path.abspath(
        path.join(basepath, "..", "audio", query["v"][0] + "." + timestamp + ".wav")
    )
    save_segment(audio_output_path, audio_segment_output_path, timestamp, timestamp + delay * 1000)
    speech = get_text(audio_segment_output_path)
    speech_file.write(speech + "\n")
speech.close()
