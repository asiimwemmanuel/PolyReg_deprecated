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

def generate_expression(base_sequence):
    exp_list = base_sequence.copy()
    random.shuffle(exp_list)
    return exp_list

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

    for deg in degrees:
        base_sequence = generate_base_sequence(deg)
        for batch in range(batch_size):
            expression = generate_expression(base_sequence)
            progression = [evaluate_expression(expression, n) for n in range(1, deg + 2)]

            # Test with integer parameter
            start_time = time.time()
            mem_usage = memory_usage((evaluate_algorithm, (1, progression, "int")))
            execution_time = time.time() - start_time
            max_mem_usage = max(mem_usage)
            print(f"Degree: {deg}, Batch: {batch}, Parameter: int, "
                  f"Execution Time: {execution_time:.4f} sec, "
                  f"Max Memory Usage: {max_mem_usage:.2f} MiB")

            # Test with "exp" parameter
            start_time = time.time()
            mem_usage = memory_usage((evaluate_algorithm, ("exp", progression, "exp")))
            execution_time = time.time() - start_time
            max_mem_usage = max(mem_usage)
            print(f"Degree: {deg}, Batch: {batch}, Parameter: exp, "
                  f"Execution Time: {execution_time:.4f} sec, "
                  f"Max Memory Usage: {max_mem_usage:.2f} MiB")

            # Test with "graph" parameter
            start_time = time.time()
            mem_usage = memory_usage((evaluate_algorithm, ("graph", progression, "graph")))
            execution_time = time.time() - start_time
            max_mem_usage = max(mem_usage)
            print(f"Degree: {deg}, Batch: {batch}, Parameter: graph, "
                  f"Execution Time: {execution_time:.4f} sec, "
                  f"Max Memory Usage: {max_mem_usage:.2f} MiB")

# User input for test type
test_type = input("Choose test type (THOROUGH/QUICK): ")

# Run the tests
run_tests(test_type)
