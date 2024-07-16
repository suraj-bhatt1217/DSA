# T-O(V + E) | S-O(V)
class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addNode(self, name):
        self.children.append(Node(name))
        return self.children

    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array

    def __repr__(self):
        return self.name


A = Node("A")
B = A.addNode("B")[0]
C = A.addNode("C")[1]
D = A.addNode("D")[2]
# print(A.children)
E = B.addNode("E")[0]
F = B.addNode("F")[1]
I = F.addNode("I")[0]
J = F.addNode("J")[1]
G = D.addNode("G")[0]
H = D.addNode("H")[1]
K = G.addNode("K")[0]

print(A.depth_first_search([]))
