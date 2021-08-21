import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

for i in range(4):
    filename = "./sample_audio/sample" + str(i + 1) + ".wav"
    # open the file
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data, language="ja-JP")
            print("filename: " + filename + " text: " + text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(
                    e
                )
            )
