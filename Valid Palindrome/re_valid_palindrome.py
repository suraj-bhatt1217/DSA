import re

def valid_palindrome(string):
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    print(cleaned_string)
    return cleaned_string == cleaned_string[::-1]

# Test cases
print(valid_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(valid_palindrome("race a car"))                     # Output: False
print(valid_palindrome(""))                               # Output: True
print(valid_palindrome(" "))                              # Output: True