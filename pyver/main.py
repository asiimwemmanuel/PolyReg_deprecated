import math_tools

print("\n-----------------------------------------------------------------------------------------------------------------------------")
print("\nThis program is meant to contain all my math functions and theorems I have compiled over the months.")
print("It features:\n  1. A quadratic series analyser that can find the nth term in any real quadratic progression.\n  2. A parallel resistance analyser that can accurately calculate total parallel resistance via the law pertaining to the above")
print("\nNOTE: If you wish to run the program again, simply click it again in file explorer or run it from the terminal\n")
print("-----------------------------------------------------------------------------------------------------------------------------")
choice = input("\n:: Would you like to carry out Quadratic series analysis or Parallel resistors analysis?\n    Input 'Q' or 'P' respectively: ").upper()

if choice == 'Q':

    # --------------------------------------input--------------------------------------
    test_quad = math_tools.my_math()
    print("\n:: Input the first 3 terms in quadratic series:")
    quad_series = []
    for i in range(3): # map and split method
        quad_series.append(float(input(f"  > Term {i+1}: ")))
    # ----------------------------------------------------------------------------------
    
    # The variables decalred below b/c I can't use the variables declared in the function & don't want jargonish printf() parameters
    # Alternative: could make them attrubutes of the class and call them with test_quad
    test_α = quad_series[1] - quad_series[0]
    test_β = quad_series[2] - quad_series[1]
    test_x = test_β - test_α
    
    # ----------------------printing standard generalisation----------------------------
    print(f"\n:: Nth term:\n    {quad_series[0]:.2f} + summation of ({test_x:.2f}x {'+' if test_α-test_x >= 0 else '-'} {abs(test_α-test_x):.2f}) from x = 1 to n-1")
    # ----------------------------------------------------------------------------------

    # --------------------------------continuous prompts--------------------------------
    print("\n:: Input '0' to close the program.")
    posn_to_find = 1
    while posn_to_find > 0:
        posn_to_find = int(input("    Which term would you like to find?: "))
        print(f"  > Term {posn_to_find}: {test_quad.get_quad_nth_v0(quad_series, posn_to_find)}")
    print('\n:: program terminated')
    # ----------------------------------------------------------------------------------

elif choice == 'P':

    # --------------------------------------input--------------------------------------
    test_res = math_tools.my_math()
    print("\n:: Input '0' to close the program.")
    res = []
    n = 1
    while n > 0:
        n = int(input(":: How many resistors in parallel?: "))
        for i in range(n): # map and split method
            res.append(int(input(f"  > Resistor {i+1}: ")))
        print(f"\n:: Total resistance: {test_res.parr_res_v0(res)}\n")
    print("\n:: program terminated")
    # ----------------------------------------------------------------------------------