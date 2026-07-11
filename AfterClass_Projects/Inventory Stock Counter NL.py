
stock_data = {}

num_products = int(input("How many different types of products do you have? "))

p_count = 0
while p_count < num_products:
    product_name = input(f"\nEnter the name of product #{p_count + 1}: ")
    num_boxes = int(input(f"How many boxes of {product_name} do you have? "))
    
    boxes = []
    b_count = 0
    
    # Inner loop to get quantities for each box
    while b_count < num_boxes:
        qty = int(input(f"  Enter quantity for Box {b_count + 1}: "))
        boxes.append(qty)
        b_count += 1
        
    stock_data[product_name] = boxes
    p_count += 1

print("\nData entry complete!\n")

print("=== FINAL STOCK REPORT ===")
for product, boxes in stock_data.items():
    print(f"\nProduct: {product}")
    
    total_items = 0
    for idx, qty in enumerate(boxes):
        print(f"  -> Box {idx + 1}: {qty} items")
        total_items += qty
        
    print(f"  Total {product} Stock: {total_items}")