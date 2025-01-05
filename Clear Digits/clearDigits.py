def clearDigits(s):
    stack = []
    for c in s:
        if c.isalpha():
            stack.append(c)
        elif c.isdigit() and stack:
            stack.pop()
    return "".join(stack)

print(clearDigits("abc"))                
print(clearDigits("abc123"))
print(clearDigits("123"))
print(clearDigits("12s3"))
print(clearDigits("abcd12eu"))
                
        