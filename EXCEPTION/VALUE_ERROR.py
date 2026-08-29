try:
    number = int(input("Enter A Number: "))
    print(("The Number Entered Is ", number))

except ValueError as ex:
    print("Execption: ", ex)