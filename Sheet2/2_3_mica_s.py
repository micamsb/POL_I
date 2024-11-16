#!/usr/local/bin/python3 --no-rcs

# Exercise 3.3
# Fixed points

# Differential equation x could describe the concentration of a protein
# dx / dt = α * (x / (1 + x)) - βx
# α and β are positive constants

# What is the role of the term α * x / (1 + x) and the interpretation of α?
    # The term represents the rate of production of the protein. It depends on the protein concentration (x) and the maximum production rate (α).

# What is the role of βx and the interpretation of β?
    # The term represents the degradation rate of the proetein (First-order decay).
    # β is the rate constant for degradation (Large β means faster decay).

# What are the fixed points of the system?
    # The fixed points of the system are the values of x where the rate of change = 0 (dx / dt = 0).
    # α * (x / (1 + x)) - βx = 0
    # x * ((α / (1 + x)) - β) = 0
    # Fixed points:
        # x1 = 0
            # α / (1 + x2) = β
            # α = β * (1 + x2)
        # x2 = (α / β) - 1

# How does the fixed point structure deped on the values of α and β?
    # x1 = 0 represents the absence of protein.
    # x2 = (α / β) - 1 only when α > β (α / β > 1) (must be positive).

# Discuss which fixed points are stable or unstable in different ranges of parameters.
    # x1 = 0 is only stable if α < β.
    # x2 = (α / β) - 1 stability depends on parameter values.