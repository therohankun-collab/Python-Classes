actual_cost = float(input("Please Enter Actual Product Price:"))
sale_amount = float(input("Please Enter Sale Amount Price:"))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))

elif (actual_cost > sale_amount):
    amount1 = actual_cost - sale_amount 
    print("Total Loss = {0}" .format(amount1))

