# this script performs polynomial regression with model selection in two dimensions (x, y)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# base tools I've made to help with regression analysis
# other versions will be PolyReg_stat, PolyReg_econ, PolyReg_cs etc, refer to documentation
class PolyReg_base_v0:
	def __init__(self):
		pass

	# Constructs the best polynomial fit based on the trend in the data
	def polytrend_v0(self, data: dict[float, float], new_data: list, degree: int = -1) -> str:

		# simple validation to ensure 'relativity'
		if len(data) < 2:
			raise ValueError("Dataset is too small, must be at least two data points.")

		# Define the x and y axes
		x = np.array(list(data.keys()))
		y = np.array(list(data.values()))

		# Define the training and testing data
		x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

		# The heart of the operation :)
		if degree == -1:
			mse_scores = []
			potent_degs = range(0, 5) # arbitrary

			# evaluating performance of different models: flat, linear, ... quintic.
			for temp_deg in potent_degs:
				# Create polynomial features
				polynomial_features = PolynomialFeatures(temp_deg=temp_deg)
				x_poly = polynomial_features.fit_transform(x_train.reshape(-1, 1))
			
				# Perform ridge regression with cross-validation
				ridge = Ridge(alpha=1.0)  # You can adjust the alpha parameter for regularization
				cv_scores = -cross_val_score(ridge, x_poly, y_train, cv=5, scoring='neg_mean_squared_error')
				average_mse = np.mean(cv_scores)
				mse_scores.append(average_mse)

			best_deg = potent_degs[np.argmin(mse_scores)]

			# selecting the best model
			polynomial_features = PolynomialFeatures(degree=best_degree)
			x_poly = polynomial_features.fit_transform(x_train.reshape(-1, 1))
			ridge = Ridge(alpha=1.0)
			ridge.fit(x_poly, y_train)

			# Evaluate the model on the test set
			x_test_poly = polynomial_features.transform(x_test.reshape(-1, 1))
			y_pred = ridge.predict(x_test_poly)
			mse = mean_squared_error(y_test, y_pred)

		# If the degree is specified
		else:
			coeffs = np.polyfit(x, y, degree)
			polynomial = np.poly1d(coeffs)

		# Generates the printed polynomial equation
		equation = "f(n) = "
		for i, βi in enumerate(reversed(coeffs)):
			equation += f"{βi:.2f}n^{i:.1f} + "

		# Remove the last "+ "
		equation = equation[:-2]

		print(equation)

		# Generate curve's points
		# cool trick to maintain viewing ratio of 120% of maximum extrapolate
		# x_curve = np.arange(1, 1.2 * max(new_data), 0.1)
		x_curve = np.linspace(min(x), max(x), 100)
		y_curve = polynomial(x_curve)

		# Plot the graph, highlighting given vs calculated points
		plt.title('PolyTrend')
		plt.xlabel('n')
		plt.ylabel('f(n)')
		plt.plot(x, y, 'bo', label='Given Data')
		plt.plot(x_curve, y_curve, 'r-', label='Line Fit')

		for i in new_data:
			plt.scatter(i, polynomial(i), c='g', label=f'({i}, {polynomial(i):.2f})')

		plt.legend()
		plt.show()

		# Store & print extrapolated values respectively
		result_dict = {}
		result_string = ''

		# extrapolating each point
		for element in new_data:
			result = polynomial(element)
			result_dict[element] = result

		# Output the dictionary in the desired format
		for key, value in result_dict.items():
			result_string += f"f({key}) → {value:.2f}\n"

		return result_string

	# Ensures that basic rules for the nth term are maintained.
	# If the degree is not known, program assumes the given data is the bare minimum required to describe the pattern
	def find_nth_term(self, sequence: list, n: list, order: int = -1) -> str:

		if min(n) < 1:
			raise ValueError(f"Invalid n value provided: {min(n)}")

		# checking if the degree was given, and assuming all data points relevant if it isn't
		# since there's typically little to no noise, there's less risk of overfitting
		if order == -1:
			order = len(sequence) - 1

		formatted_sequence = {float(key): float(value) for key, value in zip(range(1, len(sequence)+1), sequence)}
		equation = self.polytrend_v0(formatted_sequence, list(n), order)

		return equation
		
	def lagrange_interp(self, data: dict):
		pass

test = PolyReg_base_v0()

sequence = [5,7,9,11,13,15,17,19,21,23]
print(test.find_nth_term(sequence, [89]))
