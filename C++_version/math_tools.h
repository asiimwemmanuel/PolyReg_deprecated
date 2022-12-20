//declare (not define) all universal entities
#include<iostream>
#include<math.h>
#include<vector>
// #include<string>
using namespace std;
#ifndef math_tools_h
#define math_tools_h

//remember to include complex or irrational numbers in the code
class math_tools {
public:
    long double sigma_func(long double var, long double lower, long double upper);
    long double pi_func(long double var, long double lower, long double upper);
    float parr_res(vector<float>Ω);
    float get_nth(vector<float>S, int posn); //_complex base_sequence[]?
};
#endif