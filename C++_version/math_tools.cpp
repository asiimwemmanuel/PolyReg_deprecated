#include "math_tools.h"
// #include <vector>

typedef long double ld;

// Time: O(n)
// Space: O(1)
ld math_tools::get_quad_nth_v0(vector<ld>S, int posn) {
    // should be globals for α, β and x to avoid resourec duplication, or make them part of the class but only accessible by this function
    ld α = S[1] - S[0];
    ld β = S[2] - S[1];
    ld x = β - α;
    ld sum = 0.0;
    // such loops will likely increase depending on the magnitude of the series. Could be solved with recursion (in polynomial time)
    for(int i = 1; i < posn; i++)
        sum += ld((x*i)+(α-x));
    return ld(S[0]+sum);
}

// Time: O(n)
// Space: O(1)
ld math_tools::parr_res_v0(vector<ld>Ω) {
    ld reciprocal_sum = 0.0;
    for(int i = 0; i < Ω.size(); i++)
        reciprocal_sum += ld(1/Ω[i]);
    return ld(1/reciprocal_sum);
}