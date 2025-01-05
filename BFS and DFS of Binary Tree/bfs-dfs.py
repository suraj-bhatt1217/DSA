# Test commit
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def BFS(root):
    if root is None:
        return
    
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        print(node.data, end = " ")
        
        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)

def inorder_DFS(node):
    if node is None:
        return
    
    inorder_DFS(node.left)
    print(node.data, " ")
    inorder_DFS(node.right)
    
def preorder_DFS(node):
    if node is None:
        return
    
    print(node.data, " ")
    preorder_DFS(node.left)
    preorder_DFS(node.right)    

def postorder_DFS(node):
    if node is None:
        return
    
    postorder_DFS(node.left)
    postorder_DFS(node.right)             
    print(node.data, " ")
    
if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("In-order DFS: ", end='')
    inorder_DFS(root)
    print("\nPre-order DFS: ", end='')
    preorder_DFS(root)
    print("\nPost-order DFS: ", end='')
    postorder_DFS(root)
    print("\nLevel order: ", end='')
    BFS(root)