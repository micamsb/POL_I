#!/usr/local/bin/python3 --no-rcs

# Exercise 3.2
# Posotive feed-back loops

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

# Graph the null clines for different values of γand δusing n = 4, k= 2.2, α= 4.9 and β= 3.2. 
    # 
# At what ratio of δ/γ does the non-trivial fixed point disappear?
    #

# Solve numerically for the dynamics of the system with parameters γ= 1.5 and δ= 4.0. 
    # 
# What mRNA and protein concentrations are attained at the stable non-trivial fixed point?
    #


