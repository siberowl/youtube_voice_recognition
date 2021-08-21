from chat_downloader import ChatDownloader

url = "https://youtu.be/RqDU86c7Nu4"
chat = ChatDownloader().get_chat(url)  # create a generator
for message in chat:  # iterate over messages
    chat.print_formatted(message)  # print the formatted message
