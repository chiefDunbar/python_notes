# Write your solution here
from datetime import datetime, timedelta

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

if year >= 2000:
    print("You weren't born yet on the eve of the new millennium.")
else:
    dob = datetime(year, month, day)
    difference  = datetime(1999, 12, 31) - dob 
    print(f"You were {difference.days} days old on the eve of the new millennium.")

