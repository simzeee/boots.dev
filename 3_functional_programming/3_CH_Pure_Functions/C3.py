def map_keywords(document, document_map):
    map_copy = document_map.copy()
    if document in document_map:
        return map_copy[document], map_copy
    found_keywords = find_keywords(document)
    map_copy[document] = found_keywords
    return found_keywords, map_copy


def find_keywords(document):
    keywords = [
        "functional",
        "immutable",
        "declarative",
        "higher-order",
        "lambda",
        "deterministic",
        "side-effects",
        "memoization",
        "referential transparency",
    ]
    filtered_list = list(filter(lambda word: word in document, keywords))
    return filtered_list
