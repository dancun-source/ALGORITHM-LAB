# Stack.py
# Dynamic Linear Data Structure: Stack (Last In, First Out)

stack = []

# Pushing elements
stack.append("Page1")
stack.append("Page2")
stack.append("Page3")

print("Stack before pop:", stack)

# Popping last element
last_item = stack.pop()
print("Popped element:", last_item)
print("Stack after pop:", stack)
