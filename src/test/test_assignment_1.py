from src.main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_method

x0 = 1.5
tol = 1e-6

# Approximation Algorithm
print("Approximation Algorithm Result:", approximation_algorithm(x0, tol))

# Bisection Method (for f(x) = x^3 + 4x^2 - 10)
a, b = 1, 2  # Interval where the root is located
print("Bisection Method Result:", bisection_method(a, b, tol, 100))

# Fixed-Point Iteration (for f(x) = x - x^3 + 4x^2 + 10)
print("Fixed-Point Iteration Result:", fixed_point_iteration(x0, tol))

# Newton-Raphson Method (for f(x) = cos(x) - x)
p0 = 0.5
print("Newton-Raphson Method Result:", newton_method(p0, tol))
