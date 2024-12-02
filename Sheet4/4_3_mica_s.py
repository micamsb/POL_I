#!/usr/local/bin/python3 --no-rcs

# Exercise 4.3
# Random walks

x = 0               # Startponit for the random walk in one dimension
pr = 0.57           # Probability of moving right
pl = 1 - pr         # Probability of moving left
n = [50, 300]       # Steps

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_random_walk(n, pr, trials=100):
    positions = np.zeros(trials)
    for i in range(trials):
        steps = np.random.choice([-1, 1], size=n, p=[pl, pr])    # -1 = left, 1 = right
        positions[i] = np.sum(steps)
    mean_position = np.mean(positions)
    variance_position = np.var(positions)
    fraction_right = np.sum(positions > 0) / trials
    return mean_position, variance_position, fraction_right, positions

results = {}
for ni in n:
    mean, var, fraction_right, positions = simulate_random_walk(ni, pr)
    sd = np.sqrt(var)
    z_score = (ni / 2 - ni * pr) / sd
    analytical_fraction = 1 - norm.cdf(z_score)
    results[ni] = {
        "mean": mean,
        "variance": var,
        "std": sd,
        "fraction_right_sim": fraction_right,
        "fraction_right_analytical": analytical_fraction,
        "positions": positions,
    }

fig, axs = plt.subplots(1, 2, figsize=(12, 5))
for i, ni in enumerate(n):
    data = results[ni]
    axs[i].hist(data["positions"], bins=30, density=True, alpha=0.6, label="Simulated")

    # Theoretical
    x_vals = np.linspace(-ni, ni, 500)
    theoretical = norm.pdf(x_vals, loc=ni * (2 * pr - 1), scale=data["std"])
    axs[i].plot(x_vals, theoretical, 'r--', label="Theoretical")

    axs[i].set_title(f"Histogram for n=[n]")
    axs[i].set_xlabel("Position")
    axs[i].set_ylabel("Density")
    axs[i].legend()
    axs[i].grid()

plt.tight_layout()
plt.show()


# How often has the walker moved to the right on average?
print("The walker moved on average", results[50]['fraction_right_sim'], "to the right when taking 50 steps.")

# How often has the walker moved to the right on average after 300 steps?
print("The walker moved on average", results[300]['fraction_right_sim'], "to the right when taking 300 steps.")
