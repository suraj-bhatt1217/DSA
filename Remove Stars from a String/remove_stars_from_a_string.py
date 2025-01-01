def removeStars(s : str) -> str:
    stack = []
    for char in s:
        if char == "*":
            stack and stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

# print(removeStars("leet**cod*e")) #output-"lecoe"