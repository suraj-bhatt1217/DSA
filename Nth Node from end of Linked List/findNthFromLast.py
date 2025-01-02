# Naive approach - Iterative solution
# Time Complexity - O(n*k) Space Complexity - O(1)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findNthFromLast(head, n):
    if n == 0 or head is None:
        return None
    
    length = 1
    cur = head
    while cur.next is not None:
        length += 1
        cur = cur.next
        
    if n > length:
        return -1
    
    k = length - n
    cur = head
    
    for _ in range(k):
        cur = cur.next
        
    return cur.data
        
def rotateList(head, k):
    if k == 0 or head is None:
        return head
    for _ in range(k):
        cur = head
        while cur.next is not None:
            cur = cur.next
        cur.next = head
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
    
    print(findNthFromLast(head, 7))
    
if __name__ == "__main__":
    main()
    