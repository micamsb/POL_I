#!/usr/local/bin/python3 --no-rcs

# Exercise 4.1
# Stochastic protein production

# α = Protein production rate
# β = Molecule degradation rate
# α∆t = Probability that one protein is produced
# β∆t = Probability that one protein is degraded
# nβ∆t = Probability that any of the n proteins is degraded (if ∆t is small enough)
beta = 1            # Assumption

import numpy as np
import matplotlib.pyplot as plt

# Simulate and plot a trajectory of the number of proteins as a function of time until t = 120 using α = 7.5 and a step size ∆t = 0.001.
t = 120
alpha = 7.5
dt = 0.001          # Step size ∆t

def simulate_protein_dynamics(alpha, t, dt, beta):
    time_steps = int(t / dt)
    times = np.linspace(0, t, time_steps)
    n_proteins = np.zeros(time_steps)
    for time in range(1, time_steps):
        p_production = alpha * dt
        p_degradation = n_proteins[time-1] * beta * dt
        if np.random.rand() < p_production:
            n_proteins[time] = n_proteins[time-1] + 1
        elif np.random.rand() < p_degradation:
            n_proteins[time] = n_proteins[time-1] -1
        else:
            n_proteins[time] = n_proteins[time-1]
    return times, n_proteins

times, n_proteins = simulate_protein_dynamics(alpha, t, dt, beta)
plt.figure(figsize=(10,6))
plt.plot(times, n_proteins, label=f'a = {alpha}')
plt.xlabel('Time')
plt.ylabel('Number of Proteins')
plt.title('Protein Dynamics Trajectory')
plt.legend()
plt.grid()
plt.show()

# Calculate the mean number of proteins and its standard deviation for α = [.5, 1.8, 5, 24, 120]. 
# Plot both of these quantities as a function of the production rate α and compare the measured value with the theoretical expectation for the average number of proteins.
α = np.array([.5, 1.8, 5, 24, 120])
means = []
sd = []
t_mean = []             # Theoretical mean
t_sd = []               # Theoretical standard deviation

for a in α:
    _, n_proteins_sample = simulate_protein_dynamics(a, t, dt, beta)
    mean = np.mean(n_proteins_sample)
    std = np.std(n_proteins_sample)
    means.append(mean)
    sd.append(std)
    t_mean.append(a / beta)
    t_sd.append(np.sqrt(a / beta))

plt.figure(figsize=(12, 6))

# mean
plt.subplot(1, 2, 1)
plt.plot(α, means, 'o-', label='Simulated Mean')
plt.plot(α, t_mean, 'x--', label='Theoretical Mean')
plt.xlabel('Production Rate (α)')
plt.ylabel('Mean Protein Number')
plt.title('Mean Protein Number vs α')
plt.legend()
plt.grid()

# sd
plt.subplot(1, 2, 2)
plt.plot(α, sd, 'o-', label='Simulated Standard Deviation')
plt.plot(α, t_sd, 'x--', label='Theoretical Standard Deviation')
plt.xlabel('Production Rate (α)')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviation vs α')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# Compare the histogram of observed molecule number with a Poisson distribution.
from scipy.stats import poisson

_, n_protein_hist = simulate_protein_dynamics(alpha, t, dt, beta)
mean_hist = np.mean(n_protein_hist)
poisson_dist = poisson.pmf(np.arange(0, int(mean_hist) * 3), mu=mean_hist)

plt.figure(figsize=(10, 6))
plt.hist(n_protein_hist, bins=30, density=True, alpha=0.6, label='Simulated Data')
plt.plot(np.arange(0, int(mean_hist) * 3), poisson_dist, 'r--', label='Poisson Distribution')
plt.xlabel('Number of Proteins')
plt.ylabel('Probability')
plt.title('Histogram vs Poisson Distribution (α = 7.5)')
plt.legend()
plt.grid()
plt.show()
