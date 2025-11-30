'''
Use Case 3: Bug Fixing — Datatype Mismatch
The below code is intended to calculate total price, but it has datatype errors. Fix it.
Incorrect code:
item_name = input("Enter product name: ")
 price = input("Enter price per item: ")
 quantity = input("Enter quantity: ")
total_cost = price * quantity
print("You purchased " + quantity + " units of " + item_name)
 print("Total payable: " + total_cost)
Expected output after fixing:
Enter product name: Notepad
 Enter price per item: 35.50
 Enter quantity: 3
You purchased 3 units of Notepad
 Total payable: 106.5 INR
'''

item_name = input("Enter product name: ")
print(type(item_name))
price = input("Enter price per item: ")
print(type(price))
quantity = input("Enter quantity: ")
print(type(quantity))
total_cost = float(price) * int(quantity)
print("You purchased " + quantity + " units of " + item_name)
print(f"Total payable: {total_cost} INR")

