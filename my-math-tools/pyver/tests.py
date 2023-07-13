# export failed tests to a text file. include parameters given, expected and actual
import sys
import random
import time

from gpt_tools import gpt


# Helper function to generate a random progression with a given order and size
def generate_progression(order, size):
    base_seq = [float(i) for i in range(1, size+1)]
    progression = base_seq.copy()

    for i in range(1, order):
        diff_table = [progression[j] - progression[j-1]
                      for j in range(1, size)]
        progression = [progression[0]] + diff_table
        random.shuffle(diff_table)
        for j in range(1, size):
            progression[j] = progression[j-1] + diff_table[j-1]

    return progression


# Tests for gpt.gpt() function
def test_gpt(time_in_abundance: bool) -> None:
    print("Running tests for gpt.gpt()...")

    if time_in_abundance == True:
        # Thorough tests (60,000 progressions)
        num_tests = 0
        num_passed = 0
        for o in range(1, 1201):
            for i in range(25):
                size = random.randint(2, 1201)
                progression_list = [generate_progression(o, size) for _ in range(50)]

                # Randomize number of decimal places and place values in the progression
                for l, p in enumerate(progression_list):
                    dp = l
                    pv = 2 ** dp
                    progression_list[l] = [round(elem / pv, dp) for elem in p]

                for j in range(1, 51):
                    for n in range(1, size+1):
                        expected = progression_list[j-1][n-1]
                        actual = gpt.gpt(progression_list[j-1], n)
                        if abs(expected - actual) < 1e-8:
                            num_passed += 1
                        num_tests += 1

        print(f"Thorough tests complete: {num_passed}/{num_tests} tests passed")

    elif time_in_abundance == False:
        # Quick tests (6,000 progressions)
        num_tests = 0
        num_passed = 0
        for o in range(1, 1201):
            for i in range(24):
                size = random.randint(2, 1201)
                progression_list = [generate_progression(o, size) for _ in range(5)]

                # Randomize number of decimal places and place values in the progression
                for l, p in enumerate(progression_list):
                    dp = l
                    pv = 2 ** dp
                    progression_list[l] = [round(elem / pv, dp) for elem in p]

                for j in range(1, 6):
                    for n in range(1, size+1):
                        expected = progression_list[j-1][n-1]
                        actual = gpt.gpt(progression_list[j-1], n)
                        if abs(expected - actual) < 1e-8:
                            num_passed += 1
                        num_tests += 1

        print(f"Quick tests complete: {num_passed}/{num_tests} tests passed")


if __name__ == "__main__":
    choice = True if input("Do you want thorough or quick tests? (t/q): ").lower() == 't' else False
    start_time = time.time()
    test_gpt(choice)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")