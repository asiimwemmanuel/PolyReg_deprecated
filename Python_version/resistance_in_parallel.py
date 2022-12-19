# this program is to automatically calculate the total resistance for resistors in parallel connection, and is based on the original formula
n = int(input("How many resistors in parallel?: "))
print("Input the resistance of each resistor: ")
t_res = float(0.0)

for i in range(n):
    t_res += (1/float(input()))

t_res *= (1/(t_res**2))

print("Total resistance: %f" % t_res)