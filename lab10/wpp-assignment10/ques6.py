import numpy as np
import matplotlib.pyplot as plt
import random

def evaluate_polynomial(coefficients, x):
    """
    Evaluate the polynomial for a given x using its coefficients.
    """
    return sum(c * x**i for i, c in enumerate(coefficients))

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    iterations = []  # Array to store updates
    if f(a) * f(b) >= 0:
        print("Bisection method cannot proceed. f(a) and f(b) must have opposite signs.")
        return None, np.array(iterations)
    
    for i in range(max_iter):
        c = (a + b) / 2
        iterations.append((a, b, c, f(c)))
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return c, np.array(iterations)

def main():
    try:
        # Take polynomial input from the user
        degree = int(input("Enter the degree of the polynomial: "))
        print(f"Enter the coefficients of the polynomial (from x^0 to x^{degree}):")
        coefficients = [float(input(f"Coefficient of x^{i}: ")) for i in range(degree + 1)]
        
        # Define the polynomial function
        f = lambda x: evaluate_polynomial(coefficients, x)
        
        # Randomly probe an interval for the root
        a = random.uniform(-10, 10)
        b = random.uniform(-10, 10)
        while f(a) * f(b) >= 0:  # Ensure a and b have opposite signs
            a = random.uniform(-10, 10)
            b = random.uniform(-10, 10)
        
        print(f"Initial interval: a = {a}, b = {b}")
        
        root, updates = bisection_method(f, a, b)
        if root is not None:
            print(f"Root found: x = {root}")
            print("\nUpdates during root-finding:")
            print(updates)

            # Plotting the root-finding process
            x_vals = np.linspace(a, b, 1000)
            y_vals = [f(x) for x in x_vals]
            plt.plot(x_vals, y_vals, label="f(x)")
            plt.axhline(0, color="red", linestyle="--", linewidth=0.8)
            plt.scatter(updates[:, 2], [f(x) for x in updates[:, 2]], color="green", label="Iterations")
            plt.title("Bisection Method Root-Finding Process")
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.legend()
            plt.grid()
            plt.show()
        else:
            print("No root found due to invalid initial interval.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    main()
