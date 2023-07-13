import numpy as np
import matplotlib.pyplot as plt

def polytrend(data, degree):
	x = np.array(list(data.keys()))
	y = np.array(list(data.values()))

	# Fit the polynomial
	coeffs = np.polyfit(x, y, degree)
	poly_func = np.poly1d(coeffs)
	# Generate points for plotting
	x_range = np.linspace(min(x), max(x), 100)
	y_range = poly_func(x_range)

	# Plot the graph
	plt.figure()
	plt.plot(x_range, y_range, label='Fitted Polynomial')
	plt.scatter(x, y, c='r', label='Data Points')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.title('Polynomial Fit')
	plt.show()

	# Extrapolation
	def extrapolate(n):
		return poly_func(n)

	# Display function fit in specified format
	func_fit = 'f(n) -> '
	for i, coeff in enumerate(coeffs[::-1]):
		power = degree - i
		if power == 0:
			func_fit += f'{coeff:.2f}'
		elif power == 1:
			func_fit += f'{coeff:.2f}n + '
		else:
			func_fit += f'{coeff:.2f}n^{power} + '
	print(func_fit)

	return extrapolate

# Example usage
data = {1: 2, 2: 4, 3: 8, 4: 16, 5: 32}
degree = 3

extrapolate_func = polytrend(data, degree)
print(extrapolate_func(6))  # Extrapolating at n = 6
