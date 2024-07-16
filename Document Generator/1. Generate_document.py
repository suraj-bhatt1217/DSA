characters = "Today is a beautiful day and the sun is shining brightly"
document = "the sun is shining"


def doc_gen(character, document):
    freq_count = {}
    for char in characters:
        freq_count[char] = freq_count.get(char, 0) + 1

    for char in document:
        freq_count[char] = freq_count.get(char, 0) - 1
        if freq_count[char] < 0:
            return False
    return True


print(doc_gen(characters, document))
