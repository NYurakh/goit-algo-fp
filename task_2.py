import math

import matplotlib.pyplot as plt


def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return

    # Кінець поточної гілки
    x_end = x + length * math.cos(math.radians(angle))
    y_end = y + length * math.sin(math.radians(angle))

    color = "saddlebrown" if depth > 3 else "forestgreen"

    plt.plot([x, x_end], [y, y_end], color=color, linewidth=max(1, depth / 2))

    # Рекурсивно малюємо дві нові гілки
    new_length = length / math.sqrt(2)

    draw_branch(x_end, y_end, new_length, angle + 45, depth - 1)
    draw_branch(x_end, y_end, new_length, angle - 45, depth - 1)


if __name__ == "__main__":
    depth = int(input("Введіть рівень рекурсії (1-12): "))

    if not 1 <= depth <= 12:
        raise ValueError("Рівень рекурсії має бути від 1 до 12")

    plt.figure(figsize=(8, 8))
    plt.title(f"Дерево Піфагора (рівень {depth})")

    draw_branch(0, 0, 1, 90, depth)

    plt.axis("equal")
    plt.axis("off")
    plt.show()
