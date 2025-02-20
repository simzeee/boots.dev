def stylize_title(document):
    return add_border(center_title(document))


# Don't touch below this line


def center_title(document):
    width = 40
    title = document.split("\n")[0]
    centered_title = title.center(width)
    return document.replace(title, centered_title)


def add_border(document):
    title = document.split("\n")[0]
    border = "*" * len(title)
    return document.replace(title, title + "\n" + border)


def add_prefix(document, documents):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    # documents.append(new_doc)
    # create new tuple
    documents += (new_doc,)
    return documents


def get_median_font_size(font_sizes):
    if not font_sizes:
        return None

    sorted_font_sizes = sorted(font_sizes)
    length = len(font_sizes)

    if length % 2 != 0:
        return sorted_font_sizes[length // 2]
    else:
        return sorted_font_sizes[length // 2 - 1]


def format_line(line):
    # print('stripped', f"{line.rstrip()}")
    # print('stripped and capital:', f"{line.rstrip().upper()}")
    return f"{line.strip().upper().replace('.', '')}..."
