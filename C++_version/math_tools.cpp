//define all entities in math_tools.h
#include "math_tools.h"
typedef long double ld;

//basic math functions, not particularly useful
ld math_tools::sigma_func(ld var, ld lower, ld upper) {
    ld total = 0;
        for(lower; lower <= upper; lower++)
            total += var;
        return total;
}

ld math_tools::pi_func(ld var, ld lower, ld upper) {
    ld product = 0;
    for(lower; lower <= upper; lower++)
        product *= var;
    return product;
}

//specific math formulae, real interesting
float math_tools::quad_series(vector<float>S, int posn) {
    //can I return a string that has certain variables embedded in it?
    float α = S[1] - S[0];
    float β = S[2] - S[1];
    float γ = β - α;
    //nth term: S[0] + ∑ γx + α-γ
    int sum = 0;
    for(int i = 1; i < posn; i++)
        sum += float((γ * i) + α - γ);
    return float(S[0]+sum);
}

float math_tools::parr_res(vector<float>Ω) {
    float sum = 0.0;
    for(int i = 0; i < Ω.size(); i++)
        sum += Ω[i]*(1/pow(Ω[i],2));
    sum *= 1/pow(sum,2);
    return sum;
}