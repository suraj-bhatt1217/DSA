def validParentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for c in s:
        if c in mapping.values():
            stack.append(c)
        elif c in mapping:
            if stack and stack[-1] == mapping[c]:
                stack.pop()
            else:
                return False
        else:
            return False
    return len(stack) == 0

def main():
    print(validParentheses("[()]{}{[()()]()}"))
    print(validParentheses("(])"))
    
if __name__ == "__main__":
    main()