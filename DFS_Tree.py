from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_level_order(letters):
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


def preorder(node, order=None):
    if order is None:
        order = []
    if node is None:
        return order
    order.append(node.value)
    preorder(node.left, order)
    preorder(node.right, order)
    return order


def inorder(node, order=None):
    if order is None:
        order = []
    if node is None:
        return order
    inorder(node.left, order)
    order.append(node.value)
    inorder(node.right, order)
    return order


def postorder(node, order=None):
    if order is None:
        order = []
    if node is None:
        return order
    postorder(node.left, order)
    postorder(node.right, order)
    order.append(node.value)
    return order


def dfs_iterative(root):
    if root is None:
        return []
    order, stack = [], [root]
    while stack:
        node = stack.pop()
        order.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


if __name__ == "__main__":
    last_name = "CABAÑERO"
    root = build_level_order(list(last_name))

    print(f"DFS methods in tree for: {last_name}\n")
    print("Preorder  (Node-Left-Right):", " - ".join(preorder(root)))
    print("Inorder   (Left-Node-Right):", " - ".join(inorder(root)))
    print("Postorder (Left-Right-Node):", " - ".join(postorder(root)))
    print("Iterative (stack, preorder):", " - ".join(dfs_iterative(root)))