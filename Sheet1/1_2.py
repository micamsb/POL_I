#!/usr/local/bin/python3 --no-rcs

# Exercise 1.2
# Curve fitting

# Load the data mRNA.csv and fit the function f(t) = a(1 - exp(-bt)).

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = pd.read_csv('mRNA.csv')
y = data['mRNA']
t = data['time']

def fit_func(t, a, b):
    return a * (1 - np.exp(-b * t))

params, covariance = curve_fit(fit_func, t, y)

a, b = params
print("Fitted parameters:")
print(f"a = {a}")
print(f"b = {b}")

t_fit = np.linspace(t.min(), t.max(), 500)
y_fit = fit_func(t_fit, a, b)

plt.figure(figsize=(10, 6))
plt.scatter(t, y, color='blue', label='Data', s=10)
plt.plot(t_fit, y_fit, color='red', linestyle='--', label=f'Fit: $a(1 - exp{{-bt}})$/n$a={a:.4f}$, $b={b:.4f}$')
plt.xlabel('Time')
plt.ylabel('mRNA Concentration')
plt.legend()
plt.grid(True)
plt.show()

# a corresponds to the product ατ (steady state nRNA concentration)         a = ατ
# b represents 1/τ (decay rate)                                             b = 1/τ
# mRNA production rate α can be calculated as α = a * b
# mRNA lifetime τ can be calculated as τ = 1/b
