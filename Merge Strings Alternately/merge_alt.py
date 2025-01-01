# Faster than merge_str_alt
def mergeAlternately(word1: str, word2: str) -> str:
    merged = [s1 + s2 for s1,s2 in zip(word1, word2)]
    return "".join(merged) + word1[len(word2):] + word2[len(word1):]
    
# print(mergeAlternately("abcd", "pq")) #output - apbqcd