from collections import Counter

def validAnagram(s, t):
    return Counter(s) == Counter(t)
    
print(validAnagram("listen", "silent"))  # Output: True
print(validAnagram("rat", "car"))        # Output: False
print(validAnagram("anagram", "nagaram")) # Output: True