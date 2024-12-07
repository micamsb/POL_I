#!/usr/local/bin/python3 --no-rcs

# Exercise 5.1
# Fluorescence recovery after photobleaching

# Cell filled with a fluorescently tagged protein.
# At t = 0, you bleach (destroy) the fluorophore in a 2µm stripe and measure its recovery after 15, 30, 150, 300, 1000 milliseconds.

# Estimate the diffusion constant!

# Initial condition (ADAM):

# Make a rough guess of the diffusion constant by considering the time it takes to fill the void half-way and the width of the void. 

# Simulate the process for a few values of D in the vicinity of your guess and refine your guess. 
# This could be done by plotting the simulation and the data onto the same graph, possibly only for a subset of the time points.
# When you solve the diffusion problem numerically, use dx = 0.1 (same as the spacing of the data) and dt = 0.0002 (or smaller).

# What determines the final fluorescence level (the final concentration of fluorescent protein) after the profile is flat? Why is it less than initial intensity?

# EXTRA:
# -