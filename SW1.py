USD_TO_INR = 83.2      # 1 USD = 83.2 Indian Rupee
USD_TO_POUND = 0.79    # 1 USD = 0.79 Pound
USD_TO_YUAN = 7.29     # 1 USD = 7.29 Yuan

print("Enter dollar ($) (* to exit): ", end="")

while True:
    user_input = input().strip()
    
    if user_input == "*":
        print("Bye")
        break
    
    dollars = user_input.split("@")
    
    print("\n{:<12} {:<18} {:<18} {:<12}".format(
        "Dollar ($)", "Indian Rupee (R)", "British Pound (£)", "China (Y)"
    ))
    
    for d in dollars:
        try:
            d = float(d)  
            inr = d * USD_TO_INR
            pound = d * USD_TO_POUND
            yuan = d * USD_TO_YUAN
            print("{:<12} {:<18.2f} {:<18.2f} {:<12.2f}".format(d, inr, pound, yuan))
        except ValueError:
            print(f"Invalid input: {d}")
    
    print("\nEnter dollar ($) (* to exit): ", end="")
