def mergeAlternately(word1: str, word2: str) -> str:
        i = 0
        merged_str_chars = []
        while i != len(word1) and i != len(word2):
            merged_str_chars.append(word1[i])
            merged_str_chars.append(word2[i])
            i += 1
        
        while i < len(word1):
            merged_str_chars.append(word1[i])
            i += 1
        
        while i < len(word2):
            merged_str_chars.append(word2[i])
            i += 1

        return "".join(merged_str_chars)
    
# print(mergeAlternately("abcd", "pq")) #output - apbqcd