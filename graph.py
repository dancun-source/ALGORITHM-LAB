# Graph.py
# Non-Linear Data Structure: Graph (Adjacency List)

# Representing a simple graph
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

# Print neighbors of each node
print("Graph Representation:")
for node, edges in graph.items():
    print(f"{node} -> {edges}")

# Example: Check connections from A
print("Neighbors of A:", graph["A"])
