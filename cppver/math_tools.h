#include <iostream>
#include <math.h>
#include <vector>

#ifndef math_tools_h // makes sure math_tools_h is defined
#define math_tools_h
#endif // not right after #define b/c unsure about preprocessor directives

using namespace std;

class math_tools {
public:
    long double get_quad_nth_v0(vector<long double>S, int posn); // check documentation to find compatibility with non-naturals ie. vector<_complex>S
    long double parr_res_v0(vector<long double>Ω);
};
