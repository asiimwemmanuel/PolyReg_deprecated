class my_math:

	class quad_tools:
		# only to output a formula. Will not be included for NP-alg(). Notice that β is not used in the formula
		α = β = x = 0.0

		# will change in NP-alg
		def __init__(self, a: float, b: float, c: float) -> None:
			self.α = a
			self.β = b
			self.x = c
		
		# Time: O(n)
		# Space: O(1)
		def get_quad_nth_v0(self, S: list, posn: int) -> float:
			sum = 0.0
			# such loops will likely increase depending on the magnitude of the series. Could be solved with recursion (in polynomial time)
			for i in range(1, posn):
				sum += float((self.x*i)+(self.α-self.x))
			return float(S[0]+sum)
		
		# correct
		def get_quad_nth_v1(self, S: list, posn: int) -> float:
			return S[0] + ((posn-1)*((self.x*posn)+2*(self.α-self.x)))/2

		# wrong
		def get_quad_nth_v2_0(self, S: list, posn: int) -> float:
			return S[0] + (posn-1)*(self.α+self.x*(posn-1))

		# wrong
		def get_quad_nth_v2_1(self, S: list, posn: int) -> float:
			return S[0] + (posn-1)*(self.α+self.x*(posn-2))

		# equal to get_quad_nth_v2_0()
		def get_quad_nth_v3_0(self, S: list, posn: int) -> float:
			return S[0] + (posn-1)*(self.α+(posn-1)*self.x)

		# equal to get_quad_nth_v2_1()
		def get_quad_nth_v3_1(self, S: list, posn: int) -> float:
			return S[0] + (posn-1)*(self.α+(posn-2)*self.x)

		# difference table:
		#   self.α = S[1] - S[0];
		#   β = S[2] - S[1];
		#   self.x = β - self.α;

	# Time: O(n)
	# Space: O(1)
	def parr_res_v0(self, Ω: list) -> float:
		recoprocal_sum = 0.0
		for i in range(len(Ω)):
			recoprocal_sum += float(1/Ω[i])
		return float(1/recoprocal_sum)