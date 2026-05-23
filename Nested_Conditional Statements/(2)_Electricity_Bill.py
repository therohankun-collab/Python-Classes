units = int(input("Please Enter The Amount Of Units You Have Consumed (kWh): "))

if (units < 50):
    amount = units * 2.60
    surcharge = 25
    print(f"You have consumed", {units}, "kWh")

elif (units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
    print(f"You have consumed", {units}, "kWh")

elif (units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
    print(f"You have consumed", {units}, "kWh")

else: 
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75
    print(f"You have consumed", {units}, "kWh")
total = amount + surcharge
print("\n Electricity Bill is  %.2f"  %total)