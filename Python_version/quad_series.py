# this program is to automate the analysis of quadratic series
# It will be succeeded with a program analysing sereies of varying orders, not just quadratic

# general formula (by me);
# for terms a, b, c in series with differences α and β for (a and b) and (b and c) respectively, with the constant difference between α and β being γ,
# formally,
#     α = b-a
#     β = c-b
#     γ = β - α
# nth term = first_term + summation of (γx + α - γ) from x = 1 to x = n-1
# further documentation is available in the theory section

series = [] #stores the values in the series
print("Please input the first 3 terms in quadratic series")

# input sequence
for _ in range(3):
    series.append(float(input(f"Term {_+1}: ")))

# initializing necessary variables
α = series[1] - series[0]
β = series[2] - series[1]
γ = β - α

print(f"\nnth term:\n{series[0]} + ∑ {γ}x {'+' if α-γ >= 0 else '-'} {abs(α-γ)} (from x = 1 to x = n-1)\n")

choice = 1
print("Input '0' to close the program\n")

while choice != 0:
    choice = int(input("Which term would you like to find?: "))
    if choice == 0:
        break
    sum = 0
    for i in range(1, choice):
        sum += float((γ*i)+α-γ)
    print(float(series[0]+sum))
print("program terminated")
# for p in range(6):
#     print(p)