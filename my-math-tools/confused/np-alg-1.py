def solve(prog, n):
    k = len(prog)  # Calculate k from the length of prog
    # Check if n is less than k
    if n < k:
        return prog[n]
    # Initialize the difference table with the given progression
    table = [[prog[i] for i in range(k)]]
    # Calculate the difference table
    for i in range(k-1):
        row = []
        for j in range(k-i-1):
            diff = table[i][j+1] - table[i][j]
            row.append(diff)
        table.append(row)
    # Calculate the nth term using the difference table
    term = table[k-1][0]
    for i in range(1, k):
        prod = 1
        for j in range(i):
            prod *= (n - j)
        term += (prod * table[k-i-1][0])
    return term

for i in range(100):
    print(solve([1,4,9],i))