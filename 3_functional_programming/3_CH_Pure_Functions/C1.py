default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    dict = commands.copy()
    dict[new_command] = function
    return dict


def add_format(formats, format):
    list = [*formats]
    list.append(format)
    return list


def save_document(docs, file_name, doc):
    results = docs.copy()
    results[file_name] = doc
    return results


def add_line_break(line):
    return line + "\n\n"

