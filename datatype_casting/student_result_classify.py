'''
Use Case 2: Student Result Classification
a. Write a program that takes marks as input (initially as a string).
B. Check if the value can be converted to float.
C. Then classify:
Marks >= 90 --> Outstanding
 Marks >= 75 --> Excellent
 Marks >= 50 --> Pass
 Marks < 50 --> Fail
D. If the input is not numeric, print:
 Invalid marks entered — Please provide numeric input.
'''

marks=input('Enter your mark: ')

marks=float(marks)
if marks>=90:
  grade="Outstanding"
elif marks>=75 and marks<90:
  grade="Excellent"
elif marks>=50 and marks<75:
  grade="Pass"
elif marks<50:
  grade="Fail"
else:
    print("Invalid input")
print(f"Grade classification: {grade}")
