from chat_downloader import ChatDownloader
import re

url = "https://youtu.be/RqDU86c7Nu4"
f = open(re.sub("[^A-Za-z0-9]+", "", url) + "_chat.json", "w")
chat = ChatDownloader().get_chat(url)  # create a generator
for message in chat:  # iterate over messages
    chat.print_formatted(message)  # print the formatted message
    f.write(str(message["time_in_seconds"]) + ", " + message["message"] + "\n")
f.close()
