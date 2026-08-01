def greet_customer():
    print("Welcome To The Lemonade Stand!")
    print("Fresh LEmonade, Made Just For You!")

greet_customer()

price_per_cup = float(input("Enter The Price Per Cup In Dollars:"))
cups_sold = int(input("Enter The Number Of Cups Sold:"))

def calculate_total(price, cups):
    total = price * cups
    return total 

total_cost = calculate_total(price_per_cup, cups_sold)

rounded_total = round(total_cost, 2)
print("Total Cost: ", rounded_total)

amount_paid = float(input("Enter The Amount Paid By The Customer: "))

def calculate_change(paid, total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

def thank_you_message(cups):
    if cups >= 5:
        return "Wow, A Big Order! Thank You So Much For Your Support!"
    else:
        return "Thanks For Stopping By The Stand!"

closing_message= thank_you_message(cups_sold)

print("")
print("===== LEMONADE STAND RECEIPT =====")
print("Price Per Cup: ", price_per_cup)
print("Cups Sold: ", cups_sold)
print("Total Cost: ", rounded_total)
print("Amount Paid: ", amount_paid)
print("Change Due: ", rounded_change)
print(closing_message)
print("Hope You Have A Nice Day!")
print("===================================")