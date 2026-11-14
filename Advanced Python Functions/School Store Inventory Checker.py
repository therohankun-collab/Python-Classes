items = ["pencil", "eraser", "notebook", "sharpener", "glue"]
stock_counts = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_counts)}
print("Full Inventory: ", inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print("Items in stock: ", in_stock_items)

chosen_item = input("Which Item Do You Want To Buy? ")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print( "Uh-oh! Looks Like", chosen_item, "Is Out Of Stock! Stopping The Checker")
    exit()

prices = [10, 5, 40, 15, 20]
markup = int(input("Enter The Markup Amount To Add To Every Product's Price: "))

marked_up_prices = list(map(lambda p: p + markup, prices))
print("Marked-up Prices: ", marked_up_prices)

item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("The Price Of ", chosen_item, "After Markup Is :", chosen_price)

inventory[chosen_item] -= 1
print(chosen_item, "PURCHASED! Remaining Stock: ", inventory[chosen_item])

print("")
print("==========SCHOOL STORE INVENTORY CHECKER==========")
print("Item Bought: ", chosen_item)
print("Price Paid: ", chosen_price)
print("Updated Inventory: ", inventory)
print("Thank You For Shopping With Us! Have A Great Day!")
print("===================================================")