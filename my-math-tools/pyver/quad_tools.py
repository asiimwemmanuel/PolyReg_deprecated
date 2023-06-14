# outdated version; only accounts for linear and quadratic polynomials

class quad:
	# only to output a formula. Will not be included for gpt_alg().
	α = β = x = 0.0

	# isn't in GPT-alg, would include lots of memory for large degree functions.
	def __init__(self, a: float, c: float) -> None:
		self.α = a
		self.x = c
	
	# Time: O(n)
	# Space: O(1)
	def quad_alg_v0(self, S: list, n: int) -> float:
		sum = 0.0
		# nth term (degree x) = S[0] + n-1th term (degree x-1) - recursion.
		for i in range(1, n):
			sum += float((self.x*i)+(self.α-self.x))
		return float(S[0]+sum)
	
	# correct
	def quad_alg_v1(self, S: list, n: int) -> float:
		return S[0] + ((n-1)*((self.x*n)+2*(self.α-self.x)))/2
	
	# correct
	def quad_alg_v2(self, S: list, n: int) -> float:
		return S[0] + (self.x*(n**2) - 3*(self.x*n) + 2*(self.x))/2 + self.α*n - self.α
	
	# difference table:
	#   self.α = S[1] - S[0];
	#   β = S[2] - S[1];
	#   self.x = β - self.α;