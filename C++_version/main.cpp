//this program mainly implements two functions:

// 1. ANALYSIS OF QUADRATIC SERIES*
// * to be soon succeeded by a program analysing series of varying orders, not just quadratic

// general formula (by me);
// for terms a, b, c in series with differences α for (a and b) and β (b and c) respectively, with the constant difference between α and β being γ,
// formally,
//     α = b-a
//     β = c-b
//     γ = β - α
// nth term = first_term + summation of (γx + α - γ) from x = 1 to x = n-1

// 2. ANALYSIS OF RESISTANCE IN PARALLEL

// general formula;
// for n resistors in parallel circuit, the reciprocal of the total resistance (1/Ωt) is the sum of the recciprocals of all constituting resistors
// formally,
//     (1/Ωt) = (1/Ω1) + (1/Ω2) + (1/Ω3) + ... + (1/Ωn)
// total_resistance = summation of (1/Ωx) from x = 1 to x = n
//NOTE: the idea of multiplying a number n by (1/n^2) helps in the implementation of analysis 2.

#include "math_tools.h"
#include <string.h>
typedef long double ld;

int main() {
    system("CLS");
    printf("Quadratic series analysis or Parallel resistors analysis? (Q/P): ");
    char c; //sam is not paying attention
    scanf("%c",&c);
    c = toupper(c);
    if(c == 'Q') {
        math_tools test_1;
        vector<float>quad_series;
        printf("Input the first 3 terms in quadratic series\n");
        for(int i = 0; i < 3; i++) {
            float temp_input;
            printf("Term %d: ", i+1);
            scanf("%f", &temp_input);
            quad_series.push_back(temp_input);
        }
        printf("\nnth term:\n%.4f + ∑ %.4fx ", quad_series[0], quad_series[2] - (2*quad_series[1]) - quad_series[0]); //b/c I can't use variables defined in a function
        (2*(-1*quad_series[0])-quad_series[2]-quad_series[1] >= 0) ? printf("+ "):printf("- ");
        printf("%.4f (from x = 1 to x = n-1)\n", abs(2*(-1*quad_series[0])-quad_series[2]-quad_series[1]));
        printf("\nInput '0' to exit the program\n");
        int choice = 1;
        while(choice != 0) {
            printf("Which term would you like to find?: ");
            scanf("%d", &choice);
            if(choice == 0)
                break;
            test_1.quad_series(quad_series, choice);
        }
        printf("program terminated\n");
    }
    else if(c == 'P') {
        math_tools test_2;
        printf("How many resistors in parallel?: ");
        int n;
        scanf("%d", &n);
        vector<float> res(n);
        printf("Input the Ω of each resistor:\n");
        for(int i = 0; i < n; i++) {
            printf("Resistor %d: ", i+1);
            scanf("%f", &res[i]);
        }
        printf("Total resistance in parallel: %f\n", test_2.parr_res(res));
    }
    return 0;
}