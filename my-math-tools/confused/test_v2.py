import numpy as np
import matplotlib.pyplot as plt

def progression_analysis(lst, param):

	if isinstance(param, int):

		if param <= len(lst) and param >= 1:
			return lst[param - 1]

		if param < 1:
			return None

		def p(x: list[float], y: list[float], x_i: int) -> float:
			'''
			Helper function for calculating Lagrange interpolation.
			p(x) = ∑[i = 0, n] yili(x)
			li(x) = ∏[j = 0, j != i, n] (x - xj)/(xi - xj)
			'''
			s = 0.0
			for i in range(len(y)):
				l = 1.0
				for j in range(len(y)):
					if i == j:
						continue
					l *= (x_i - x[j])/(x[i]-x[j])
				s += y[i]*l
			return round(s, 2)

		return p([float(i) for i in range(1, len(lst)+1)], lst, param)

	elif param == 'exp':
		degree = len(lst) - 1
		coeffs = np.polyfit(range(1, len(lst) + 1), lst, degree)
		polynomial = np.poly1d(coeffs)
		return str(polynomial)

	elif param == 'graph':
		degree = len(lst) - 1
		coeffs = np.polyfit(range(1, len(lst) + 1), lst, degree)
		polynomial = np.poly1d(coeffs)

		x = np.linspace(1, len(lst), 100)
		y = polynomial(x)

		plt.plot(x, y)
		plt.xlabel('n')
		plt.ylabel('f(n)')
		plt.title('Graph of f(n)')
		plt.grid(True)
		plt.show()

	else:
		# Handle invalid parameter case
		return None

print(progression_analysis([1, 8, 27, 64], 'exp'))