from chat_downloader import ChatDownloader


def download_chat(output_path, url):
    f = open(output_path, "w")
    chat = ChatDownloader().get_chat(url)  # create a generator
    for message in chat:  # iterate over messages
        chat.print_formatted(message)  # print the formatted message
        f.write(str(message["time_in_seconds"]) + ", " + message["message"] + "\n")
    f.close()
