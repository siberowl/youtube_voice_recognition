import speech_recognition as sr

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


def save_speech(output_path, audio_path):
    f = open(output_path, "w")
    text = getText(audio_path)
    f.write(text)
