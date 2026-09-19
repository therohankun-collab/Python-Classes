import math
import random

# --- PART 1: RANDOM MODULE FEATURES ---

# 1. Lucky Number Generator
lucky_number = random.randint(1, 100)
print(f"Your Lucky Number for today is: {lucky_number}")

# 2. Random Activity Chooser
activities = [
    "Read a book",
    "Go for a walk",
    "Play a game",
    "Code a project",
    "Listen to music",
]
chosen_activity = random.choice(activities)
print(f"Random Activity suggested for you: {chosen_activity}")

# 3. Number Guessing Game
print("\n--- Quick Number Guessing Game ---")
target_number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == target_number:
    print("Awesome! You guessed it right!")
else:
    print(f"Not quite! The correct number was {target_number}.")

# --- PART 2: MATH MODULE DEMO ---

print("\n--- Math Module Demos ---")

# math.ceil() - Rounds up
num_ceil = 4.2
print(f"math.ceil({num_ceil}) -> {math.ceil(num_ceil)}")

# math.floor() - Rounds down
num_floor = 4.8
print(f"math.floor({num_floor}) -> {math.floor(num_floor)}")

# math.copysign(x, y) - Copies sign of y to x
print(f"math.copysign(10, -5) -> {math.copysign(10, -5)}")

# math.fabs() - Absolute value (as float)
print(f"math.fabs(-7.5) -> {math.fabs(-7.5)}")

# math.gcd() - Greatest Common Divisor
a, b = 24, 36
print(f"math.gcd({a}, {b}) -> {math.gcd(a, b)}")