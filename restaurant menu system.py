restaurant = {
    "menu": {},  # Stores menu items with price
    "orders": {}  # Stores customer orders
}

while True:
    print("\nWelcome to Restaurant Management System")
    print("1. Manager Side")
    print("2. Customer Side")
    print("3. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":  
        while True:
            print("\nManager Menu:")
            print("1. Add Item")
            print("2. Update Item")
            print("3. Remove Item")
            print("4. View Menu")
            print("5. Back to Main Menu")
            
            manager_choice = input("Enter your choice: ")
            
            if manager_choice == "1": 
                item = input("Enter item name: ")
                price = float(input("Enter price: "))
                restaurant["menu"][item] = price
                print(f"{item} added successfully!")

            elif manager_choice == "2":  
                item = input("Enter item name to update: ")
                if item in restaurant["menu"]:
                    price = float(input("Enter new price: "))
                    restaurant["menu"][item] = price
                    print(f"{item} updated successfully!")
                else:
                    print("Item not found!")

            elif manager_choice == "3": 
                item = input("Enter item name to remove: ")
                if item in restaurant["menu"]:
                    del restaurant["menu"][item]
                    print(f"{item} removed successfully!")
                else:
                    print("Item not found!")

            elif manager_choice == "4":  
                if restaurant["menu"]:
                    print("\nMenu:")
                    for item, price in restaurant["menu"].items():
                        print(f"{item}: ${price:.2f}")
                else:
                    print("Menu is empty!")

            elif manager_choice == "5":  
                break

            else:
                print("Invalid choice, try again!")

        choice = input("Do you want to enter more product ? press 'y' for yes and press 'n' for no : ")
        if choice == 'y' or choice == 'yes':
            status = True 
        else:
            status = False

    elif choice == "2":  
        while True:
            print("\nCustomer Menu:")
            print("1. View Menu")
            print("2. Place Order")
            print("3. View Order")
            print("4. Back to Main Menu")
            
            customer_choice = input("Enter your choice: ")
            
            if customer_choice == "1":  
                if restaurant["menu"]:
                    print("\nMenu:")
                    for item, price in restaurant["menu"].items():
                        print(f"{item}: ${price:.2f}")
                else:
                    print("Menu is empty!")

            elif customer_choice == "2":  
                if not restaurant["menu"]:
                    print("No items available to order!")
                    continue

                name = input("Enter your name: ")
                if name not in restaurant["orders"]:
                    restaurant["orders"][name] = []

                order_item = input("Enter item name to order: ")
                if order_item in restaurant["menu"]:
                    restaurant["orders"][name].append(order_item)
                    print(f"{order_item} added to your order!")
                else:
                    print("Item not found!")

            elif customer_choice == "3":  
                name = input("Enter your name: ")
                if name in restaurant["orders"] and restaurant["orders"][name]:
                    print("\nYour Order:")
                    for item in restaurant["orders"][name]:
                        print(f"- {item}")
                else:
                    print("No orders found!")

            elif customer_choice == "4":  
                break

            else:
                print("Invalid choice, try again!")
    
    elif choice == "3":  
        print("Thank you for using the Restaurant Management System!")
        break

    else:
        print("Invalid choice, try again!")