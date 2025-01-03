def deleteLastOccurrence(head, key):
    cur = head
    last = None
    lastPrev = None
    prev = None
    
    while cur is not None:
        if cur.data == key:
            last = cur
            lastPrev = prev
        prev = cur
        cur = cur.next
    
    if last is not None:
        if lastPrev is None:
            head = head.next
        else:
            lastPrev.next = last.next
    
    return head

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(head):
    cur = head
    while cur is not None:
        print(cur.data, end="-->")
        cur = cur.next
    print()
    
        
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(4)
    key = 1
    print("Original list:")
    printList(head)
    
    head = deleteLastOccurrence(head, key)
    print("After deleting the last occurrence of", key, ":")
    printList(head)
    
if __name__ == "__main__":
    main()
    
