'''might need to use newton's divided difference, even though time is O(n^2) but constant is smaller'''
# solves for any degree polynomial

from typing import List, Union
import numpy as np

class gpt:
	'''
	Implementation of General Polynomial Time algorithm for finding nth term in a sequence.
	Uses Lagrange Interpolation to calculate the value of nth term.
	Time: O(n^2)
	Space: O(n)
	Only works when polynomial expression has a constant degree (no x^x)
	'''
	@staticmethod
	def interpolate(data: List[float], n: Union[int, bool]=False) -> float | None:
		'''
		Parameters:
		    data (List[float]): A list of known terms of the sequence, staring with the 1st.
		    n (int): The position of the term to be found.
		Returns:
		    Union[float, None]: The value of nth term of the sequence, or None if n is less than or equal to 0.
		Time: O(n^2 - n)
		Space: O(n)
		'''

		if n == True:
			# supposed to return a polynomial fit instead of a float
			return None

		def p(x: List[float], progression: List[float], x_i: int) -> float:
			'''
			Helper function for calculating Lagrange interpolation.
			p(x) = ∑[i = 0, n] yili(x)
			li(x) = ∏[j = 0, j != i, n] (x - xj)/(xi - xj)
			'''
			s = 0.0
			for i in range(len(progression)):
				l = 1.0
				for j in range(len(progression)):
					if i == j:
						continue
					l *= (x_i - x[j])/(x[i]-x[j])
				s += progression[i]*l
			return round(s, 2)


		# checking the validity of n
		if n <= 0:
			return None

		# checking if the term needs to be interpolated
		elif n <= len(data):
			return float(data[n-1])

		# getting the set of known x-values
		x = [float(i) for i in range(1, len(data)+1)]

		return p(x, data, n)

test = gpt()

for i in range(100):
	print(test.interpolate([1, 2], i))