# Write your solution here
# Remember the import statement
from datetime import date

def list_years(dates: list):
    years = []
    for date in dates:
        years.append(date.year)
    return sorted(years)