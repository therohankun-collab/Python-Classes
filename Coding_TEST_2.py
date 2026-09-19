def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("Welcome To The Calculator! What Do You Want To Choose? \n 1) Addition 2) Subtraction 3) Multiplication 4) Division")

try:
    n = int(input("Enter Your Choice: "))

    if n == 1:
        d = float(input("Enter The First Number You Want To Add: "))
        e = float(input("Enter The Second Number You Want To Add: "))
        f = str(input("Want to add one more number? (y/n): "))
        if f.lower() == "y":
            g = float(input("Enter The Third Number You Want To Add: "))
            result = add(add(d, e), g)
        else:
            result = add(d, e)
        print("The Answer Is: ", result)

    elif n == 2:
        h = float(input("Enter The First Number You Want To Subtract: "))
        i = float(input("Enter The Second Number You Want To Subtract: "))
        j = str(input("Want to subtract one more number? (y/n): "))
        if j.lower() == "y":
            g = float(input("Enter The Third Number You Want To Subtract: "))
            result = subtract(subtract(h, i), g)
        else:
            result = subtract(h, i)
        print("The Answer Is: ", result)

    elif n == 3:
        a = float(input("Enter The First Number You Want To Multiply: "))
        b = float(input("Enter The Second Number You Want To Multiply: "))
        c = str(input("Want to Multiply one more number? (y/n): "))
        if c.lower() == "y":
            g = float(input("Enter The Third Number You Want To Multiply: "))
            result = multiply(multiply(a, b), g)
        else:
            result = multiply(a, b)
        print("The Answer Is: ", result)

    elif n == 4:
        x = float(input("Enter The First Number You Want To Divide: "))
        y = float(input("Enter The Second Number You Want To Divide: "))
        z = str(input("Want to Divide one more number? (y/n): "))
        
        try:
            if z.lower() == "y":
                g = float(input("Enter The Third Number You Want To Divide: "))
                result = divide(divide(x, y), g)
            else:
                result = divide(x, y)
            print("The Answer Is: ", result)
        except ZeroDivisionError:
            print("You Can't Divide By Zero.")

except ValueError:
    print("That Is Not A Number!")