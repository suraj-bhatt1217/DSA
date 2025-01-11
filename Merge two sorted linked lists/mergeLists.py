class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def sortedMerge(head1, head2):
    arr = []  

    while head1 is not None:
        arr.append(head1.data)
        head1 = head1.next

    while head2 is not None:
        arr.append(head2.data)
        head2 = head2.next

    arr.sort()

    dummy = Node(-1)
    curr = dummy

    for value in arr:
        curr.next = Node(value)
        curr = curr.next

    return dummy.next 

def printList(curr):
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    head1 = Node(5)
    head1.next = Node(10)
    head1.next.next = Node(15)

    head2 = Node(2)
    head2.next = Node(3)
    head2.next.next = Node(20)

    res = sortedMerge(head1, head2)

    printList(res)