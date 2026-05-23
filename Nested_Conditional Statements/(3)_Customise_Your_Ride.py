print("Select Your Ride:")
print("1. 2 Wheeler")
print("2. 4 Wheeler")

choice = int(input("Enter Your Choice: "))

if choice == 1:
    print("What Type Of 2 Wheeler? ")
    print("1. Motorcycle\n")
    print("2. Scooter\n")

    choice2 = int(input("Enter Your Choice: "))
    if choice2 == 1:
        print("You Have Selected Motorcycle")
    else:
        print("You Have Selected Scooter")

        print("What Fuel Does It Run On?")
        print("1. Petrol")
        print("2. Diesel")
        print("3. Electricity")
        choice4 = int(input("Enter Your Choice: "))
    if choice4 == 1:
        print("You Have Selected Petrol")
    elif choice4 ==2 :
        print("You Have Selected Diesel")
    else:
        print("You Have Selected Electricity")


elif (choice == 2):
    print("What Type Of 4 Wheeler? ")
    print("1. Sedan")
    print("2. Hatchback")
    print("3. SUV")
    print("4. Coupe")
    choice3 = int(input("Enter Your Choice: "))

    if choice3 == 1:
        print("You Have Selected Sedan")
    if choice3 == 2:
        print("You Have Selected Hatchback")
    if choice3 == 3:
        print("You Have Selected SUV")
    if choice3 == 4:
        print("You Have Selected Coupe")

        
        print("What Fuel Does It Run On?")
        print("1. Petrol")
        print("2. Diesel")
        print("3. Electricity")
        choice5 = int(input("Enter Your Choice: "))
    if choice5 == 1:
        print("You Have Selected Petrol")
    elif choice5 ==2 :
        print("You Have Selected Diesel")
    else:
        print("You Have Selected Electricity")
