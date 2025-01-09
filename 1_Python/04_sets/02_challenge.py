def count_vowels(text):
    vowels_lowercase = ["a", "e", "i", "o", "u"]
    vowels_uppercase = ["A", "E", "I", "O", "U"]
    vowel_count = 0
    vowel_set = set()

    for letter in text:
        if letter in vowels_lowercase or letter in vowels_uppercase:
            vowel_count += 1
            vowel_set.add(letter)
    return vowel_count, vowel_set
