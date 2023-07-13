// declarations for all 3 classes

#include <vector>

#define prog vector<long double> // progression definition

typedef long double ld;
using namespace std;

// outdated version
// only accounts for linear and quadratic polynomials
class quad_tools {
public:
	// either removed entirely, parameters will change or modified to receive progression magnitude in gpt_alg()
	quad_tools(ld a, ld b, ld c);
	// check documentation to find compatibility with complex numbers ie. vector<_complex>S
	ld quad_alg_v0(prog S, int n);
	ld quad_alg_v1(prog S, int n);
	ld quad_alg_v2(prog S, int n);
	// only to output a formula. Will not be included for gpt-alg().
	ld α, β, x;
	// difference table:
		// α = S[1] - S[0];
		// β = S[2] - S[1];
		// x = β - α;
};
class gpt_tools {
public:
	static ld gpt_alg_v0(prog data, int n);
};
class res_tools {
public:
	ld parr_res_v0(prog Ω);
};