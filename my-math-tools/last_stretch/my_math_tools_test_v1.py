import sys
import time
import random
from memory_profiler import memory_usage
from my_math_tools import MyMathTools

def generate_base_sequence(deg):
    base_sequence = [1]
    for i in range(1, deg + 2):
        coeff = deg + (1 - i) / 2
        base_sequence.append(coeff)
    return base_sequence

def generate_expression(base_sequence) -> float:
    exp_list = base_sequence.copy()
    random.shuffle(exp_list)
    return exp_list

def evaluate_expression(exp_list, n):
    result = 0.0
    for i in range(0, len(exp_list), 2):
        coeff = exp_list[i]
        exp = exp_list[i+1]
        term = coeff * (n ** exp)
        result += term
    return result

def evaluate_algorithm(method, progression, param_type):
    nth_term = MyMathTools.NthTerm(progression)
    if param_type == "int":
        result = nth_term.calculate_value_at_position(2)
    elif param_type == "exp":
        result = nth_term.generate_polynomial_expression()
    else:
        result = nth_term.plot_progression_graph()
    return result

def run_tests(test_type):
    degrees = list(range(1, 101))
    if test_type == "THOROUGH":
        batch_size = 10000
    else:
        batch_size = 1000

    passed_tests = 0
    total_tests = 0
    failed_tests = []

    for deg in degrees:
        base_sequence = generate_base_sequence(deg)
        for batch in range(batch_size):
            expression = generate_expression(base_sequence)
            progression = [evaluate_expression(expression, n) for n in range(1, deg + 2)]

            # Test with integer parameter
            expected_int = evaluate_algorithm(1, progression, "int")
            actual_int = evaluate_algorithm(1, progression, "int")
            if abs(actual_int - expected_int) > 1e-8:
                failed_tests.append((deg, batch, "int", expected_int, actual_int))
            else:
                passed_tests += 1
            total_tests += 1

            # Test with "exp" parameter
            expected_exp = evaluate_algorithm("exp", progression, "exp")
            actual_exp = evaluate_algorithm("exp", progression, "exp")
            if any(abs(e - a) > 1e-8 for e, a in zip(expected_exp, actual_exp)):
                failed_tests.append((deg, batch, "exp", expected_exp, actual_exp))
            else:
                passed_tests += 1
            total_tests += 1

            # Test with "graph" parameter
            expected_graph = evaluate_algorithm("graph", progression, "graph")
            actual_graph = evaluate_algorithm("graph", progression, "graph")
            # Add graph comparison logic here
            if graph_comparison_logic(expected_graph, actual_graph):
                failed_tests.append((deg, batch, "graph", expected_graph, actual_graph))
            else:
                passed_tests += 1
            total_tests += 1

    # Export failed tests to a log file
    with open("failed_tests.log", "w") as log_file:
        for test in failed_tests:
            deg, batch, param_type, expected, actual = test
            log_file.write(f"Degree: {deg}, Batch: {batch}, Parameter: {param_type}\n")
            log_file.write(f"Expected: {expected}\n")
            log_file.write(f"Actual: {actual}\n\n")

    # Print test results
    print(f"Tests Passed: {passed_tests}/{total_tests}")

# User input for test type
test_type = input("Choose test type (THOROUGH/QUICK): ")

# Run the tests
run_tests(test_type)