def mathematical_progression_analysis(lst, param):
    order = len(lst) - 1

    if isinstance(param, int):
        if param <= len(lst):
            return lst[param - 1]
        else:
            n = param
            result = 0
            power = order

            for coefficient in lst:
                result += coefficient * (n ** power)
                power -= 1

            return result

    # elif isinstance(param, str):
    #     if param == "exp":
    #         coefficients = calculate_coefficients(lst)
    #         expression = format_polynomial_expression(coefficients)
    #         return expression

    #     elif param == "graph":
    #         coefficients = calculate_coefficients(lst)
    #         expression = format_polynomial_expression(coefficients)
    #         plot_graph(expression)

    # return None


for i in range(100):
    print(mathematical_progression_analysis([1,4,9], i))