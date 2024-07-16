# T-O(n) | S-O(1)
string = "abcdcaf"


def first_non_repeating_character(string):
    freq_count = dict()
    for char in string:
        freq_count[char] = freq_count.get(char, 0) + 1

    for char in string:
        count_char = freq_count[char]
        if count_char == 1:
            return char
    return -1


print(first_non_repeating_character(string))
