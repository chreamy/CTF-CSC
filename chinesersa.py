from sympy import symbols, Eq, gcd, solve

# Given values
N = 1481162781400309006761410131097650867404271858439557572357702716476911109
e = 3
C1 = 383959923261929119807038368007402205817644876672712648704618871543676316
C2 = 148209684408489840089982879211741755329442835437440763430482279534770741

# Define the variables
x, M2 = symbols('x M2', integer=True)

# Define the linear polynomial f = ax + b
a = symbols('a', integer=True, nonzero=True)
b = symbols('b', integer=True, nonzero=True)
f = a * x + b

# Define the polynomials g1 and g2
g1 = (f**e - C1).expand()
g2 = (x**e - C2).expand()

# Compute the GCD of g1 and g2
GCD = gcd(g1, g2)

# Check if the GCD is a linear polynomial x - M2
linear_polynomial = Eq(GCD, x - M2)

# Solve for M2 if the GCD is linear
solutions = solve(linear_polynomial, M2)

# Print the solutions
if solutions:
    M2_value = solutions[0]
    print("M2:", M2_value)
else:
    print("No solution found.")
