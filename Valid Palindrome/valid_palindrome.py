# Overall Time Complexity: 
# 𝑂(𝑛).
def valid_palindrome(string):
    return string == string[::-1]

# Test cases
print(valid_palindrome('abcba'))  # Output: True (Palindrome)
print(valid_palindrome('hello'))  # Output: False (Not a palindrome)
print(valid_palindrome(''))       # Output: True (Empty string is a palindrome)
print(valid_palindrome('a'))      # Output: True (Single character is a palindrome)


# Time Complexity:
# Reversing the string: The slicing operation string[::-1] creates a reversed copy of the string. This operation takes O(n), where n is the length of the string.
# Comparison: Comparing the original string with the reversed string also takes 
# 𝑂(𝑛), as each character must be checked.

