from math import gcd


def gcdOfStrings(s1, s2):
    if s1 + s2 != s2 + s1:
        return ""
    return s1[: gcd(len(s1), len(s2))]


print(gcdOfStrings("ABCABC", "ABC"))
print(gcdOfStrings("ABABAB", "ABAB"))
