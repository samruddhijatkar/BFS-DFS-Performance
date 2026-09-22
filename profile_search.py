import cProfile
import pstats
from collections import deque


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


# Profile BFS
print("========== BFS PROFILE ==========")

bfs_profiler = cProfile.Profile()
bfs_profiler.enable()

for i in range(100000):
    bfs('A', 'R')

bfs_profiler.disable()

bfs_stats = pstats.Stats(bfs_profiler)
bfs_stats.sort_stats('cumulative')
bfs_stats.print_stats(10)


# Profile DFS
print("\n========== DFS PROFILE ==========")

dfs_profiler = cProfile.Profile()
dfs_profiler.enable()

for i in range(100000):
    dfs('A', 'R')

dfs_profiler.disable()

dfs_stats = pstats.Stats(dfs_profiler)
dfs_stats.sort_stats('cumulative')
dfs_stats.print_stats(10)