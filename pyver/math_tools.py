class my_math:

    # Time: O(n)
    # Space: O(1)
    def get_quad_nth_v0(self, S: list, n: int) -> float:
        # need these as attributes, since I need to access them for printing the formula
        # make them part of the class but only accessible by this function
        α = S[1] - S[0]
        β = S[2] - S[1]
        x = β - α
        sum = 0.0
        # such loops will likely increase depending on the magnitude of the series. Could be solved with recursion (in polynomial time)
        for i in range(1, n):
            sum += float((x*i)+(α-x))
        return float(S[0]+sum)

    # Time: O(n)
    # Space: O(1)
    def parr_res_v0(self, Ω: list) -> float:
        recoprocal_sum = 0.0
        for i in range(len(Ω)):
            recoprocal_sum += float(1/Ω[i])
        return float(1/recoprocal_sum)