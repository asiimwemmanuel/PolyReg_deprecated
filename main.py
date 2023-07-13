# main serves as test due to relative imports bug, use the commented out import statement once it works

import random
from typing import List, Tuple
import numpy as np

# relative import is buggy in test file. decided to use it here
from src.polytrend import PolyTrend

class PolyTrendTest():
	def __init__(self):
		self.polytrend = PolyTrend()

	# tests polyplot in all applicable degrees (listed below)
	# tests polyplot at a certain degree
	def plotest(self, degree: int) -> None:
		# testing linear, quadratic, cubic, and quartic polynomials
		# remember to adjust the error bounds based on the degree. My personal desired R-squared should be approx. 0.8
		data = self.generate_data(degree, 100, -100, 100, -20000, 20000)
		print("\nGenerated Data:\n")
		for point in data:
			print(point)
		print("\nPlotting...\n")
		self.polytrend.polyplot(range(1, degree+1), data)
		print("\nFinished 😉\n")

	# def fitest(self):
	# 	# testing linear, quadratic, cubic and quartic polynomials
	# 	known_data = self.generate_data(range(1, 5), 1000, 0, 100, 0, 10)
	# 	func = self.polytrend.polyfind(range(1, 5), known_data)

	def generate_data(self, degree: int, num_samples: int, data_lower_bound: float, data_upper_bound: float, err_lower_bound: float, err_upper_bound: float) -> List[Tuple[float, float]]:
		# generating a random polynomial of specified degree, bounds are arbitrary
		coeffs = np.array([random.randint(1, 10) for i in range(degree+1)])

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
	print("This is a simple example of the PolyTrend capability 🕺")
	test = PolyTrendTest()
	test.plotest(2)
	print("Check ./models for the plots 😁")