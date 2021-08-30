from chat_downloader import ChatDownloader
from urllib.parse import urlparse
from urllib.parse import parse_qs
from os import path


def download_chat(url):
    url_data = urlparse(url)
    query = parse_qs(url_data.query)
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "chat", query["v"][0] + ".chat"))
    f = open(filepath, "w")
    chat = ChatDownloader().get_chat(url)  # create a generator
    for message in chat:  # iterate over messages
        chat.print_formatted(message)  # print the formatted message
        f.write(str(message["time_in_seconds"]) + ", " + message["message"] + "\n")
    f.close()
