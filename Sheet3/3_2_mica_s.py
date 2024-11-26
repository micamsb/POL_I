#!/usr/local/bin/python3 --no-rcs

# Exercise 3.2
# Positive feed-back loops

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Analyze the behaviour of the following self-activating corcuit in which protein X accelerates its own transcription (x1 is the mRNA, x2 is the protein).
    # dx1/dt = α * (x2^n / (k^n + x2^n)) - β * x1
    # dx2/dt = γ * xy - δ * (x2 / (4 + x2))

# How do the null clines depend on the parameters α, β, γ, δ? 
    # Nullclines are the curves in phase space where dx1/dt = 0 and dx2/dt = 0
    # dx1/dt = 0
        # α * (x2^n / (k^n + x2^n)) = β * x1
        # x1 = α/β * (x2^n / (k^n + x2^n))
        # x1 scales with α/β
    # dx2/dt = 0
        # γx1 = δ * (x2 / (4 + x2))
        # x2 = δ/γ * (x2 / (4 + x2))
        # x2 scales with δ/γ

# Are particular ration of these parameters important?
    # The ratio δ/γ determines the slope & position of the x2 nullcline relative to the x1 nullcline. 
    # If δ/γ is too large or too small, the nullclines may not intersect, resulting in the loss of a non-trivial fixed point.

# Graph the null clines for different values of γ and δ using n = 4, k= 2.2, α= 4.9 and β= 3.2. 
alpha = 4.9
beta = 3.2
gamma_values = [1.0, 1.5, 2.0]
delta_values = [2.0, 4.0, 6.0]
n = 4
k = 2.2

def x1_nc(x2, alpha, beta, n, k):
    return (alpha / beta) * (x2**n / (k**n + x2**n))
def x2_nc(x2, gamma, delta):
    return (delta / gamma) * (x2 / (4 + x2))

x2_values = np.linspace(0, 10, 500)
plt.figure(figsize=(10, 6))
for gamma in gamma_values:
    for delta in delta_values:
        plt.plot(x2_values, x1_nc(x2_values, alpha, beta, n, k), label=f"x1 nullcline (γ={gamma}, δ={delta})")
        plt.plot(x2_values, x2_nc(x2_values, gamma, delta), label=f"x2 nullcline (γ={gamma}, δ={delta})")
        plt.xlabel("Protein concentration (x2)")
        plt.ylabel("mRNA concentration (x1)")
        plt.title("Nullclines for different γ and δ")
        plt.legend()
        plt.grid()
        plt.show()

# At what ratio of δ/γ does the non-trivial fixed point disappear?
    # Starting a ratio of ~3 the nullclines fail to intersect.

# Solve numerically for the dynamics of the system with parameters γ= 1.5 and δ= 4.0. 
def system(t, state, alpha, beta, gamma, delta, n, k):
    x1, x2 = state
    dx1_dt = alpha * (x2**n / (k**n + x2**n)) - beta * x1
    dx2_dt = gamma * x1 - delta * (x2 / (4 + x2))
    return [dx1_dt, dx2_dt]

gamma = 1.5
delta = 4.0
t_span = (0, 50)
initial_conditions = [0, 0]  # Starting concentrations for x1 and x2
sol = solve_ivp(system, t_span, initial_conditions, args=(alpha, beta, gamma, delta, n, k), dense_output=True)

t_vals = np.linspace(0, 50, 500)
x1_vals, x2_vals = sol.sol(t_vals)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, x1_vals, label="mRNA (x1)")
plt.plot(t_vals, x2_vals, label="Protein (x2)")
plt.xlabel("Time")
plt.ylabel("Concentration")
plt.title("Dynamics of the system")
plt.legend()
plt.grid()
plt.show()

# What mRNA and protein concentrations are attained at the stable non-trivial fixed point?
x1_range = np.linspace(0, 5, 50)
x2_range = np.linspace(0, 5, 50)
x1_grid, x2_grid = np.meshgrid(x1_range, x2_range)
basin_map = np.zeros_like(x1_grid)

for i in range(x1_grid.shape[0]):
    for j in range(x2_grid.shape[1]):
        initial_conditions = [x1_grid[i, j], x2_grid[i, j]]
        sol = solve_ivp(system, t_span, initial_conditions, args=(alpha, beta, gamma, delta, n, k), dense_output=False)
        final_x1, final_x2 = sol.y[:, -1]
        if final_x1 < 0.1 and final_x2 < 0.1:  # Trivial fixed point
            basin_map[i, j] = 0
        else:  # Non-trivial fixed point
            basin_map[i, j] = 1

plt.figure(figsize=(10, 6))
plt.contourf(x1_range, x2_range, basin_map, levels=1, cmap="coolwarm")
plt.xlabel("Initial mRNA (x1)")
plt.ylabel("Initial Protein (x2)")
plt.title("Basins of Attraction")
plt.colorbar(label="Attraction (0: Trivial, 1: Non-Trivial)")
plt.grid()
plt.show()

