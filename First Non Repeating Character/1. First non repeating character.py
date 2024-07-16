# T-O(n^2) | S-O(1)
string = "abcdcaf"


def first_non_repeating_character(string):
    for i in range(len(string)):
        found_duplicates = False
        for j in range(len(string)):
            if i != j and string[i] == string[j]:
                found_duplicates = True
        if found_duplicates != True:
            return string[i]
    return -1


print(first_non_repeating_character(string))
