import random

import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    """Симуляція кидків двох кубиків."""
    counts = {s: 0 for s in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        counts[die1 + die2] += 1

    probabilities = {s: counts[s] / num_rolls for s in counts}

    return probabilities


def theoretical_probability(total):
    """Точна ймовірність суми двох кубиків."""
    return (6 - abs(7 - total)) / 36


def plot_probabilities(probabilities):
    sums = list(range(2, 13))

    simulated = [probabilities[s] * 100 for s in sums]
    theoretical = [theoretical_probability(s) * 100 for s in sums]

    plt.figure(figsize=(10, 5))

    plt.bar([s - 0.2 for s in sums], simulated, width=0.4, label="Монте-Карло")
    plt.bar([s + 0.2 for s in sums], theoretical, width=0.4, label="Теоретична")

    plt.xticks(sums)
    plt.xlabel("Сума двох кубиків")
    plt.ylabel("Ймовірність (%)")
    plt.title("Порівняння ймовірностей")
    plt.legend()
    plt.grid(axis="y", alpha=0.3)
    plt.show()


if __name__ == "__main__":
    random.seed(42)
    num_rolls = 100_000

    probabilities = simulate_dice_rolls(num_rolls)

    print(f"Кількість кидків: {num_rolls}\n")
    print(f"{'Сума':>5} | {'Монте-Карло':>13} | {'Теоретична':>12}")
    print("-" * 38)

    for s, probability in probabilities.items():
        theoretical = theoretical_probability(s)

        print(f"{s:>5} | {probability * 100:>12.2f}% | {theoretical * 100:>11.2f}%")

    plot_probabilities(probabilities)
