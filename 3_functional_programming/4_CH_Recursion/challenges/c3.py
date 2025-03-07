def find_longest_word(document, longest_word=""):
    if len(document) == 0:
        return longest_word
    words = document.split(maxsplit=1)
    if len(words) < 1:
        return longest_word
    first_word = words[0]
    if len(first_word) > len(longest_word):
        longest_word = first_word
    if len(words) < 2:
        return longest_word
    return find_longest_word(words[1], longest_word)


def find_longest_word(document, longest_word=""):
    words = document.split(
        maxsplit=1
    )  # Split at the first space to avoid excessive splitting
    if not words:  # Base case: if no words remain, return the longest found word
        return longest_word
    first_word = words[0]
    rest_of_document = (
        words[1] if len(words) > 1 else ""
    )  # Handle edge cases where there's no second part
    return find_longest_word(
        rest_of_document,
        first_word if len(first_word) > len(longest_word) else longest_word,
    )
