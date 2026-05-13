from collections import deque

# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS function
def bfs(graph, start, goal):

    visited = set()

    queue = deque([[start]])

    while queue:

        path = queue.popleft()

        node = path[-1]

        # Goal test
        if node == goal:
            return path

        if node not in visited:

            visited.add(node)

            # Expand neighbors
            for neighbor in graph[node]:

                new_path = list(path)

                new_path.append(neighbor)

                queue.append(new_path)

    return None

# Initial node and goal node
start_node = 'A'
goal_node = 'F'

# Run BFS
path = bfs(graph, start_node, goal_node)

# Output
print("BFS Search Path:")

print(" -> ".join(path))