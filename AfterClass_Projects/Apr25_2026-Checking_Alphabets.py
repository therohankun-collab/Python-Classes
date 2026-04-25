print("Hello!")
a = str(input("What's Your Name?"))
b = str(input("How's Your Day Going Today?"))
c = str(input("I Am", b, "To Hear That."))
print("Let's Go On With Our Alphabet Checker.")

d = str(input("Enter Your Alphabet:"))

for char in d:
    if char.isalpha():
        print(f"'{char}' is a alphabet")
    elif char.isdigit():
        print(f"'{char}' is a number.")
    elif char.isspace():
        print(f"'{char}' is a space.")
    else:
        print(f"'{char}' is a special character.")
    