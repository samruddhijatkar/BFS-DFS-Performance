import cProfile
import pstats
from collections import deque

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

def build_flamegraph_svg(title, root_name, func_name, total_time, self_time, calls, width=1200, row_height=24):
    """Generates an SVG flamegraph identical in style to py-spy."""
    height = 200
    svg = f'''<svg version="1.1" width="{width}" height="{height}" 
     xmlns="http://www.w3.org/2000/svg" 
     style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 12px; background: #2d3139;">
  <style>
    .func-rect {{ rx: 2px; stroke: #1e1e1e; stroke-width: 0.5px; }}
    .func-rect:hover {{ opacity: 0.85; cursor: pointer; }}
    .func-text {{ fill: #ffffff; font-weight: 500; pointer-events: none; }}
    .title {{ fill: #e0e0e0; font-size: 15px; font-weight: bold; }}
  </style>

  <!-- Title -->
  <text class="title" x="20" y="30">{title}</text>

  <!-- Level 0: Main module -->
  <g>
    <rect class="func-rect" x="20" y="50" width="{width - 40}" height="{row_height}" fill="#b8860b"/>
    <text class="func-text" x="25" y="{50 + 16}">&lt;module&gt; (profile_search.py) [{total_time:.4f}s total]</text>
  </g>

  <!-- Level 1: Runner function -->
  <g>
    <rect class="func-rect" x="20" y="{50 + row_height + 4}" width="{width - 40}" height="{row_height}" fill="#d9534f"/>
    <text class="func-text" x="25" y="{50 + row_height + 4 + 16}">{root_name} (profile_search.py) [100,000 iterations]</text>
  </g>

  <!-- Level 2: Search algorithm target execution -->
  <g>
    <rect class="func-rect" x="20" y="{50 + (row_height + 4) * 2}" width="{width - 40}" height="{row_height}" fill="#e67e22"/>
    <text class="func-text" x="25" y="{50 + (row_height + 4) * 2 + 16}">{func_name} (bfs_dfs.py) - {calls:,} calls, {total_time:.4f}s cumulative, {self_time:.4f}s self-time</text>
  </g>
</svg>'''
    return svg


if __name__ == '__main__':
    RUNS = 100000

    # 1. Profile BFS
    print("Profiling BFS (100,000 runs)...")
    bfs_profiler = cProfile.Profile()
    bfs_profiler.enable()
    for _ in range(RUNS):
        bfs('A', 'R')
    bfs_profiler.disable()

    bfs_stats = pstats.Stats(bfs_profiler)
    # Extract timings for BFS
    bfs_total_time = bfs_stats.total_tt
    for func, (cc, nc, tt, ct, callers) in bfs_stats.stats.items():
        if func[2] == 'bfs':
            bfs_svg = build_flamegraph_svg("Flame Graph: BFS Profile", "run_bfs", "bfs", ct, tt, nc)
            with open("bfs_profile.svg", "w", encoding="utf-8") as f:
                f.write(bfs_svg)
            print("-> Successfully generated 'bfs_profile.svg'")
            break

    # 2. Profile DFS
    print("Profiling DFS (100,000 runs)...")
    dfs_profiler = cProfile.Profile()
    dfs_profiler.enable()
    for _ in range(RUNS):
        dfs('A', 'R')
    dfs_profiler.disable()

    dfs_stats = pstats.Stats(dfs_profiler)
    # Extract timings for DFS
    dfs_total_time = dfs_stats.total_tt
    for func, (cc, nc, tt, ct, callers) in dfs_stats.stats.items():
        if func[2] == 'dfs':
            dfs_svg = build_flamegraph_svg("Flame Graph: DFS Profile", "run_dfs", "dfs", ct, tt, nc)
            with open("dfs_profile.svg", "w", encoding="utf-8") as f:
                f.write(dfs_svg)
            print("-> Successfully generated 'dfs_profile.svg'")
            break