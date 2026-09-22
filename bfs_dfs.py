from collections import deque
import time

# -----------------------------
# 18-NODE GRAPH
# -----------------------------
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F', 'G'],
    'C': ['H', 'I', 'J'],
    'D': ['K', 'L', 'M'],
    'E': ['N', 'O'],
    'F': ['P', 'Q'],
    'G': ['R'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
    'P': [],
    'Q': [],
    'R': []
}


# -----------------------------
# BFS
# -----------------------------
def bfs(start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


# -----------------------------
# DFS
# -----------------------------
def dfs(start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


# -----------------------------
# PERFORMANCE TEST
# -----------------------------

start_node = 'A'
goal_node = 'R'

# Repeat the same search many times
# This gives a measurable runtime
RUNS = 100000


# ---------- BFS ----------
bfs_start_time = time.perf_counter()

for i in range(RUNS):
    bfs_nodes = bfs(start_node, goal_node)

bfs_end_time = time.perf_counter()

bfs_total_time = (bfs_end_time - bfs_start_time) * 1000
bfs_average_time = bfs_total_time / RUNS


# ---------- DFS ----------
dfs_start_time = time.perf_counter()

for i in range(RUNS):
    dfs_nodes = dfs(start_node, goal_node)

dfs_end_time = time.perf_counter()

dfs_total_time = (dfs_end_time - dfs_start_time) * 1000
dfs_average_time = dfs_total_time / RUNS


# -----------------------------
# OUTPUT
# -----------------------------

print("====================================")
print("       BFS PERFORMANCE")
print("====================================")
print("Number of Nodes in Graph : 18")
print("Number of Runs           :", RUNS)
print("BFS Nodes Expanded       :", bfs_nodes)
print("BFS Total Runtime        :", bfs_total_time, "ms")
print("BFS Average Runtime      :", bfs_average_time, "ms")


print("\n====================================")
print("       DFS PERFORMANCE")
print("====================================")
print("Number of Nodes in Graph : 18")
print("Number of Runs           :", RUNS)
print("DFS Nodes Expanded       :", dfs_nodes)
print("DFS Total Runtime        :", dfs_total_time, "ms")
print("DFS Average Runtime      :", dfs_average_time, "ms")