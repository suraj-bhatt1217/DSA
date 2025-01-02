class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getLength(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length
    
    
def getMiddle(head):
    length = getLength(head)
    mid = length // 2
    while mid:
        head = head.next
        mid -= 1
    return head.data
    
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    print(getMiddle(head))
    
if __name__ == "__main__":
    main()