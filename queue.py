# Queue.py
# Dynamic Linear Data Structure: Queue (First In, First Out)

from collections import deque

queue = deque()

# Adding elements
queue.append("Job1")
queue.append("Job2")
queue.append("Job3")

print("Queue before dequeue:", queue)

# Removing first element
first_item = queue.popleft()
print("Dequeued element:", first_item)
print("Queue after dequeue:", queue)
