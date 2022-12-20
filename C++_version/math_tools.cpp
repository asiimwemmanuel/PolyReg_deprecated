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
float math_tools::get_nth(vector<float>S, int posn) {
    //can I return a string that has certain variables embedded in it?
    float α = S[1] - S[0];
    float β = S[2] - S[1];
    float γ = β - α;
    //nth term: S[0] + ∑ γx + α-γ
    int sum = 0;
    // such loops will likely increase depending on the magnitude of the series. such a problem could be solved with recursion (in polynomial time), at least in the short term
    for(int i = 1; i < posn; i++)
        sum += float(γ * i);
    return float(S[0]+sum+((α-γ)*(posn-1))); //refactiring the sum to S[0] + ∑ (γx) + (α-γ)(n-1)
}

float math_tools::parr_res(vector<float>Ω) {
    float sum = 0.0;
    for(int i = 0; i < Ω.size(); i++)
        sum += Ω[i]*(1/pow(Ω[i],2));
    sum *= 1/pow(sum,2);
    return sum;
}