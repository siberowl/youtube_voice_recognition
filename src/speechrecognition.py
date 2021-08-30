import speech_recognition as sr
from urllib.parse import urlparse
from urllib.parse import parse_qs
from os import path



def getText(audio_path):
    # initialize the recognizer
    r = sr.Recognizer()
    # open the file
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data, language="ja-JP")
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError:
            return "Could not request results from Google"


def save_speech(url):
    url_data = urlparse(url)
    query = parse_qs(url_data.query)
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "speech", query["v"][0] + ".speech"))
    f = open(filepath, "w")
    audio_filepath = path.abspath(path.join(basepath, "..", "audio", query["v"][0] + ".wav"))
    text = getText(audio_filepath)
    f.write(text)
