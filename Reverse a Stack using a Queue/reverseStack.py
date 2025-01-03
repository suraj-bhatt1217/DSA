from collections import deque

def reverseStack(stack):
    queue = deque()
    while stack:
        queue.append(stack.pop())
        
    while queue:
        stack.append(queue.popleft())

    return stack

print(reverseStack([1, "Two", 3, False, 5]))