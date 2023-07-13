import numpy as np

def find_nth_term(n, x_values, y_values, display_expression=False):
    coefficients = np.polyfit(x_values, y_values, len(x_values) - 1)
    polynomial = np.poly1d(coefficients)
    nth_term = polynomial(n)

    if display_expression:
        expression = polynomial.__str__()
        print(f"The interpolating function is: {expression}")

    return nth_term

# Example usage:
x_values = [1, 2, 3, 4, 5]  # X-values of the known points
y_values = [1, 8, 27, 64, 125]  # Y-values of the known points
n = 6  # Position of the term desired

nth_term = find_nth_term(n, x_values, y_values, display_expression=True)
print(f"The {n}th term of the sequence is: {nth_term}")
