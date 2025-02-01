import math

# Approximation Algorithm
def approximation_algorithm(x0, tol, max_iter=100):
    x = x0
    for iter in range(max_iter):
        y = x
        x = (x / 2) + (1 / x)
        if abs(x - y) < tol:
            return x
    return x

# Bisection Method
def f_bisection(x):
    return x**3 + 4*x**2 - 10

def bisection_method(a, b, tol, max_iter):
    left, right = a, b
    for _ in range(max_iter):
        mid = (left + right) / 2
        if f_bisection(left) * f_bisection(mid) < 0:
            right = mid
        else:
            left = mid
        if abs(right - left) < tol:
            return mid
    return mid

# Fixed-Point Iteration
def g_fixed(x):
    return x - x**3 + 4*x**2 + 10

def fixed_point_iteration(p0, tol, max_iter=50):
    for _ in range(max_iter):
        p = g_fixed(p0)
        if abs(p - p0) < tol:
            return p
        p0 = p
    return p0

# Newton-Raphson Method
def f_newton(x):
    return math.cos(x) - x

def f_newton_prime(x):
    return -math.sin(x) - 1

def newton_method(p0, tol, max_iter=100):
    for _ in range(max_iter):
        if f_newton_prime(p0) == 0:
            return None
        p_next = p0 - f_newton(p0) / f_newton_prime(p0)
        if abs(p_next - p0) < tol:
            return p_next
        p0 = p_next
    return None
