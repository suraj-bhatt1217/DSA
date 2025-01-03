def reverseString(s):
    revStack = []
    # stack = []
    # for c in s:
    #     stack.append(c)
    stack = list(s)
    for _ in range(len(stack)):
        revStack.append(stack.pop())
        
    return "".join(revStack)
    
print(reverseString("TechQuiz"))