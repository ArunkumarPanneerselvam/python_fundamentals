'''
Use Case 3 (Bug Fixing): Infinite Loop Issue
 Fix the code below so that it prints numbers from 1 to 10 and stops correctly.
Incorrect code:
i = 1
 while i <= 10:
 print(i)
Expected behavior:
 The program must increment i and stop when 10 is printed.
'''

i = 1
while i <= 10:
 print(i)
 i=i+1
