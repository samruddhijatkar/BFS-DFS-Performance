from collections import deque
import timeit

# 18-node graph
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


# BFS
def bfs(start, goal):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return len(visited)

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)


# DFS
def dfs(start, goal):
    stack = ['A']
    visited = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return len(visited)

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)


# Number of timing repetitions
RUNS = 100000

# Measure BFS
bfs_time = timeit.timeit(
    lambda: bfs('A', 'R'),
    number=RUNS
)

# Measure DFS
dfs_time = timeit.timeit(
    lambda: dfs('A', 'R'),
    number=RUNS
)

# Calculate average time
bfs_average = (bfs_time * 1000) / RUNS
dfs_average = (dfs_time * 1000) / RUNS


# Display results
print("====================================")
print("       TIMEIT BENCHMARK")
print("====================================")

print("Number of Nodes : 18")
print("Number of Runs  :", RUNS)

print("\nBFS Results")
print("BFS Total Time   :", bfs_time * 1000, "ms")
print("BFS Average Time :", bfs_average, "ms")

print("\nDFS Results")
print("DFS Total Time   :", dfs_time * 1000, "ms")
print("DFS Average Time :", dfs_average, "ms")