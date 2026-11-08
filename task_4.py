
import heapq
import uuid

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color
        self.left: Node | None = None
        self.right: Node | None = None
        self.id = str(uuid.uuid4())


def build_heap_tree(heap, index=0):
    """Будує бінарне дерево зі списку купи."""
    if index >= len(heap):
        return None

    node = Node(heap[index])

    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)

    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    graph.add_node(node.id, color=node.color, label=node.val)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        left_x = x - 1 / 2 ** layer
        pos[node.left.id] = (left_x, y - 1)
        add_edges(graph, node.left, pos, left_x, y - 1, layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        right_x = x + 1 / 2 ** layer
        pos[node.right.id] = (right_x, y - 1)
        add_edges(graph, node.right, pos, right_x, y - 1, layer + 1)

    return graph


def draw_tree(root):
    if root is None:
        return

    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)

    colors = [data["color"] for _, data in graph.nodes(data=True)]
    labels = {node: data["label"] for node, data in graph.nodes(data=True)}

    plt.figure(figsize=(9, 6))
    nx.draw(
        nx.Graph(graph), pos, labels=labels,
        node_color=colors, node_size=2500
    )
    plt.title("Бінарна мін-купа")
    plt.show()


if __name__ == "__main__":
    heap_list = [1, 3, 5, 7, 9, 2]

    heapq.heapify(heap_list)
    print("Купа:", heap_list)

    root = build_heap_tree(heap_list)
    draw_tree(root)
