def convert_file_format(filename, target_format):
    valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
    valid_conversions = {
        "docx": ["pdf", "txt", "md"],
        "pdf": ["docx", "txt", "md"],
        "txt": ["docx", "pdf", "md"],
        "pptx": ["ppt", "pdf"],
        "ppt": ["pptx", "pdf"],
        "md": ["docx", "pdf", "txt"],
    }

    current_format = filename.split(".")[-1]
    if (
        current_format in valid_extensions
        and target_format in valid_conversions[current_format]
    ):
        return filename.replace(current_format, target_format)
    return None


def add_format(default_formats, new_format):
    formats_copy = default_formats.copy()
    formats_copy[new_format] = True
    return formats_copy


def remove_format(default_formats, old_format):
    formats_copy = default_formats.copy()
    formats_copy[old_format] = False
    return formats_copy


def convert_case(text, target_format):
    if not text or not target_format:
        raise ValueError(f"no text or target format provided")

    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"unsupported format: {target_format}")


def remove_emphasis_from_word(word):
    # remove from each word
    if word.endswith("\n"):
        return word[:-1].strip("*") + "\n"
    return word.strip("*")


def remove_emphasis_from_line(line):
    result = list(map(remove_emphasis_from_word, line))
    return result


def remove_emphasis(doc_content):
    split_content = doc_content.split(" ")
    result = remove_emphasis_from_line(split_content)
    return " ".join(result)


# def remove_emphasis_from_word(word):
#     return word.strip("*")


# def remove_emphasis_from_line(line):
#     words = line.split()
#     new_words = map(remove_emphasis_from_word, words)
#     return " ".join(new_words)


# def remove_emphasis(doc_content):
#     lines = doc_content.split("\n")
#     new_lines = map(remove_emphasis_from_line, lines)
#     return "\n".join(new_lines)


def word_count_memo(document, memos):
    memos_copy = memos.copy()
    if document in memos_copy:
        return memos_copy[document], memos_copy
    else:
        string_count = word_count(document)
        memos_copy[document] = string_count
        return string_count, memos_copy


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count
