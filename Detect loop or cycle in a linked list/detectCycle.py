class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectCycle(head):
    hash_set = set()
    cur = head
    
    while cur.next is not None:
        if cur in hash_set:
            return True
        hash_set.add(cur)
        cur = cur.next
    return False

def main():
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = head.next
    print(detectCycle(head))

if __name__ == "__main__":
    main()