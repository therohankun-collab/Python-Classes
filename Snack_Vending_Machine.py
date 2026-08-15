def calculate_change(paid,price):
    change = paid - price
    return change

snack_price = 25
print("===== SNACK VENDING MACHINE =====")
print(f"This Snack Cost ${snack_price} units.")
print("Accepted Coins: 1, 5, 10, 25\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert A Coin 1, 5, 10, OR 25): "))

    if coin != 1 and coin  !=  5 and coin != 10 and coin != 25 :
     print("Invalid Coin, Try Again.\n")
     continue 

    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted} \n")
    if total_inserted >= snack_price:
     print("Enough Money Inserted.\n")
     break
change_due = calculate_change(total_inserted, snack_price)

print("Dispensing Your Snack. . .")

if change_due == 0:
   pass
else:
   print(f"Here Is Your Change: {change_due} units. ")

print("\n===== PURCHASE SUMMARY =====")
print("Snack Price: ", snack_price)
print("Coins Inserted: ", coins_inserted)
print("Total Paid: ", total_inserted)
print("Change Given: ", change_due)
print("==============================")
print("Thanks For Your Purchase!")