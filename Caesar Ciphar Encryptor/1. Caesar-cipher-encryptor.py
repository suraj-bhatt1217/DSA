# T-O(n) | S-O(n)
def ceasar_cipher_encryptor(s, key):
    e_string = []
    for char in s:
        e_string.append(get_encrypted_value(char, key))
    return "".join(e_string)


def get_encrypted_value(char, key):
    key %= 26
    new_ord_value = ord(char) + key
    if new_ord_value <= 122:
        return chr(new_ord_value)
    else:
        return chr(97 + new_ord_value % 123)


a_string = "xyz"
key = 2


print(ceasar_cipher_encryptor(a_string, key))
