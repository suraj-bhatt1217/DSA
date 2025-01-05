def validAnagram(s, t):
    return sorted(s) == sorted(t)

print(validAnagram("listen", "silent"))  # Output: True
print(validAnagram("rat", "car"))        # Output: False
print(validAnagram("anagram", "nagaram")) # Output: True