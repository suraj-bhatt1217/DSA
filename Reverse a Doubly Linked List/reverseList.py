class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def reverseList(head):
    curr = head
  
    if curr is None:
        return None

    temp = curr.prev
    curr.prev = curr.next
    curr.next = temp

    if curr.prev is None:
        return curr

    return reverseList(curr.prev)

def print_list(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next
    head.next.next.next = Node(4)
    head.next.next.next.prev = head.next.next

    print("Original Linked list")
    print_list(head)
    head = reverseList(head)
    print("\nReversed Linked list")
    print_list(head)