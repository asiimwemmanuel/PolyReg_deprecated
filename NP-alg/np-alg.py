# as you prompt GPT, remember to maintain the relationship between k and progression order
# find a way to defeat rounding errors

# Time: O(n^2)
# Space: O(k(k+1)/2)
class NP_alg:
	def np_alg(prog: list, n: int) -> float:

		# k = order + 1. Assumes prog[] contains the NECESSARY terms only
		k = len(prog)

		# check if vars are valid
		if n <= 0 or k <= 1:
			return None

		# due to list indexing, the nth term is found at prog[n-1]
		n -= 1

		# Return the nth term if already found in prog[]
		if n < k:
			return prog[n]
		
		# To save time
		if len(prog) == 2:
			# formula for the nth term of an arithmetic progression: a + (n-1)*d
			return prog[0] + (n - 1) * (prog[1] - prog[0])
		elif len(prog) == 3:
			# formula for the nth term of a quadratic progression: a + (n-1)d + (n-1)(n-2)/2 * c
			return prog[0] + (n - 1) * (prog[1] - prog[0]) + (n - 1) * (n - 2) / 2 * (prog[2] - 2 * prog[1] + prog[0])
		elif len(prog) == 4:
			# formula for the nth term of a cubic progression: a + (n-1)d + (n-1)(n-2)/2 * c1 + (n-1)(n-2)(n-3)/6 * c2
			return (3 * prog[3] - 6 * prog[2] + 4 * prog[1] - prog[0]) * (n - 1) * (n - 2) * (n - 3) / 6 \
					+ (prog[2] - 3 * prog[1] + 3 * prog[0] - prog[3]) * (n - 1) * (n - 2) / 2 \
					+ (prog[1] - prog[0]) * (n - 1) \
					+ prog[0]

		else:
			# Initialize the first row of the difference table
			table = [[prog[i] for i in range(k)]]

			# Calculate the other rows in the  difference table
			for i in range(k-1):
				row = []
				for j in range(k-i-1):
					diff = table[i][j+1] - table[i][j]
					row.append(diff)
				table.append(row)

			# Calculate the nth term using the difference table. This part needs investigation
			term = table[k-1][0]
			for i in range(1, k):
				prod = 1
				for j in range(i):
					prod *= (n - j)
				term += (prod * table[k-i-1][0])

		return term

# ------------------------------------ TESTING ------------------------------------
test = NP_alg()
# DEMO
for i in range(10**4):
	print(i , "->", test.np_alg([1, 8, 27, 64],i))

# test for k = 1, 2, 3 ... 10**4 (for quick testing).
# The upper bound changes depending on the type of testing.
# If thorough, upper bound is 10**100.
# For each k, check the following for at least 50 different progs:
# 	normal
# 	edge
# 	corner
# 	invalid
# Half of the 50 progs in a given k are depreciating lists. The other half are appreciating lists
# In each prog, the difference table should contain increasingly more decimal points (from ) in its floats
# export failed tests to test_log.txt in the same directory

# # Test normal input with k = 1 (first 2 terms are 1 and 5 then 1 and 2)

# assert np_alg([1, 5], 0) == 0
# assert np_alg([1, 5], 1) == 1
# assert np_alg([1, 5], 2) == 5
# assert np_alg([1, 5], 3) == 9
# assert np_alg([1, 5], 4) == 13
# assert np_alg([1, 5], 5) == 17
# assert np_alg([1, 5], 10) == 37
# assert np_alg([1, 2], 0) == 0
# assert np_alg([1, 2], 1) == 1
# assert np_alg([1, 2], 2) == 2
# assert np_alg([1, 2], 3) == 3
# assert np_alg([1, 2], 10) == 10

# # Test extreme input with k = 1 (first 2 terms vary)

# assert np_alg([1, 1009], 0) == 0
# assert np_alg([6.21, 10000021], 1) == 6.21
# assert np_alg([1, 14151], 3) == 28301
# assert np_alg([1, 1002101], 10000) == 10019997901
# assert np_alg([1, 101124], 10001) == 1011230001
# assert np_alg([1, 0], 10210) == -10209

# # Test edge/corner input with k = 1 (first 2 terms are 1 and 2)


# # Test invalid input with k = 1 (first 3 terms are 1, 5)

# assert np_alg([1, 5], -1) == None
# assert np_alg([1, 5], 0.5) == None
# assert np_alg([1, 5], 4.5) == None
# assert np_alg([1, 5], "a") == None
# assert np_alg([1, 5], None) == None

# # Test normal input for quadratic progression with k = 2 (first four terms are 2, 5, 10)

# assert np_alg([2, 5, 10], 0) == 0
# assert np_alg([2, 5, 10], 1) == 2
# assert np_alg([2, 5, 10], 2) == 5
# assert np_alg([2, 5, 10], 3) == 10
# assert np_alg([2, 5, 10], 4) == 17
# assert np_alg([2, 5, 10], 5) == 28
# assert np_alg([2, 5, 10], 6) == 39