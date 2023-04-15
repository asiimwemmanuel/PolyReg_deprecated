// Might change the dependency on long doubles to complex numbers

#include <iostream>
#include <math.h>
#include <vector>

#define prog vector<long double> // progression definition

typedef long double ld;
using namespace std;

class math_tools {
public:
    class quad_tools {
    public:
        // either removed entirely, parameters will change or modified to receive progression magnitude
        quad_tools(ld a, ld b, ld c);
        // check documentation to find compatibility with imaginary numbers ie. vector<_complex>S
        ld get_quad_nth_v0_0(prog S, int posn);
        ld get_quad_nth_v1_0(prog S, int posn);
        ld get_quad_nth_v2_0(prog S, int posn);
        ld get_quad_nth_v2_1(prog S, int posn);
        ld get_quad_nth_v3_0(prog S, int posn);
        ld get_quad_nth_v3_1(prog S, int posn);
        // only to output a formula. Will not be included for NP-alg().
        ld α, β, x;
        // difference table:
            // α = S[1] - S[0];
            // β = S[2] - S[1];
            // x = β - α;
    };
    ld parr_res_v0(prog Ω);
};