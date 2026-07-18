# Get the number from the user
number = int(input("Enter a number: "))

# Handle negative numbers just in case
number = abs(number)

count = 0

# Special case for the number 0
if number == 0:
    count = 1
else:

    while number > 0:
        number = number // 10  # This removes the last digit
        count += 1             

print(f"Total digits: {count}")