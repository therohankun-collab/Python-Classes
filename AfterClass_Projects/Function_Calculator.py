# ── FUNCTIONS ──────────────────────────────────────────────────
# TODO: Define add(a, b) — return the sum of a and b
def add(a, b):
    return a + b


# TODO: Define subtract(a, b) — return a minus b
def subtract(a, b):
    return a - b


# TODO: Define multiply(a, b) — return a times b
def multiply(a, b):
    return a * b


# TODO: Define divide(a, b) — return a divided by b
def divide(a, b):
    return a / b


# ── MAIN PROGRAM ───────────────────────────────────────────────
print("=" * 36)
print("      🧮  FUNCTION CALCULATOR")
print("=" * 36)
print("Operations: add | subtract | multiply | divide")
print()

# Wrapped in a try/except ValueError block to handle invalid number inputs
try:
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    
    op = input("Choose operation (add, subtract, multiply, divide): ").strip().lower()

    
    if op == "add":
        result = add(num1, num2)
        print(f"Result: {result}")
    elif op == "subtract":
        result = subtract(num1, num2)
        print(f"Result: {result}")
    elif op == "multiply":
        result = multiply(num1, num2)
        print(f"Result: {result}")
    elif op == "divide":
      
        try:
            result = divide(num1, num2)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")
    else:
        print("Error: Unknown operation. Please enter add, subtract, multiply, or divide.")

except ValueError:
    print("Error: Please enter valid numeric values!")