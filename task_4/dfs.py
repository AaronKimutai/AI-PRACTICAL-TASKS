# Depth First Search implementation 
def dfs(graph, start, goal, path=None, visited=None):
    # Initialize path and visited set on first call
    if path is None:
        path = []
    if visited is None:
        visited = set()

    # Add current node to path and mark as visited
    path.append(start)
    visited.add(start)

    # If goal is found, return the path
    if start == goal:
        return path

    # Explore neighbors (go deeper first)
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path.copy(), visited.copy())
            if result is not None:
                return result

    # If no path found from this branch
    return None



# Example graph 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run DFS
start_node = 'A'
goal_node = 'F'

path = dfs(graph, start_node, goal_node)

# Output result
if path:
    print("DFS Path from", start_node, "to", goal_node, ":", " -> ".join(path))
else:
    print("No path found")