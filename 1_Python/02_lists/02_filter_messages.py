def filter_messages(messages):
    filter_messages = []
    count_list = []
    for message in messages:
        split_message_list = message.split()
        non_bad_list = []
        counter = 0
        for word in split_message_list:
            if word == "dang":
                counter += 1
            else:
                non_bad_list.append(word)
        clean_message = " ".join(non_bad_list)
        filter_messages.append(clean_message)
        count_list.append(counter)
    return filter_messages, count_list
