# T-O(n) | S-O(n)
import string

astring = "xyz"
key = 2
alphabets = list(string.ascii_lowercase)


def ccencryptor(astring, key):
    key %= 26
    encrypted_string = [get_enc_char(chr, key) for chr in astring]
    return "".join(encrypted_string)


def get_enc_char(char, key):
    idx_char = alphabets.index(char)
    enc_idx_char = idx_char + key
    if enc_idx_char <= 25:
        return alphabets[enc_idx_char]
    else:
        return alphabets[enc_idx_char % 26]


print(ccencryptor(astring, key))
