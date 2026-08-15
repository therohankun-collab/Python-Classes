# 1. Bill Helper using Positional Arguments
def calculate_bill(subtotal, tax_rate, tip_percent):
    """Calculates total bill using subtotal, tax percentage, and tip percentage."""
    tax = subtotal * (tax_rate / 100)
    tip = subtotal * (tip_percent / 100)
    return subtotal + tax + tip

# 2. Seating Helper using Recursion
def count_seating_arrangements(people):
    """
    Calculates total ways to seat N people recursively (Factorial).
    Base case: 1 person = 1 way.
    Recursive case: people * count_seating_arrangements(people - 1)
    """
    if people <= 1:
        return 1  # Base case
    return people * count_seating_arrangements(people - 1)  # Recursive case


# --- PROGRAM EXECUTION WITH INPUTS ---

# Accessing and printing docstrings
print("--- DOCSTRINGS ---")
print("Bill Function Doc:", calculate_bill.__doc__)
print("Seating Function Doc:", count_seating_arrangements.__doc__)
print("-" * 30)

# Getting user inputs for the bill
subtotal_input = float(input("Enter subtotal amount: "))
tax_input = float(input("Enter tax percentage (e.g. 18): "))
tip_input = float(input("Enter tip percentage (e.g. 10): "))

# Calling calculate_bill with positional arguments
final_bill = calculate_bill(subtotal_input, tax_input, tip_input)
print("Total Bill:", round(final_bill, 2))

print("-" * 30)

# Getting user input for seating arrangements
people_input = int(input("Enter number of people to seat: "))

# Calling recursive seating function
total_arrangements = count_seating_arrangements(people_input)
print("Total seating arrangements:", total_arrangements)