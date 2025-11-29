'''
Use Case 3 (Bug Fixing): Nested Condition Logic Issue
Fix the following code so that it correctly determines whether the entered temperature indicates normal, fever, or high fever.
Incorrect code:
temp = input("Enter body temperature in Celsius: ")
if temp < "37":
 print("Normal temperature")
 elif temp > "37" and temp < "39":
 print("Fever")
 else
 print("High fever")
Expected behavior:
•	Convert temperature to float before comparison.


•	Conditions should print:
 Normal temperature (less than 37)
 Fever (between 37 and 39)
 High fever (39 and above)
'''

temp = float(input("Enter body temperature in Celsius: "))
if temp < 37:
 print("Normal temperature")
elif temp >= 37 and temp < 39:
 print("Fever")
else:
 print("High fever")
