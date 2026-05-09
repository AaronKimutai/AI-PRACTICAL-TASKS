import networkx as nx
import matplotlib.pyplot as plt

# Available colors
colors = ["Red", "Green", "Blue"]

# Nairobi sub-counties
subcounties = [
    "Westlands",
    "Dagoretti North",
    "Dagoretti South",
    "Langata",
    "Kibra",
    "Roysambu",
    "Kasarani",
    "Ruaraka",
    "Embakasi Central",
    "Embakasi East",
    "Embakasi West",
    "Embakasi South",
    "Makadara",
    "Kamukunji",
    "Starehe",
    "Mathare",
    "Njiru"
]

# Adjacency relationships
adjacency = {
    "Westlands": ["Dagoretti North", "Kibra"],
    "Dagoretti North": ["Westlands", "Dagoretti South", "Kibra"],
    "Dagoretti South": ["Dagoretti North", "Langata", "Kibra"],
    "Langata": ["Dagoretti South", "Kibra", "Embakasi South"],
    "Kibra": ["Westlands", "Dagoretti North", "Dagoretti South", "Langata"],
    "Roysambu": ["Kasarani", "Ruaraka"],
    "Kasarani": ["Roysambu", "Ruaraka", "Njiru"],
    "Ruaraka": ["Roysambu", "Kasarani", "Embakasi West"],
    "Embakasi Central": ["Embakasi East", "Embakasi West"],
    "Embakasi East": ["Embakasi Central", "Njiru"],
    "Embakasi West": ["Ruaraka", "Embakasi Central"],
    "Embakasi South": ["Langata"],
    "Makadara": ["Kamukunji", "Starehe"],
    "Kamukunji": ["Makadara", "Starehe"],
    "Starehe": ["Makadara", "Kamukunji", "Mathare"],
    "Mathare": ["Starehe"],
    "Njiru": ["Kasarani", "Embakasi East"]
}

# Store assignments
assignment = {}

# Check constraints
def is_valid(region, color):
    for neighbor in adjacency.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking CSP solver
def solve(index=0):

    if index == len(subcounties):
        return True

    region = subcounties[index]

    for color in colors:

        if is_valid(region, color):

            assignment[region] = color

            if solve(index + 1):
                return True

            del assignment[region]

    return False

# Solve CSP
if solve():

    print("Coloring Solution:\n")

    for region, color in assignment.items():
        print(region, "->", color)

    # Create graph
    G = nx.Graph()

    for region in subcounties:
        G.add_node(region)

    # Add edges
    for region, neighbors in adjacency.items():
        for neighbor in neighbors:
            G.add_edge(region, neighbor)

    # Assign node colors
    node_colors = [assignment[node].lower() for node in G.nodes()]

    # Create figure
    plt.figure(figsize=(16, 12))

    # Spread nodes farther apart
    pos = nx.spring_layout(G, seed=42, k=2.5)

    # Draw graph
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=5000,
        font_size=9,
        font_weight='bold',
        edge_color='black',
        width=1.5
    )

    # Title
    plt.title(
        "Nairobi Sub-Counties CSP Coloring",
        fontsize=16,
        fontweight='bold'
    )

    # Save image
    plt.savefig("nairobi_csp_coloring.png")

    # Show graph
    plt.show()

else:
    print("No valid coloring found")