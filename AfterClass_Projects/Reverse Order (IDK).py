# Get the number from the user
number = int(input("Enter a number: "))

# Handle negative numbers just in case
number = abs(number)

count = 0

# Special case for the number 0
if number == 0:
    count = 1
else:
    # Chop off the last digit one by one using a while loop
    while number > 0:
        number = number // 10  # This removes the last digit
        count += 1             # Add 1 to our digit count

print(f"Total digits: {count}")