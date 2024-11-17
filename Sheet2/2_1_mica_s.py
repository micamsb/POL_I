#!/usr/local/bin/python3 --no-rcs

# Exercise 2.1
# Logistic growth

# Solution of the logistic equation:
    # n(t) = N * (exp(t / τ)) / ((N / n0) - 1 + exp(t / τ))

# Verify by explicit differentiation that this is a solution of the equation:
    # dn(t) / dt = (n(t) / τ) * (1 - n(t) / N)
    # with initial condition n(0) = n0

    # Differentiate n(t) with respect to t
    # n'(t) = d / dt * [N * (exp(t / τ)) / ((N / n0) - 1 + exp(t / τ))]         | D = (N / n0) - 1 + exp(t / τ)
    # n(t) = N * exp(t / τ) / D
    # n'(t) = N * (1/τ exp(t/τ) D - exp(t/τ) dD/dt) / D^2
    # D = N/n0 - 1 + exp(t/τ)
    # dD / dt = 1/τ exp(t/τ)
    # n'(t) = N * (1/τ exp(t/τ) D - exp(t/τ) (1/τ exp(t/τ))) / D^2
    # n'(t) = (N/τ exp(t/τ) (D - exp(t/τ)) / D^2                                | D = (N / n0) - 1 + exp(t / τ)
    # n'(t) = n(t)/τ (1 - n(t)/N)

# Verify by explicit differentiation that this is a solution of the equation (t1/2 = time at which n(t1/2) = N/2):
    # n(t) = [N exp((t-t1/2)/τ)] / [1 + exp((t-t1/2)/τ)]                        | E = exp((t-t1/2)/τ)
    # n(t) = NE / (1 + E)

    # n'(t) = [N (1/τ E(1 + E) - E * 1/τ * E)] / (1 + E)^2
    # n'(t) = [N/τ E (1 + E - E)] / (1 + E)^2
    # n'(t) = (N/τ E) / (1 + E)^2                                               | n(t) = NE / (1 + E)
    # n'(t) = n(t)/τ * (1 - n(t)/N)

# To every choice of t1/2 corresponds exactoly one choice of n0. Show how th etwo are related! In other words, express n0 as a funnction of t1/2 and t1/2 as a function no n0.
    # N/2 = [N * exp(t1/2 / τ)] / [(N / n0) - 1 + exp(t1/2 / τ)]
    # 1/2 = exp(t1/2 / τ) / [(N / n0) - 1 + exp(t1/2 / τ)]
    # N/n0 - 1 + exp(t1/2 / τ) = 2exp(t1/2 / τ)
    # N/n0 - 1 = exp(t1/2 / τ)
    # exp(t1/2 / τ) = N/n0 - 1                                                  | ln()
    # t1/2 = τln(N/n0 - 1)
    # N/n0 = 1 + exp(t1/2 / τ)
    # n0 = N / 1 + exp(t1/2 / τ)

    # t1/2 = τln(N/n0 - 1)
    # n0 = N / 1 + exp(t1/2 / τ)
