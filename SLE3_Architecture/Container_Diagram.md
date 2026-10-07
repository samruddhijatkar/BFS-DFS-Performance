# Container Diagram

The system is divided into the following main containers.

## 1. Input Module

Accepts:
- Graph
- Start node
- Goal node
- Algorithm selection

## 2. Search Controller

Controls the execution of the selected search algorithm.

## 3. BFS/DFS Search Engine

Performs:
- BFS using FIFO queue
- DFS using LIFO stack

## 4. Visited & Parent Store

Maintains:
- Visited nodes
- Parent relationships

## 5. Output & Profiler

Produces:
- Search path
- Nodes expanded
- Runtime

## Container Flow

Input Module
↓
Search Controller
↓
BFS/DFS Search Engine
↓
Visited & Parent Store
↓
Output & Profiler