from typing import List, Union
import matplotlib.pyplot as plt
import numpy as np

class MyMathTools:

	class NthTerm:

		def __init__(self, prog: List[float]) -> None:
			self.prog = prog
			self.polydeg = len(prog) - 1

		def calculate_value_at_position(self, posn: int) -> Union[None, float]:
			if posn < 1:
				return None

			elif posn <= len(self.prog):
				return self.prog[posn - 1]

			elif posn > len(self.prog):
				return self.lagrange_interpolation(posn)

		# has bugs
		def generate_polynomial_expression(self) -> str:
			expression = self.lagrange_interpolation_expression()
			polynomial = self.format_polynomial_expression(expression)

			return polynomial

		def plot_progression_graph(self) -> None:
			y = self.prog

			for i in range(len(self.prog)+1, 1001):
				y.append(self.lagrange_interpolation(i))

			x = list(range(1, len(y)+1))
		
			plt.plot(x, y, marker='o')
			plt.xlabel('Position')
			plt.ylabel('Value')
			plt.title('Graph of f(n)')
			plt.grid(True)
			plt.show()

		def lagrange_interpolation(self, posn):
			'''
			Helper function for calculating Lagrange interpolation.
			p(x) = ∑[i = 0, n] yili(x)
			li(x) = ∏[j = 0, j != i, n] (x - xj)/(xi - xj)
			'''

			# due to list indexing
			posn -= 1
			s = 0.0

			for i in range(len(self.prog)):
				l = 1.0

				for j in range(len(self.prog)):
					if i != j:
						l *= (posn - j)/(i - j)

				s += self.prog[i]*l

			return round(s, 2)

		def lagrange_interpolation_expression(self) -> List[float]:
			coefficients = []
			
			for i in range(self.polydeg + 1):
				term = self.prog[i]
				for j in range(self.polydeg + 1):
					if j != i:
						term /= (i - j)
				coefficients.append(term)
			
			return coefficients

		def format_polynomial_expression(self, coefficients) -> str:
			terms = []
			
			for i in range(self.polydeg, -1, -1):
				term = f"{round(coefficients[i], 2)}n^{i}"
				terms.append(term)
			
			expression = "f(n) -> " + " + ".join(terms)
			
			return expression

test = MyMathTools.NthTerm([1.0, 2.0])

for i in range(2, 1001):
	print(test.calculate_value_at_position(i))

print(test.plot_progression_graph())