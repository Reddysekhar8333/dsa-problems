from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Graph represented as an adjacency list using a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Function for BFS
def bfs(graph, start,visit=[],queue=None):
    if queue is None:
        queue=[start]
    if not queue:
        return
    node=queue.pop(0)
    if node not in visit:
        visit.append(node)
        for nei in graph[node]:
            if nei not in visit:
                queue.append(nei)
    bfs(graph,start,visit,queue)
    return visit
# Function for DFS
def dfs(graph, start, visited=[]):
    if start not in visited:
        visited.append(start)
        if start not in graph:
            return visited
        for i in graph[start]:
            visited=dfs(graph,i,visited)
    return visited

# Perform BFS and DFS
start_node = 'A'
bfs_result = bfs(graph, start_node)
dfs_result = dfs(graph, start_node)

# Print results
print(f"BFS Traversal from {start_node}: {bfs_result}")
print(f"DFS Traversal from {start_node}: {dfs_result}")

# Graph Visualization
G = nx.Graph(graph)

plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='red', node_size=2000, font_size=12)
plt.title("Graph Representation")
plt.show()
