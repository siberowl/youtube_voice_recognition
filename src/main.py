from youtubedownloader import download_audio
from chatdownloader import download_chat
from speechrecognition import save_speech

# download_chat("https://www.youtube.com/watch?v=i5x64B_V7YY")
url = input("Enter url: ")
print("Downloading audio...")
download_audio(url)
print("Saving speech...")
save_speech(url)
