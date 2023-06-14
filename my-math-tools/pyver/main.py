# turn into website and app: add ads to website
# post app on play store and all other platforms that engineers get tools (like worlfram alpha and the like) from
# give access to Victor, ask him to share it with his friends, who can add and give feedback - the one catalyst for its success.
# might even be able to use it to get to know people in research groups at those universities (if it grows and if it is relevant to the target consumer)

from gpt_tools import gpt
from res_tools import res

print("\n----------------------------------------------------------------------------------")
print("\nThis program is meant to contain all my math functions and theorems I have compiled over the months.")
print("It features:\n  1. A polynomial progression analyser that can find the nth term in any real progression of any degree.\n  2. A parallel resistance analyser that can accurately calculate total parallel resistance via the law pertaining to the above")
print("\nNOTE: To run the program again, simply click it again in file explorer or run it from the terminal\n")
print("----------------------------------------------------------------------------------")

choice = input("\n:: Would you like to carry out Real progression analysis or Parallel resistors analysis?\n    Input 'R or 'P' respectively: ").upper()

if choice == 'R':

	main_gpt = gpt()

	# -------------------------------------input----------------------------------------
	series = []
	# alternative: map and split method
	order = int(input("\n Number of terms known: "))
	for i in range(order):
		series.append(float(input(f":: Term at position {i+1}: ")))
	# ----------------------------------------------------------------------------------

	'''
	# -----------------------------standard generalisation------------------------------
	print(main_gpt.gpt_alg_v0(series, True))
	# ----------------------------------------------------------------------------------
	'''

	# --------------------------------continuous prompts--------------------------------
	if order > 0:
		print("\n:: Input '0' to close the program.")
		new_n = 1
		while new_n > 0:
			new_n = int(input("\n:: Position of term to find: "))
			print(f"  > Term {new_n}: {main_gpt.interpolate(series, new_n)}")
		print('\n:: program terminated')
	# ----------------------------------------------------------------------------------

elif choice == 'P':

	main_res = res()

	# ------------------------------input / continuous prompts--------------------------
	print("\n:: Input '0' to close the program.")
	res = []
	n = 1
	while n > 0:
		n = int(input("\n:: Number of resistors in parallel: "))
		# map and split method
		for i in range(n):
			res.append(int(input(f"  > Resistor {i+1}: ")))
		print(f"\n:: Total resistance: {main_res.parr_res_v0(res)}\n")
	print(":: program terminated")
	# ----------------------------------------------------------------------------------