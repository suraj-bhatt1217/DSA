class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectCycle(head):
    fast = slow = head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False        

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = head.next
    print(detectCycle(head))

if __name__ == "__main__":
    main()