from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root, data):
    if root is None:
        root = Node(data)
        
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node.left is None:
            node.left = Node(data)
            break
        else:
            queue.append(node.left)
            
        if node.right is None:
            node.right = Node(data)
            break 
        else:
            queue.append(node.right)
                
               
def inorder(node):
    if node is None:
        return

    inorder(node.left)
    print(node.data, end = " ")
    inorder(node.right)
    
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    print("Inorder traversal before inserting new node:\n ", inorder(root))
    insert(root, 8)
    print("Inorder traversal after inserting new node:\n ", inorder(root))