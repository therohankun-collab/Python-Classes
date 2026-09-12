try:
    def add():
     d = float(input("Enter The First Number You Want To Add: "))
     e = float(input("Enter The  Second Number You Want To Add: "))
     f = str(input("Want to add one for number? (y/n)"))
     if f == "y":
        g = float(input("Enter The Third Number You Want To Add: "))
     result_pre = d + e
     if f == "y":
        result_pre2 = d + e + g
     print("The Answer Is: ", result_pre)
     if f == "y":
         print("The Answer Is: ", result_pre2)
except ValueError:
    print("That Is Not A Number!")

try:
    def subtract():
     h = float(input("Enter The First Number You Want To Subtract: "))
     i = float(input("Enter The  Second Number You Want To Subtract: "))
     j = str(input("Want to subtract one more number? (y/n)"))
     if j == "y":
        g = float(input("Enter The Third Number You Want To Subtract: "))
     result_pre3 = h - i
     if j == "y":
        result_pre4 = h - i - j
     print("The Answer Is: ", result_pre3)
     if j == "y":
         print("The Answer Is: ", result_pre4)
except ValueError:
    print("That Is Not A Number!")

try:
    def multiply():
     a = float(input("Enter The First Number You Want To Multiply: "))
     b = float(input("Enter The  Second Number You Want To Multiply: "))
     c = str(input("Want to Multiply one more number? (y/n)"))
     if c == "y":
        g = float(input("Enter The Third Number You Want To Multiply: "))
     result_pre5 = a*b
     if c == "y":
        result_pre6 = a*b*c
     print("The Answer Is: ", result_pre5)
     if c == "y":
         print("The Answer Is: ", result_pre6)
except ValueError:
    print("That Is Not A Number!")

try:
    def divide():
     x = float(input("Enter The First Number You Want To Divide: "))
     y = float(input("Enter The  Second Number You Want To Divide: "))
     z = str(input("Want to Divide one more number? (y/n)"))
     if z == "y":
        g = float(input("Enter The Third Number You Want To Divide: "))
     result_pre7 = x/y
     if z == "y":
        result_pre8 = x/y/z
     print("The Answer Is: ", result_pre7)
     if z == "y":
         print("The Answer Is: ", result_pre8)
     if z == "n":
       print("OK. Hope You Have A Great Day!")
except ValueError:
    print("That Is Not A Number!")
except ZeroDivisionError:
   print("You Can't Divide By Zero. The Anser To Any Division By Zero No Zero.")

print("Welcome To The Calculator! What DO You Want To Choose? \n 1) Addition 2) Subtraction 3) Multiplication 4) Division")
n = int(input("Enter Your Choice: "))
if n == 1:
      add
if n == 2:
        subtract
if n == 3:
        multiply 
if n == 4:
        divide
    


