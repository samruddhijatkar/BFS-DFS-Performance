# Code Level Overview

The following functions and data structures represent the main code-level elements of the BFS and DFS Search System.

## Main Functions

1. `bfs(graph, start, goal)`
2. `dfs(graph, start, goal)`
3. `reconstruct_path(parent, goal)`

## Main Data Structures

4. `visited = set()`
5. `parent = {}`

## Performance Measurement

6. `nodes_expanded += 1`
7. `time.perf_counter()`

## BFS Implementation

BFS uses a FIFO queue implemented using `collections.deque`.

## DFS Implementation

DFS uses a LIFO stack implemented using a Python list.

## Path Reconstruction

The parent dictionary stores the relationship between nodes and is used to reconstruct the final path.