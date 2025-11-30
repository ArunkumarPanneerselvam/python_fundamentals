'''
Use Case 3 (Bug Fixing): Logical and Comparison Operator Errors
The following code should determine voting eligibility, but it contains operator mistakes. Fix it.
Incorrect code:
age = input("Enter age: ")
 citizen = input("Are you an Indian citizen? (yes/no)")
if age > "18" and citizen = "yes":
 print("Eligible to vote")
 else:
 print("Not eligible")
Expected behavior:
•	Convert age to integer before comparison.
•	Only print "Eligible to vote" if age is 18 or above AND citizen input is "yes" (case-insensitive).
'''

age = input("Enter age: ")
citizen = input("Are you an Indian citizen? (yes/no)").lower()
if int(age) >= 18 and citizen == "yes":
 print("Eligible to vote")
else:
 print("Not eligible to vote")
