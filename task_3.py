
import heapq

import matplotlib.pyplot as plt
import networkx as nx


def dijkstra(graph, start):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0

    # Черга з пріоритетом: (відстань, вершина)
    queue = [(0, start)]

    while queue:
        current_distance, vertex = heapq.heappop(queue)

        if current_distance > distances[vertex]:
            continue

        for neighbor in graph.neighbors(vertex):
            weight = graph[vertex][neighbor]["weight"]
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    return distances


if __name__ == "__main__":
    # Створюємо зважений граф
    G = nx.Graph()

    G.add_weighted_edges_from([
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
        ("D", "F", 6),
        ("E", "F", 3)
    ])

    distances = dijkstra(G, "A")

    print("Найкоротші відстані від вершини A:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")

    # Візуалізація графа
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos, with_labels=True,
        node_color="skyblue", node_size=1000
    )

    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Зважений граф")
    plt.show()
