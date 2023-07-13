# calculates parallel resistance

class res:
	'''
	Implementation of an algorithm that finds parallel resistance.
	Uses some method to do so
	Time: O(n)
	Space: O(n)
	'''
	def parr_res_v0(self, Ω: list[float]) -> float:
		if Ω == None:
			return 0
		recoprocal_sum = 0.0
		for i in range(len(Ω)):
			recoprocal_sum += float(1/Ω[i])
		return float(1/recoprocal_sum)