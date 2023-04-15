#include "math_tools.h"

math_tools::quad_tools::quad_tools(ld a, ld b, ld c) : α(a), β(b), x(c) {}

// Time: O(n)
// Space: O(1)
ld math_tools::quad_tools::quad_tools::get_quad_nth_v0_0(prog S, int posn) {
    ld sum = 0.0;
    // such loops will likely increase depending on the magnitude of the series. Could be solved with recursion (in polynomial time) or a clever general solution
    for(int i = 1; i < posn; i++)
        sum += ld((x*i)+(α-x));
    return ld(S[0]+sum);
}

// correct
ld math_tools::quad_tools::get_quad_nth_v1_0(prog S, int posn) {
    return S[0] + ((posn-1)*((x*posn)+2*(α-x)))/2;
}

// wrong
ld math_tools::quad_tools::get_quad_nth_v2_0(prog S, int posn) {
    return S[0] + (posn-1)*(α+x*(posn-1));
}

// wrong
ld math_tools::quad_tools::get_quad_nth_v2_1(prog S, int posn) {
    return S[0] + (posn-1)*(α+x*(posn-2));
}

// equal to get_quad_nth_v2_0()
ld math_tools::quad_tools::get_quad_nth_v3_0(prog S, int posn) {
    return S[0] + (posn-1)*(α+(posn-1)*x);
}

// equal to get_quad_nth_v2_1()
ld math_tools::quad_tools::get_quad_nth_v3_1(prog S, int posn) {
    return S[0] + (posn-1)*(α+(posn-2)*x);
}

// Time: O(n)
// Space: O(1)
ld math_tools::parr_res_v0(prog Ω) {
    ld reciprocal_sum = 0.0;
    for(int i = 0; i < Ω.size(); i++)
        reciprocal_sum += ld(1/Ω[i]);
    return ld(1/reciprocal_sum);
}