import random
from my_math_tools import MyMathTools

def generate_expression(deg):
    exp_list = [1]
    for i in range(1, deg+1):
        coeff = random.randint(-10, 10)
        exp_list.extend([coeff, i])
    return exp_list

def evaluate_expression(exp_list, n):
    result = 0.0
    for i in range(0, len(exp_list), 2):
        coeff = exp_list[i]
        exp = exp_list[i+1]
        term = coeff * (n ** exp)
        result += term
    return result

def format_expression(exp_list):
    terms = []
    for i in range(0, len(exp_list), 2):
        coeff = exp_list[i]
        exp = exp_list[i+1]
        term = f"{coeff}n^{exp}"
        terms.append(term)
    expression = " + ".join(terms)
    return expression

def run_tests():
    total_tests = 0
    passed_tests = 0
    failed_tests = []

    for deg in range(1, 101):
        base_sequence = generate_expression(deg)
        for _ in range(100):
            coeffs = base_sequence.copy()
            random.shuffle(coeffs)
            n = deg + 1
            expected_value = evaluate_expression(coeffs, n)
            expected_expression = format_expression(coeffs)

            nth_term = MyMathTools.NthTerm(coeffs)
            actual_value = nth_term.calculate_value_at_position(n)
            actual_expression = nth_term.generate_polynomial_expression()

            total_tests += 1
            if abs(actual_value - expected_value) < 10**-8:
                passed_tests += 1
            else:
                failed_tests.append({
                    'Coefficients': coeffs,
                    'Expected Value': expected_value,
                    'Actual Value': actual_value,
                    'Expected Expression': expected_expression,
                    'Actual Expression': actual_expression
                })

    print(f"Tests Passed: {passed_tests}/{total_tests}")
    if failed_tests:
        print("Failed Tests:")
        for test in failed_tests:
            print(test)

run_tests()
