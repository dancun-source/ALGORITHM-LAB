# LinkedList.py
# Dynamic Linear Data Structure: Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # points to the next node

# Creating nodes
head = Node(10)
second = Node(20)
third = Node(30)

# Linking nodes
head.next = second
second.next = third

# Traversing the linked list
current = head
print("Linked List Elements:")
while current:
    print(current.data)
    current = current.next
