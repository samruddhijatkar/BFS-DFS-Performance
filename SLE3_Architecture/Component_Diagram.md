# Component Diagram

This diagram expands the BFS/DFS Search Engine container.

## Components

### 1. Search Entry
Starts the selected search algorithm.

### 2. Frontier Manager
Manages the nodes waiting to be explored.

- BFS → Queue
- DFS → Stack

### 3. Visited Checker
Checks whether a node has already been visited.

### 4. Goal Test
Checks whether the current node is the goal node.

### 5. Parent/Path Builder
Stores parent relationships and reconstructs the final path.

## Component Flow

Search Entry
↓
Frontier Manager
↓
Visited Checker
↓
Goal Test
↓
Parent/Path Builder
↓
Final Path