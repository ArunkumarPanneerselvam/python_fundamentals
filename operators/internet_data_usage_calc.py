'''
I. Python Operators Usecases

Use Case 1: Internet Data Usage Calculator
Write a program that asks the user for:
•	Total monthly data limit (in GB)
•	Data used so far (in GB)


Calculate using arithmetic operators:
 Remaining data = limit - used
 Usage percentage = (used / limit) * 100
Print:
•	Remaining data
•	Usage percentage rounded to 2 decimals


If usage percentage is greater than or equal to 80, print:
 "Warning: High usage, consider upgrading your plan."
'''

monthly_data_limit=float(input('Enter your Total monthly data limit (in GB): '))
data_used=float(input('Enter Data used so far (in GB): '))

remaining_data=(monthly_data_limit - data_used)
usage_percentage = (data_used / monthly_data_limit) * 100

rounded_usage_percent=round(usage_percentage, 2)

print(f'Remaining Data (in GB): {remaining_data} GB')
print(f'Usage percentage rounded: {rounded_usage_percent} %')

if rounded_usage_percent>=80:
  print('Warning: High usage, consider upgrading your plan.')
