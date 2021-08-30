from youtubedownloader import download_audio
from chatdownloader import download_chat
from speechrecognition import get_text
from segmenter import Segmenter
from urllib.parse import urlparse
from urllib.parse import parse_qs
from os import path

# download_chat("https://www.youtube.com/watch?v=i5x64B_V7YY")
url = input("Enter youtube url: ")
delay = input("Enter delay between chat and response in seconds: ")
segment_length = input("Enter the clip length in seconds: ")

url_data = urlparse(url)
query = parse_qs(url_data.query)
basepath = path.dirname(__file__)


print("Downloading audio...")
audio_output_path = path.abspath(path.join(basepath, "..", "audio", query["v"][0] + ".wav"))
download_audio(audio_output_path, url)

print("Downloading chat...")
chat_output_path = path.abspath(path.join(basepath, "..", "chat", query["v"][0] + ".chat"))
download_chat(chat_output_path, url)

speech_output_path = path.abspath(path.join(basepath, "..", "speech", query["v"][0] + ".speech"))
speech_file = open(speech_output_path, "w")

chat_file = open(chat_output_path, "r")
chat_lines = chat_file.readlines()

seg = Segmenter()
print("Loading audio into segmenter...")
seg.load(audio_output_path)

for line in chat_lines:
    timestamp = float(line.split(",")[0]) * 1000
    message = line.split(",")[1]
    start = timestamp + (float(delay) * 1000)
    end = start + (float(segment_length)*1000)
    audio_segment_output_path = path.abspath(
        path.join(basepath, "..", "audio", query["v"][0] + "." + str(start).split(".")[0] + ".segment.wav")
    )
    seg.save_segment(audio_segment_output_path, start, end)
    speech = get_text(audio_segment_output_path)
    print(str(start / 1000) + ", " + str(end / 1000) + ", " + speech)
    speech_file.write(speech + "\n")
speech_file.close()
