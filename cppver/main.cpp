// work on the U.I. Make it more interactive
// write tests. tests are important, especially since this is math-y

#include "math_tools.h"

int main() {
    cout << "\n-----------------------------------------------------------------------------------------------------------------------------\n";
    cout << "\nThis program is meant to contain all my math functions and theorems I have compiled over the months.\n";
    cout << "It features:\n  1. A quadratic series analyser that can find the nth term in any real quadratic progression.\n  2. A parallel resistance analyser that can accurately calculate total parallel resistance via the law pertaining to the above\n";
    cout << "\nNOTE: If you wish to run the program again, simply click it again in file explorer or run it from the terminal\n\n";
    cout << "\n-----------------------------------------------------------------------------------------------------------------------------\n";
    cout << "\n:: Would you like to carry out Quadratic series analysis or Parallel resistors analysis?\n     Input 'Q' or 'P' respectively: ";
    char choice;
    cin >> choice;
    choice = toupper(choice);

    if(choice == 'Q') {

        // --------------------------------------input--------------------------------------
        prog quad_series(3);
        cout << "\n:: Input the first 3 terms in quadratic series:\n"; 
        for(int i = 0; i < 3; i++) {
            cout << "  > Term " << i+1 << ": ";
            cin >> quad_series[i];
        }
        // ----------------------------------------------------------------------------------

        // contructor must remain the same
        math_tools::quad_tools main_quad(quad_series[1]-quad_series[0], quad_series[2]-quad_series[1], (quad_series[2]-quad_series[1])-(quad_series[1]-quad_series[0]));

        // ----------------------printing standard generalisation----------------------------
        cout << "\n:: Nth term:\n    " << quad_series[0] << " + summation of (" << main_quad.x << "x ";
        (main_quad.α-main_quad.x >= 0) ? cout << "+ " : cout <<  "- ";
        cout << abs(main_quad.α-main_quad.x) <<  ") from x = 1 to n-1\n"; 
        // ----------------------------------------------------------------------------------

        // --------------------------------continuous prompts--------------------------------
        cout << "\n:: Input '0' to exit the program\n";
        int posn_to_find = 1;
        while(posn_to_find > 0) {
            cout << "    Which term would you like to find?: "; 
            cin >> posn_to_find;
            if(posn_to_find == 0)
                break;
            // Used get_quad_nth_v1_0() with O(1) instead of get_quad_nth_v0_0() with O(n). Watch for errors
            cout << "  > Term " << posn_to_find << ": " << main_quad.get_quad_nth_v1_0(quad_series, posn_to_find) << "\n";
        };
        cout << "\n:: program terminated\n";
        // ----------------------------------------------------------------------------------
    }

    else if(choice == 'P') {

        // --------------------------------------input--------------------------------------
        math_tools main_res;
        cout << "\n:: Input '0' to exit the program\n\n";
        int n = 1;
        while(n > 0) {
            cout << ":: How many resistors in parallel?: ";
            cin >> n;
            prog res(n);
            cout << "\n:: Input the resistance of each resistor:\n";
            for(int i = 0; i < n; i++) {
                cout << "  > Resistor " << i+1 << ": ";
                cin >> res[i];
            }
            cout << "\n:: Total resistance: " << main_res.parr_res_v0(res) << (n > 1 ? " ohms" : "ohm") << "\n\n";
        }
        cout << "\n:: program terminated\n";
        // ----------------------------------------------------------------------------------
        
    }
    return 0;
}