def get_common_formats(formats1, formats2):
    return set(formats1).intersection(set(formats2))


valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    zipped = list(zip(doc_names, doc_formats))
    return filter(lambda x: x[1] in valid_formats, zipped)


def restore_documents(originals, backups):
    return set(filter(lambda x: not x.isdigit(), (map(str.upper, originals + backups))))
