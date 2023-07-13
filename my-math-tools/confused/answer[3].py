def find_nth_term(n, x_values, y_values, display_expression=False):
    coefficients = []
    for degree in range(len(x_values)):
        # Calculate the coefficient for each term in the interpolating function
        coef = y_values[degree]
        for j in range(len(x_values)):
            if j != degree:
                coef /= (x_values[degree] - x_values[j])
        coefficients.append(coef)
    
    def polynomial(x):
        result = 0
        for degree in range(len(coefficients)):
            term = coefficients[degree]
            for j in range(len(coefficients)):
                if j != degree:
                    # Calculate the term by multiplying the coefficient with the appropriate term (x - x_i) / (x_j - x_i)
                    term *= (x - x_values[j]) / (x_values[degree] - x_values[j])
            result += term
        return result
    
    nth_term = polynomial(n)
    
    if display_expression:
        expression = " + ".join(f"{coefficients[i]} * (x - {x_values[i]})" for i in range(len(coefficients)))
        print(f"The interpolating function is: {expression}")
    
    return nth_term

# Example usage:
x_values = [1, 2, 3, 4, 5]  # X-values of the known points
y_values = [1, 4, 9, 16, 25]  # Y-values of the known points
n = 18  # Position of the term desired

nth_term = find_nth_term(n, x_values, y_values, display_expression=False)
print(f"The {n}th term of the sequence is: {nth_term}")
