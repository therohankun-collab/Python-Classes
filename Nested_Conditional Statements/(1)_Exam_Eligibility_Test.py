medical_cause = input("Do you have a medical cause? Y/N ").strip().upper()

if medical_cause == 'Y':
    print("You are allowed")
else:
    atten = int(input("Enter The Attendance Of The Student: "))
    if atten >= 75:
        print("You are allowed")
    else:
        print("Not allowed")