# BFS vs DFS Performance Analysis

## SLE-2: Empirical Performance Profiling

### Course

02AML204 – Introduction to Artificial Intelligence

### Student Details

* **Name:** Samruddhi Sharad Jatkar
* **PRN:** 25UAM104
* **Division:** SY B

---

## Objective

The objective of this project is to compare the practical performance of **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** on the same graph.

The comparison is based on:

* Nodes expanded
* Total execution time
* Average execution time
* Function calls and profiling information

---

## Algorithms Used

### 1. Breadth-First Search (BFS)

BFS explores the graph level by level. It uses a queue to store nodes that need to be explored.

### 2. Depth-First Search (DFS)

DFS explores one branch as deeply as possible before backtracking. It uses a stack-based approach.

---

## Problem Used

An 18-node graph was used for both BFS and DFS.

* **Starting node:** A
* **Goal node:** R
* **Number of graph nodes:** 18

Both algorithms were tested on exactly the same graph so that their performance could be compared fairly.

---

## Profiling Method

The following Python tools were used:

* `time.perf_counter()` for runtime measurement
* `timeit` for repeated performance measurement
* `cProfile` for function-call and execution profiling

Each algorithm was executed **100,000 times** to obtain measurable timing results.

---

## Experimental Results

| Metric                |         BFS |         DFS |
| --------------------- | ----------: | ----------: |
| Graph nodes           |          18 |          18 |
| Number of runs        |     100,000 |     100,000 |
| Nodes expanded        |          18 |          10 |
| Total time (`timeit`) | 221.6429 ms | 161.5130 ms |
| Average time per run  | 0.002216 ms | 0.001615 ms |
| cProfile total time   |     1.338 s |     0.853 s |
| Function calls        |   5,500,001 |   3,300,001 |

---

## Analysis

For the selected graph and starting/goal nodes, DFS expanded fewer nodes than BFS.

* BFS expanded **18 nodes**.
* DFS expanded **10 nodes**.
* The measured total execution time of DFS was lower than BFS in this experiment.
* The cProfile results also showed fewer function calls for DFS.

This result is specific to the selected graph, implementation, Python environment, and computer. It does not mean that DFS is always faster than BFS.

The experiment demonstrates that empirical profiling can show how algorithm behaviour changes depending on the input and implementation.

---

## AI Contribution

AI assistance was used to:

* Understand the concepts of BFS and DFS.
* Design and modify the test graph.
* Understand Python performance-measurement techniques.
* Prepare the structure of the profiling experiment.
* Interpret the measured results.

The final code was executed and tested by the student, and the performance results were obtained from the student's own runs.

---

## Conclusion

The experiment successfully compared BFS and DFS using the same 18-node graph.

For this particular test case, DFS expanded fewer nodes and required less measured execution time than BFS. The experiment shows the importance of empirical performance profiling in addition to theoretical time-complexity analysis.

---

## Project Files

* `bfs_dfs.py` – BFS and DFS implementation with runtime measurement
* `benchmark.py` – Repeated timing using `timeit`
* `profile_search.py` – Profiling using `cProfile`
* `README.md` – Project documentation
* `.gitignore` – Git ignored files

## GitHub Repository

BFS-DFS-Performance
