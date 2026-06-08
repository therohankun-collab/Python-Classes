base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent (power): "))

result = 1

# Using a loop to calculate the power
for _ in range(exponent):
    result = result * base

print("Result:", result)