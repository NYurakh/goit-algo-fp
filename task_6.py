items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    """Вибір страв за співвідношенням калорій до ціни."""
    sorted_items = sorted(
        items.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )

    chosen = []
    total_cost = 0
    total_calories = 0

    for name, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            chosen.append(name)
            total_cost += details["cost"]
            total_calories += details["calories"]

    return total_calories, total_cost, chosen


def dynamic_programming(items, budget):
    """Оптимальний вибір страв методом 0/1 Knapsack."""
    names = list(items)
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]

        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]

            if cost <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost] + calories)

    # Відновлення обраних страв
    chosen = []
    remaining = budget

    for i in range(n, 0, -1):
        if dp[i][remaining] != dp[i - 1][remaining]:
            name = names[i - 1]
            chosen.append(name)
            remaining -= items[name]["cost"]

    chosen.reverse()

    return dp[n][budget], budget - remaining, chosen


if __name__ == "__main__":
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Бюджет:", budget)
    print("\nЖадібний алгоритм:")
    print("Калорії, вартість, страви:", greedy_result)

    print("\nДинамічне програмування:")
    print("Калорії, вартість, страви:", dp_result)
