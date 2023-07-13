# use main to run tests. this file has buggy relative imports

import random
from typing import List, Tuple
import unittest
import numpy as np
# relative import is buggy.
from ..src.polytrend import PolyTrend

class PolyTrendTest(unittest.TestCase):
	def setUp(self):
		self.polytrend = PolyTrend()

	# tests polyplot in all applicable degrees
	# gonna modify with parameters soon
	def plotest(self):
		# testing linear, quadratic, cubic and quartic polynomials
		for i in range(1, 5):
			data = self.generate_data(i, 100, -100, 100, -1000, 1000)
			print("Generated Data:")
			for point in data:
				print(point)
			print("Plotting...")
			self.polytrend.polyplot(range(1, 5), data)

	# def fitest(self):
	# 	# testing linear, quadratic, cubic and quartic polynomials
	# 	known_data = self.generate_data(range(1, 5), 1000, 0, 100, 0, 10)
	# 	func = self.polytrend.polyfind(range(1, 5), known_data)

	def generate_data(self, degree: int, num_samples: int, data_lower_bound: float, data_upper_bound: float, err_lower_bound: float, err_upper_bound: float) -> List[Tuple[float, float]]:
		# generating a random polynomial of specified degree, bounds are arbitrary
		coeffs = np.array([random.uniform(1, 50) for i in range(degree+1)])

		# Generate the data using the specified parameters
		# x = random.uniform(data_lower_bound, data_upper_bound)
		# y = np.polyval(coeffs, x) + random.uniform(err_lower_bound, err_upper_bound)
		data = [
			(x, float(np.polyval(coeffs, x)) + random.uniform(err_lower_bound, err_upper_bound))
			for x in [
				random.uniform(data_lower_bound, data_upper_bound) for _ in range(num_samples)
			]
		]

		return data

if __name__ == '__main__':
	unittest.main()