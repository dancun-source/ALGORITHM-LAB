# Tree.py
# Non-Linear Data Structure: Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating nodes
root = Node(100)
root.left = Node(50)
root.right = Node(150)
root.left.left = Node(25)
root.left.right = Node(75)

# Simple traversal: Root → Left → Right
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

print("Preorder Traversal of Tree:")
preorder(root)
