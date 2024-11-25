#!/usr/local/bin/python3 --no-rcs

# Exercise 3.1
# Cooperativity and Hill-functions

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
n = sp.symbols('n', positive=True, real=True)
k = sp.symbols('k', positive=True, real=True)
x = sp.symbols('x', positive=True, real=True)
alpha = sp.symbols('alpha', positive=True, real=True)

# Cooperative binding of transcription factors is usually parameterized using the Hill-functions of the form 
f = alpha * x**n / (k**n + x**n)

# At what value of x is f(x) at 50% of its maximal value? What is the maximal value of f(x) and for what values of x is it attained?
    # The maximal value is at α -> ∞ and f(x) -> α when x is a lot larger than k (x >>> k).
    # At 50% of its maximal value f(x) = α/2 which is when x = k, independent of n.
f_halve = alpha / 2
x_halve = sp.solve(f - f_halve, x)
f_max = sp.limit(f, x, sp.oo)

# Compute the deivative of f(x) and evaluate it for x = k.
f_prime = sp.diff(f, x)
print("f'(x) =", f_prime)
f_prime_at_k = f_prime.subs(x, k)
print("For x = k: f'(x) =", f_prime_at_k)

# Compute the width of the region along the x-axis where f(x) increases from (i) 1/3 to (ii) 2/3 of its maximal value.
    # (i) For f(x) = α/3
f_third = alpha / 3
x1 = sp.solve(f - f_third, x)
    # (ii) For f(x) = 2α/3
f_two_third = 2 * alpha / 3
x2 = sp.solve(f - f_two_third, x)

if x1 and x2:
    x1 = x1[0]
    x2 = x2[0]
    width = x2 - x1
else:
    raise ValueError("Solutions for x1 or x2 could not be determined.")
n_values = np.linspace(1, 10, 100)
width_values = []
inverse_derivative_values = []
for n_val in n_values:
    try:
        width_n = width.subs({alpha: 1, k: 1, n: n_val}).evalf()
        f_prime_inv_n = 1 / f_prime_at_k.subs({alpha: 1, k: 1, n: n_val}).evalf()
        width_values.append(width_n)
        inverse_derivative_values.append(f_prime_inv_n)
    except Exception as e:
        width_values.append(None)
        inverse_derivative_values.append(None)
        print(f"Error at n={n_val}: {e}")
#print("Width of region along x-axis where f(x) increases from 1/3 to 2/3 of its maximal value:", width_values)
#print("Inverse of the derivative of f(x) at x = k as a function of n:", inverse_derivative_values)

# Graph this width and the inverse of the derivative of f(x) at x = k as a function of n.
plt.figure(figsize=(10, 6))
plt.plot(n_values, width_values, label="Width (1/3 to 2/3 max)")
plt.plot(n_values, inverse_derivative_values, label="Inverse of f'(x) at x = k")
plt.xlabel("Hill coefficient (n)")
plt.ylabel("Value")
plt.title("Width and Inverse Derivative vs Hill Coefficient")
plt.legend()
plt.grid()
plt.show()

x_halve, f_max, f_prime_at_k
