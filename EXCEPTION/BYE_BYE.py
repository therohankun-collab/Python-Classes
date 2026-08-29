valid = False
while not valid:
    try:
        n=int(input("Enter A Number: "))
        while n%2==0:

         print("Bye Bye")
        valid = True

    except ValueError:
        print("INVALID!")