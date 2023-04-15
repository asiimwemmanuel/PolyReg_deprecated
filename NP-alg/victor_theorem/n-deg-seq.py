# Get nth term of the highest degree polynomial sequence

def get_nth(terms: list, want: int) -> int:
    nth = terms[0]
    matrix = [[None for j in terms] for i in terms]
    matrix[0] = terms
    count = len(terms) - 1
    for i in range(1, len(terms)):
        for j in range(count):
            matrix[i][j] = matrix[i-1][j+1] - matrix[i-1][j]
        count -= 1
    if want > len(terms):
        more = want-len(terms)
    # Recursion...
    def get_next(curr: int, degree: int) -> int:
        pass
    print(nth)
    return nth

get_nth([1,4,9],4)