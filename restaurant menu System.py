products = {}  # Main dictionary to store product details

# Manager: Adding products to inventory
status = True

while True:
    print("\nWelcome to Restaurant Management System")
    print("1. Manager Side")
    print("2. Customer Side")
    print("3. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        while status:
            specification = {}  # Sub-dictionary for product details

            product_name = input("Enter product name: ").lower()
            product_qty = int(input("Enter quantity: "))
            product_price = int(input("Enter product price: "))

            if product_name in products:
                specification["qty"] = products[product_name]["qty"] + product_qty  
                specification["price"] = product_price  
            else:
                specification["qty"] = product_qty
                specification["price"] = product_price

            products[product_name] = specification

            print("\nCurrent Inventory:")
            for k, v in products.items():
                print(f"{k.capitalize()} | Qty: {v['qty']} | Price (1 pc): Rs. {v['price']}")

            choice = input("Do you want to add more products? (y/n): ").lower()
            if choice not in ('y', 'yes'):
                status = False

# Customer: Buying products
    elif choice == "2":
        while True:
            product_name = input("\nEnter the product name you want to buy: ").lower()

            if product_name not in products:
                print("Sorry, this product is not available.")
                continue

            print(f"Per pc price: Rs. {products[product_name]['price']}")
            
            product_qty = int(input("Enter the quantity you want: "))

            if product_qty > products[product_name]["qty"]:
                print("Sorry, not enough stock available.")
                continue

            total_price = products[product_name]["price"] * product_qty
            print(f"Total: {products[product_name]['price']} x {product_qty} = Rs. {total_price}")

            confirm = input("Do you want to proceed with the purchase? (y/n): ").lower()
            if confirm in ('y', 'yes'):
                products[product_name]["qty"] -= product_qty  
                print("Purchase successful! Thank you.")

            choice = input("Do you want to buy another product? (y/n): ").lower()
            if choice not in ('y', 'yes'):
                break

        print("\nFinal Inventory After Sales:")
        for k, v in products.items():
            print(f"{k.capitalize()} | Qty: {v['qty']} | Price (1 pc): Rs. {v['price']}")

    elif choice == "3":  
        print("Thank you for using the Restaurant Management System!")
        break

    else:
        print("Invalid choice, try again!")