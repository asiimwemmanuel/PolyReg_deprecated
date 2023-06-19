import numpy as np
import matplotlib.pyplot as plt

# confirms the data characteristics
def nth_term_validator(coord: dict) -> bool:
	if not isinstance(coord, dict) or len(coord) < 2:
		print("Invalid input data. Expected a list with at least two elements.")
		return False

	return True

def polynomial_regression(coord: dict, param):
	if nth_term_validator(coord):
		order = len(coord) - 1
		coeffs = np.polyfit(np.arange(len(coord)), list(coord.values()), order)

		if isinstance(param, float):
			# if the user asks for what was already given
			if param in list(coord.keys()):
				return coord.get(param)

			# Perform polynomial regression to estimate the value
			estimated_value = np.polyval(coeffs, param)

			return estimated_value

		elif isinstance(param, str):
			if param == 'exp':
				# Construct the polynomial expression
				expression = ''

				for i in range(order, -1, -1):
					coeff = coeffs[order - i]
					
					if coeff != 0:
						term = f"{coeff}n^{i}" if i > 1 else f"{coeff}n" if i == 1 else str(coeff)
						expression += term + " + "

				expression = expression.rstrip(" + ")

				return expression

			elif param == 'graph':
				# Plot the graph using the suggested polynomial expression
				x_vals = np.arange(len(list(coord.values())))
				y = np.array(list(coord.values()))
				coeffs = np.polyfit(x_vals, y, order)
				poly = np.poly1d(coeffs)
				plt.plot(x_vals, y, 'bo', label='Data')
				plt.plot(x_vals, poly(x_vals), 'r-', label='Polynomial Fit')
				plt.xlabel('n')
				plt.ylabel('f(n)')
				plt.legend()
				plt.show()

			else:
				raise ValueError("Invalid parameter. Expected 'exp' or 'graph'.")

		else:
			raise ValueError("Invalid parameter type. Expected a float or a string.")

# Example usage
data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
parameter = 100.0
output = polynomial_regression(data, parameter)
print(output)
