#!/usr/local/bin/python3 --no-rcs

# Exercise 1.3
# The number of ribosomes

# (i) Translation rate of ribosome: 12 codons a second = R1                
# (ii) Translation rate of ribosome: 20 codons a second = R2
    # constant; each codon = one amino acid
# Protein equivalent of a bacterial cell : 10^9 amino acids = P
# Number of amino acids in a ribosome: 8000 = A
# Doubling time of cell = 30 minutes = τ = 1800 s

# (a) Total Number of Ribosomes N in a Bacterium required with τ = 1800 s.
# (b) Fraction of Ribosomes of the Total Protein Pool as a Function of τ.

# Total protein output of a single ribosome over 30 min cell cycle.
    # (i) R1 * τ = 12 * 1800 = 21600 amino acids
    # (ii) R2 * τ = 20 * 1800 = 36000 amino acids
# (a) 
    # (i) N1 * 21600 = 10^9
        # N1 = 10^9 / 21600 = 46296 ribosomes
    # (ii) N2 * 36000 = 10^9
        # N2 = 10^9 / 36000 = 27778 ribosomes
# (b) 
    # Fraction of ribosomal protein = (N * A) / P
    # (i) (46296 * 8000) / 10^9 = 0.37 = 37%
    # (ii) (27778 * 8000) / 10^9 = 0.22 = 22%

# With increasing translation rate, the number of ribosomes needed decreases, as each ribosome is more productive.
# The proportion of cell resources devoted to ribosome production also decreases with an increase in translation rate.
