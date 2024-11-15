#!/usr/local/bin/python3 --no-rcs

# Exercise 1.1
# mRNA production and degradation

# mRNA production rate = α
# mRNA lifetime = τ
# mRNA degradation rate = 1/τ

# Write down a differential equation that describes changes in the number of mRNA molecules. Call that number y.
    # dy/dt = α - y/τ

# Determine the fixed point of the system. The fixed point corresponds to the steady state of number of mRNA molecules.
    # Steady state when dy/dt = 0
    # 0 = α - y/τ                   | + y/τ
    # y/τ = α                       | * τ
    # y = α * τ
    # The number of mRNA molecules y will stabilize at y = ατ at seady state.
    # The production and degradation rate are balanced at this point.

# Give  the analytic solution for y(t) for the following initial conditions:
# (i) y(0) = 0
# (ii) y(0) = 2ατ                    (note that ατ has the same dimensions a y).
    # dy/dt + y/τ = α               | * e^(t/τ)
    # e^(t/τ) * dy/dt + e^(t/τ) * y/τ = e^(t/τ) * α
    # d/dt(ye^(t/τ)) = αe^(t/τ)     | ∫
    # ye^(t/τ) = ∫ αe^(t/τ) dt
    # ye^(t/τ) = ατe^(t/τ) + C      | : e^(t/τ)
    # y(t) = ατ + Ce^(-t/τ)

    # (i) y(0) = 0                  t = 0 ; y(0) = 0 
    # 0 = ατ + Ce^0 
    # 0 = ατ + C                    | - ατ
    # C = -ατ
    # y(t) = ατ - ατe^(-t/τ)
    # y(t) = ατ (1 - e^(-t/τ))

    # (ii) y(0) = 2ατ               t = 0 , y(0) = 2ατ
    # 2ατ = ατ + Ce^0
    # 2ατ = ατ + C
    # C = ατ
    # y(t) = ατ + ατe^(-t/τ)
    # y(t) = ατ(1 + e^(-t/τ))

# Graph or sketch the solutions for these two initial consitions. Indicate the asymptotic concentration at long times.
import numpy as np
import matplotlib.pyplot as plt

α = 1
τ = 5
t = np.linspace(0, 30, 300)

y1 = α * τ * (1 - np.exp(-t / τ))
y2 = α * τ * (1 + np.exp(-t / τ))

y_asymptote = α * τ

plt.figure(figsize=(10, 6))
plt.plot(t, y1, label=r"$y(0) = 0$", color='blue', linestyle='-', linewidth=2)
plt.plot(t, y2, label=r"$y(0) = 2ατ$", color='green', linestyle='--', linewidth=2)
plt.axhline(y_asymptote, color='red', linestyle=':', linewidth=1.5, label=r"Asymptote $y = ατ$")

plt.xlabel("Time (t)", fontsize=12)
plt.ylabel("mRNA Concentration (y)", fontsize=12)
plt.title("Solutions for mRNA concentration y(t) with different initial conditions", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.show()
