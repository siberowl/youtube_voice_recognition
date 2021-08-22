import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()


def getText(path):
    # open the file
    with sr.AudioFile(path) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data, language="ja-JP")
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio"
        except sr.RequestError:
            return "Could not request results from Google"
