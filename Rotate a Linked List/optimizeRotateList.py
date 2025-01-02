# Time Complexity - O(n) Space Complexity - O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def rotateList(head, k):
    if k == 0 or head is None:
        return head
    
    cur = head
    length = 1
    while cur.next is not None:
        length += 1
        cur = cur.next
        
    k %= length
    cur.next = head
    cur = cur.next
    
    for _ in range(1, k):
        cur = cur.next
    
    head = cur.next
    cur.next = None
            
    return head

def printList(head):
    cur = head
    while cur is not None:
        print(cur.data, end="-->")
        cur = cur.next
    print()
    
        
def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    
    print("Before Reversing:")
    printList(head)
    k = 2
    print(k)
    head = rotateList(head, k)
    print("After Rotating:")
    printList(head)
if __name__ == "__main__":
    main()