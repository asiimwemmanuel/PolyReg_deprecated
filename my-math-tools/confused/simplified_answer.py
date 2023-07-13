import numpy as np

def find_nth_term(n, x_values, y_values) -> float:
    coefficients = np.polyfit(x_values, y_values, len(x_values) - 1)
    polynomial = np.poly1d(coefficients)
    return polynomial(n)

# Example usage:
x_values = [1, 2, 3, 4]  # X-values of the known points
y_values = [2, 4, 8, 16]  # Y-values of the known points

for i in range(10):
	print(f"The {i}th term of the sequence is: {find_nth_term(i, x_values, y_values):.2f}")
