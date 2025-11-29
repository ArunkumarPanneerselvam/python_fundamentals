'''
Use Case 2: Check room availability

 -Check room availability
    - If available:
        - If guest is VIP
            → Offer complimentary upgrade
        - Else if member 5+ years
            → Offer discount
        - Else
            → Standard price
    - Else:
        → Show: "No rooms available"
'''

from datetime import datetime

room_avail = 1
member_since = input("Enter your membership year (e.g., 2018): ")
guest_cat = input("Enter guest category (VIP/Regular): ").lower()

try:
    if room_avail == 1:
        joining_year = int(member_since)
        current_year = datetime.now().year

        if guest_cat == "vip":
            print("You are VIP member, You are eligible for a complimentary upgrade.")
        elif current_year - joining_year >= 5:
            print(f"You are our member since {joining_year}, eligible for 5+ year discount.")
        else:
            print("Standard price applies.")
    else:
        print("No rooms available.")
except Exception as errdesc:
    print("Invalid input:", errdesc)
