class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def convertToCircularList(cur, head):
    if cur.next == None:
        cur.next = head
        return
        
    convertToCircularList(cur.next, head)

def printList(head):
    curr = head
    
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == head:
            break
    print()

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)    
    convertToCircularList(head, head)
    printList(head)
    