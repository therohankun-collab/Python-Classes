def calculate_discount():
    while True:
        try:
            
            original_price = float(input("Enter total bill amount: "))
            discount_percent = float(input("Enter discount percentage: "))

            if original_price < 0 or discount_percent < 0 or discount_percent > 100:
                raise ValueError("Inputs cannot be negative, and discount cannot exceed 100%.")

            discount_amount = original_price * (discount_percent / 100)
            final_price = original_price - discount_amount

        except ValueError as ve:
            print(f"Invalid input error: {ve}. Please enter valid positive numbers.\n")
        except ZeroDivisionError:
            print("Error: Division by zero encountered. Please check your values.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

        else:
            print("\n--- Bill Summary ---")
            print(f"Original Price : ${original_price:.2f}")
            print(f"Discount ({discount_percent}%) : -${discount_amount:.2f}")
            print(f"Final Payable Amount: ${final_price:.2f}")
            break  

        finally:
            print("Processing attempt complete.")

calculate_discount()