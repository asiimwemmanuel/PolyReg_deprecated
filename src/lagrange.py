class lagrange:
	def lagrange_polynomial(x, y):
		"""
		Generate and return the Lagrange's polynomial function.
	
		Args:
			x (list): List of x-coordinates of the data points.
			y (list): List of y-coordinates of the data points.
	
		Returns:
			function: The generated Lagrange's polynomial function as a lambda function.
		"""
		n = len(x)

		return lambda x_val: sum(
			y[i] * (
				lambda xi: lambda x_val, i: 
					(x_val - x[i]) / (xi - x[i])
			)(x[i])(x_val, i)
			for i in range(n)
		)