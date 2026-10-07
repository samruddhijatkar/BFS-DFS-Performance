# Design Decisions

## 1. BFS and DFS

BFS and DFS were selected because they were already implemented and compared in SLE-2.

## 2. Same Graph

The same graph is used for both algorithms to make the performance comparison fair.

## 3. BFS Data Structure

BFS uses `collections.deque` because BFS requires FIFO processing.

## 4. DFS Data Structure

DFS uses a Python list as a stack because DFS requires LIFO processing.

## 5. Visited Set

A visited set is used to avoid processing the same node repeatedly.

## 6. Parent Dictionary

A parent dictionary is used to reconstruct the path from the goal node.

## 7. Performance Measurement

`time.perf_counter()` is used to measure runtime.

## 8. Node Counting

A node counter is used to measure the number of expanded nodes.

## SLE-2 Performance Evidence

| Measurement | BFS | DFS |
|---|---:|---:|
| Run 1 | 8.25 ms | 6.42 ms |
| Run 2 | 7.11 ms | 6.30 ms |
| Run 3 | 8.33 ms | 7.73 ms |
| Average | 7.90 ms | 6.82 ms |
| Nodes Expanded | 10 | 10 |

DFS was faster by 1.08 ms on average in the SLE-2 experiment.