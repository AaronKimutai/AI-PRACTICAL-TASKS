import networkx as nx
import matplotlib.pyplot as plt

# Colors available
colors = ["Red", "Green", "Blue"]

# Regions
regions = ["WA", "NT", "SA", "QLD", "NSW"]

# Adjacency relationships
adjacency = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "QLD"],
    "SA": ["WA", "NT", "QLD", "NSW"],
    "QLD": ["NT", "SA", "NSW"],
    "NSW": ["SA", "QLD"]
}

# Store assignments
assignment = {}

# Constraint checker
def is_valid(region, color):
    for neighbor in adjacency[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm
def solve(index=0):

    if index == len(regions):
        return True

    region = regions[index]

    for color in colors:

        if is_valid(region, color):

            assignment[region] = color

            if solve(index + 1):
                return True

            del assignment[region]

    return False

# Solve CSP
if solve():

    print("Solution found:")

    for region, color in assignment.items():
        print(region, "->", color)

    # Create graph
    G = nx.Graph()

    for region in regions:
        G.add_node(region)

    for region, neighbors in adjacency.items():
        for neighbor in neighbors:
            G.add_edge(region, neighbor)

    # Convert assigned colors
    node_colors = [assignment[node].lower() for node in G.nodes()]

    # Draw graph
    plt.figure(figsize=(8,6))

    nx.draw(
        G,
        with_labels=True,
        node_color=node_colors,
        node_size=3000,
        font_size=14,
        font_weight='bold'
    )

    plt.title("Australia Map Coloring CSP")

    # Save image
    plt.savefig("australia_csp_coloring.png")

    # Show graph
    plt.show()

else:
    print("No solution found")