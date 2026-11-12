"""Assessment 3.3 - Graph built from the last name CABAÑERO.

Vertices (the distinct letters, in order of first appearance):
    C, A, B, Ñ, E, R, O

Edges (undirected):
    C-A, C-O, A-B, A-Ñ, B-Ñ, Ñ-E, E-R, R-O

Neighbours are visited in the order the letters first appear in the name
(C, A, B, Ñ, E, R, O), so the traversal result is the same every run.
"""
from collections import deque

ORDER = ["C", "A", "B", "Ñ", "E", "R", "O"]
EDGES = [("C", "A"), ("C", "O"), ("A", "B"), ("A", "Ñ"),
         ("B", "Ñ"), ("Ñ", "E"), ("E", "R"), ("R", "O")]


def build_graph(vertices, edges):
    graph = {v: [] for v in vertices}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    for v in graph:  # fixed visiting order
        graph[v].sort(key=vertices.index)
    return graph


def bfs(graph, start):
    """Breadth-First Search: queue + visited set."""
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return order


def dfs(graph, start, visited=None, order=None):
    """Depth-First Search: go as deep as possible, then backtrack."""
    if visited is None:
        visited, order = set(), []
    visited.add(start)
    order.append(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited, order)
    return order


if __name__ == "__main__":
    g = build_graph(ORDER, EDGES)
    print("Adjacency list:")
    for v in ORDER:
        print(f"  {v}: {', '.join(g[v])}")
    print()
    print("BFS from C:", " - ".join(bfs(g, "C")))
    print("DFS from C:", " - ".join(dfs(g, "C")))