import heapq
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx

from task_4 import add_edges, build_heap_tree


def dfs(root):
    """Обхід у глибину за допомогою стека."""
    stack = [root]
    order = []

    while stack:
        node = stack.pop()

        if node is None:
            continue

        order.append(node)
        stack.append(node.right)
        stack.append(node.left)

    return order


def bfs(root):
    """Обхід у ширину за допомогою черги."""
    queue = deque([root])
    order = []

    while queue:
        node = queue.popleft()

        if node is None:
            continue

        order.append(node)
        queue.append(node.left)
        queue.append(node.right)

    return order


def generate_color(step, total):
    """Градієнт від темно-синього до світло-блакитного."""
    ratio = step / max(total - 1, 1)

    r = int(40 + 190 * ratio)
    g = int(70 + 165 * ratio)
    b = int(110 + 145 * ratio)

    return f"#{r:02x}{g:02x}{b:02x}"


def visualize(root, order, title):
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)

    total = len(order)
    _fig, ax = plt.subplots(figsize=(9, 6))

    for step in range(total):
        ax.clear()

        visited = {
            node.id: generate_color(i, total)
            for i, node in enumerate(order[: step + 1])
        }

        numbers = {node.id: i + 1 for i, node in enumerate(order[: step + 1])}

        colors = [visited.get(node, "skyblue") for node in graph.nodes()]

        labels = {
            node: f"{data['label']}\n({numbers[node]})"
            if node in numbers
            else str(data["label"])
            for node, data in graph.nodes(data=True)
        }

        nx.draw_networkx(
            graph,
            pos,
            labels=labels,
            node_color=colors,
            node_size=2200,
            arrows=False,
            ax=ax,
        )

        ax.set_title(f"{title}: крок {step + 1}/{total}")
        plt.pause(0.4)

    plt.show()


if __name__ == "__main__":
    heap_list = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
    heapq.heapify(heap_list)

    root = build_heap_tree(heap_list)

    dfs_order = dfs(root)
    bfs_order = bfs(root)

    print("DFS:", [node.val for node in dfs_order])
    print("BFS:", [node.val for node in bfs_order])

    visualize(root, dfs_order, "DFS")
    visualize(root, bfs_order, "BFS")
