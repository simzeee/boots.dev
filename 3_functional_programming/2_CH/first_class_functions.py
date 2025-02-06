def file_to_prompt(file, to_string):
    stringified = to_string(file)
    return f"```\n{stringified}\n```"


def file_type_getter(file_extension_tuples):
    file_extensions_dict = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            file_extensions_dict[ext] = tup[0]
    return lambda ext: file_extensions_dict.get(ext, "Unknown")


def change_bullet_style(document):
    return "\n".join(map(convert_line, document.split("\n")))


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line


def remove_invalid_lines(document):
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )


import functools


def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence


def join_first_sentences(sentences, n):
    if n == 0:
        return ""
    return functools.reduce(join, sentences[:n]) + "."
