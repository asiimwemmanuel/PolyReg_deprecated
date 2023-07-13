class quad_tools:
	# Time: O(1)
	# Space: O(1)
	# Asiimwe's quadratic formula
	def get_quad_nth_v0(self, seq: list, n: int) -> float:
		# Note that β isn't used in the main formula (since it can be derived from the other two)
		α = seq[1] - seq[0]
		# β = seq[2] - seq[1]
		c = seq[2] - 2 * seq[1] + seq[0]
		return seq[0] + (n-1) * ( (c * (n - 2) + 2 * α) ) / 2