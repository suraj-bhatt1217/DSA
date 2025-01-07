class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findMiddle(head):
    slowPrev = None
    slow = fast = head
    while fast and fast.next:
        slowPrev = slow
        slow = slow.next
        fast = fast.next.next
    return slowPrev
        

def deleteMiddle(head):
    if not head or not head.next:
        return None
    slowPrev = findMiddle(head)
    slowPrev.next = slowPrev.next.next
    return head     

def printList(head):
    cur = head
    while cur:
        print(cur.data, end=" -> ")
        cur = cur.next

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    print("Before deleting middle of linked list:")
    printList(head)
    head = deleteMiddle(head)
    print("After deleting middle of linked list:")
    printList(head)

if __name__ == "__main__":
    main()