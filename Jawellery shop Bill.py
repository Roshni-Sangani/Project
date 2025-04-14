# KALYAN JWELLERS : 

name = input("Enter your name: ")
gender = input("Enter gender (M/F): ").upper()
age = int(input("Enter age: "))
product = input("Enter product: ").capitalize()
product_gram = float(input("Enter product gram: "))
gold_price_per_gram = 5752
making_charge_per_gram = 845
        
total_gold_price = product_gram * gold_price_per_gram

total_making_charges = product_gram * making_charge_per_gram

total_amount = total_gold_price + total_making_charges

total_purchase = total_amount

if gender == "M":
        if age > 65:
            if 200000 > total_purchase < 300000:
                discount_percentage = 20
            elif 300000 > total_purchase < 500000:
                discount_percentage = 30
            elif total_purchase > 500000:
                discount_percentage = 35
            else:
                discount_percentage = 0
        else:
            if 200000 > total_purchase < 300000:
                discount_percentage = 10
            elif 300000 > total_purchase < 500000:
                discount_percentage = 20
            elif total_purchase > 500000:
                discount_percentage = 25
            else:
                discount_percentage = 0
elif gender == "F":
        if age > 65:
            if 200000 > total_purchase < 300000:
                discount_percentage = 25
            elif 300000 > total_purchase < 500000:
                discount_percentage = 35
            elif total_purchase > 500000:
                discount_percentage = 40
            else:
                discount_percentage = 0
        else:
            if 200000 > total_purchase < 300000:
                discount_percentage = 10
            elif 300000 > total_purchase < 500000:
                discount_percentage = 20
            elif total_purchase > 500000:
                discount_percentage = 25
            else:
                discount_percentage = 0
else:
    print("Invalid gender entered.")


discount_amount = (total_gold_price * discount_percentage) / 100
    

total_net_amount = total_amount - discount_amount
    
    # Output the results
print("\n-------------------------------")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Product: {product}")
print(f"Product Gram: {product_gram} gm")
print(f"Current Gold Price (1 gm): ₹{gold_price_per_gram}")
print("\n-------------------------------")
print(f"Total Gold Price: ₹{total_gold_price}")
print("\n-------------------------------")
print(f"making charges (1 gram) : 845")
print(f"Making Charges (Total): ₹{total_making_charges}")
print("\n-------------------------------")
print(f"Total Amount (Gold + Making Charges): ₹{total_amount}")    
print("\n-------------------------------")
print(f"Discount Percentage: {discount_percentage}%")
print(f"Discount Amount: ₹{discount_amount}")    
print("\n-------------------------------")
print(f"Total Net Amount after Discount: ₹{total_net_amount}")