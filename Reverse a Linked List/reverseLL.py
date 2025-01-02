class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getReversedLL(head):
    cur = head
    prev = None
    
    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev    

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    print(getReversedLL(head).data)
    
if __name__ == "__main__":
    main()   