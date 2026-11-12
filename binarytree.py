"""Assessment 3.3 - Binary Tree built from the last name CABAÑERO.

The letters are inserted level by level (left to right), the same way the
lecture example places A..G:

Level 0:                C
Level 1:         A             B
Level 2:      A     Ñ       E     R
Level 3:    O
"""
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_level_order(letters):
    """Build a complete binary tree by inserting letters level by level."""
    if not letters:
        return None
    root = Node(letters[0])
    queue = deque([root])
    i = 1
    while i < len(letters):
        parent = queue.popleft()
        parent.left = Node(letters[i])
        queue.append(parent.left)
        i += 1
        if i < len(letters):
            parent.right = Node(letters[i])
            queue.append(parent.right)
            i += 1
    return root


def bfs(root):
    """Breadth-First Search: visit level by level using a queue."""
    order = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def dfs(node, order=None):
    """Depth-First Search (preorder): Node, Left, Right using recursion."""
    if order is None:
        order = []
    if node is None:
        return order
    order.append(node.value)
    dfs(node.left, order)
    dfs(node.right, order)
    return order


def print_tree(node, prefix="", is_left=True):
    """Print the tree sideways so the diagram can be seen in the console."""
    if node is None:
        return
    print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + node.value)
    print_tree(node.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    last_name = "CABAÑERO"
    root = build_level_order(list(last_name))

    print("Binary tree (rotated 90 degrees, root at the left):")
    print_tree(root)
    print()
    print("BFS:", " - ".join(bfs(root)))
    print("DFS:", " - ".join(dfs(root)))