# correct
def get_quad_nth_v1(S: list, n: int) -> float:
	α = S[1] - S[0]
	β = S[2] - S[1]
	x = β - α
	return S[0] + ((n-1)*((x*n)+2*(α-x)))/2

# wrong
def get_quad_nth_v2_0(S: list, n: int) -> float:
	α = S[1] - S[0]
	β = S[2] - S[1]
	x = β - α
	return S[0] + (n-1)*(α+x*(n-1))

# wrong
def get_quad_nth_v2_1(S: list, n: int) -> float:
	α = S[1] - S[0]
	β = S[2] - S[1]
	x = β - α
	return S[0] + (n-1)*(α+x*(n-2))

# equal to get_quad_nth_v2_0()
def get_quad_nth_v3_0(S: list, n: int) -> float:
	α = S[1] - S[0]
	β = S[2] - S[1]
	x = β - α
	return S[0] + (n-1)*(α+(n-1)*x)

# equal to get_quad_nth_v2_1()
def get_quad_nth_v3_1(S: list, n: int) -> float:
	α = S[1] - S[0]
	β = S[2] - S[1]
	x = β - α
	return S[0] + (n-1)*(α+(n-2)*x)

for i in range(10**3+1):
	print(f"i = {i}: {get_quad_nth_v1([1,4,9], i):.3f} {get_quad_nth_v2_0([1,4,9], i):.3f} {get_quad_nth_v2_1([1,4,9], i):.3f} {get_quad_nth_v3_0([1,4,9], i):.3f} {get_quad_nth_v3_1([1,4,9], i)}")