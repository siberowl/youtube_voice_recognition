import speech_recognition as sr
filename = "./sample_audio/sample1.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data, language="ja-JP")
    print(text)
