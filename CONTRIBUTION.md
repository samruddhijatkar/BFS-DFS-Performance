# Contribution Log

## Project

**BFS vs DFS Performance Analysis**

## Course

**02AML204 – Introduction to Artificial Intelligence**

## Student

**Samruddhi Sharad Jatkar**

## Division

**SY B**

---

## Contribution Summary

I contributed to the development and performance analysis of the BFS and DFS search algorithms.

### 1. BFS Implementation

* Implemented Breadth-First Search using Python.
* Used `deque` as a queue for BFS traversal.
* Used a `visited` set to avoid visiting the same node repeatedly.
* Tested BFS on the 18-node graph.
* Used node expansion counting to measure the search effort.

### 2. DFS Implementation

* Implemented Depth-First Search using Python.
* Used a list as a stack for DFS traversal.
* Used a `visited` set to avoid repeated nodes.
* Tested DFS on the same 18-node graph.
* Compared DFS with BFS using the same start and goal nodes.

### 3. Performance Measurement

* Used Python `time.perf_counter()` for runtime measurement.
* Used `timeit` for repeated performance testing.
* Executed the algorithms **100,000 times** to obtain measurable timing differences.
* Calculated total runtime and average runtime per execution.

### 4. Profiling

* Used Python `cProfile` and `pstats`.
* Generated profiling information for both BFS and DFS.
* Analyzed function calls, cumulative time, and self-time.
* Created:

  * `bfs_profile.svg`
  * `dfs_profile.svg`

### 5. Result Analysis

The measured experiment showed:

| Metric              |         BFS |         DFS |
| ------------------- | ----------: | ----------: |
| Nodes Expanded      |          18 |          10 |
| Total Runtime       | 221.6429 ms | 161.5130 ms |
| Average Runtime     | 0.002216 ms | 0.001615 ms |
| cProfile Total Time |     1.338 s |     0.853 s |
| Function Calls      |   5,500,001 |   3,300,001 |

For this particular graph and implementation, DFS expanded fewer nodes and had lower measured runtime.

### 6. GitHub Contribution

* Created and maintained the GitHub repository.
* Added Python source files.
* Added BFS and DFS profiling SVG files.
* Updated project documentation.
* Committed changes and pushed them to the GitHub repository.

---

## Tools and Technologies Used

* Python
* `collections.deque`
* `time`
* `timeit`
* `cProfile`
* `pstats`
* SVG
* Git
* GitHub
* VS Code

---

## AI Contribution

AI assistance was used to:

* Understand BFS and DFS concepts.
* Understand performance profiling methods.
* Understand how to use `timeit` and `cProfile`.
* Help structure the profiling code.
* Help interpret the measured results.
* Help generate the SVG profiling representation.
* Help troubleshoot Git and GitHub commands.

The final code was executed and tested by the student, and the measured results were used for the project analysis.

---

## Conclusion

The project provided practical experience in implementing BFS and DFS and comparing their empirical performance. The experiment demonstrated that measured performance can depend on the graph structure, number of nodes expanded, implementation details, and execution environment.
