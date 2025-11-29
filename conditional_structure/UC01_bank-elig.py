'''
K. Conditional Structure

Use Case 1: Banking Eligibility Check
Write a program that asks the user for:
•	Age
•	Monthly income

Conditions:
•	If age < 18: print "Not eligible for a bank account."
•	If age >= 18 and income < 15000: print "Eligible for basic savings account."
•	If age >= 18 and income between 15000 and 50000: print "Eligible for savings + salary account."
•	If age >= 18 and income > 50000: print "Eligible for premium account."

'''

age = int(input('Enter the age: '))
monthly_income = float(input('Enter the monthly income (eg., 10000: '))
if age < 18:
    print(f'Not eligible for a bank account.')
elif age >= 18 and monthly_income < 15000:
    print(f'Eligible for basic savings account.')
elif age >= 18 and (monthly_income >= 15000 and monthly_income < 50000):
    print(f'Eligible for savings + salary account.')
elif age >= 18 and monthly_income > 50000:
    print(f'Eligible for premium account.')
else:
    print("Invalid Input, try again.")
