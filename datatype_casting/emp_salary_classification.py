Use Case 1 — Employee Salary Breakdown Using Numeric & String Types
Employee Salary Breakdown
a. Write a program that asks the user for:
•	employee_name (string)
•	base_salary (float)
•	hra_percent (integer)
•	bonus_amount (float)


B. Convert inputs to the correct datatype if required.
Calculate:
 HRA = base_salary * (hra_percent / 100)
 Total Salary = base_salary + HRA + bonus_amount
C. Print the output like this:
Employee: Arun

Base Salary: 40000.0

HRA @ 20%: 8000.0

Bonus: 5000.0

Total Salary Payable: ₹53000.0
'''

employee_name=str(input('Enter employee Name: '))
base_salary=float(input('Enter the base salary: '))
hra_percent=int(input('Enter hra percent: '))
bonus_amount=float(input("Enter bonus amount: "))

hra_amount = base_salary * (hra_percent / 100)
total_salary= base_salary + hra_amount + bonus_amount

print(f'''Employee:  {employee_name}

Base Salary: {base_salary}

HRA @ {hra_percent}%: {hra_amount}

Bonus: {bonus_amount}

Total Salary Payable: ₹{total_salary}
''')
