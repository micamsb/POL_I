#!/usr/local/bin/python3 --no-rcs

# Exercise 2.2
# Bacterial growth curves

# Load the data (growth_data.csv) and plot the time course of OD of each experiment (WT_1, WT_2, WT_3) both on a lonear and a logarithmic y-axis. Discuss the features of these curves.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

d = pd.read_csv('growth_data.csv')
# i = data['index']
t = d['t']  # time
wt_1 = d['WT_1']
wt_2 = d['WT_2']
wt_3 = d['WT_3']

def linear_fit(t, a, b):
    return a + b * t

# Time range
tr = t[t <= 32]
# Logarithms
l_wt1 = np.log(wt_1[t <= 32])
l_wt2 = np.log(wt_2[t <= 32])
l_wt3 = np.log(wt_3[t <= 32])

# Parameters
p_wt1, _ = curve_fit(linear_fit, tr, l_wt1)
p_wt2, _ = curve_fit(linear_fit, tr, l_wt2)
p_wt3, _ = curve_fit(linear_fit, tr, l_wt3)

# Growth rates
gr_wt1 = p_wt1[1]
gr_wt2 = p_wt2[1]
gr_wt3 = p_wt3[1]

# Exponential
e_wt1 = np.exp(linear_fit(t, *p_wt1))
e_wt2 = np.exp(linear_fit(t, *p_wt2))
e_wt3 = np.exp(linear_fit(t, *p_wt3))

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, wt_1, 'red', '--', label="WT_1 (data)")
plt.plot(t, wt_2, 'green', '--', label="WT_2 (data)")
plt.plot(t, wt_3, 'blue', '--', label="WT_3 (data)")
plt.plot(t, e_wt1, 'red', '--', label="WT_1 (fit)")
plt.plot(t, e_wt2, 'green', '--', label="WT_2 (fit)")
plt.plot(t, e_wt3, 'blue', '--', label="WT_3 (fit)")
plt.xlabel("Time")
plt.ylabel("OD")
plt.title("Bacterial Growth (linear)")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, wt_1, 'red', '--', label="WT_1 (data)")
plt.plot(t, wt_2, 'green', '--', label="WT_2 (data)")
plt.plot(t, wt_3, 'blue', '--', label="WT_3 (data)")
plt.plot(t, e_wt1, 'red', '--', label="WT_1 (fit)")
plt.plot(t, e_wt2, 'green', '--', label="WT_2 (fit)")
plt.plot(t, e_wt3, 'blue', '--', label="WT_3 (fit)")
plt.yscale('log')
plt.xlabel("Time")
plt.ylabel("OD")
plt.title("Bacterial Growth (logarithmic)")
plt.grid(True)
plt.legend()

plt.show()

# Growth rates (~slope)
print("Growth rate for wt1:", gr_wt1)
print("Growth rate for wt2:", gr_wt2)
print("Growth rate for wt3:", gr_wt3)
