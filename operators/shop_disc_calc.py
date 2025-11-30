'''
Use Case 2: Shopping Discount Calculation
Write a program that takes:
•	Original price (float)
•	Discount percent (int)


Using assignment and arithmetic operators, calculate:
 Discount amount = (price * discount_percent) / 100
 Final price = price - discount_amount
Print:
 Original price, discount applied, and final payable amount.
'''

original_price=float(input('Enter Original price: '))
discount_percent=int(input('Enter discount %: '))

discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount
print(f'Original price is {original_price}, discount {discount_amount} applied, and final payable amount is {final_price}.')

