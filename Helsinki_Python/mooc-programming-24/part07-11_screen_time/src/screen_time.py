# Write your solution here
from datetime import datetime, timedelta

file_name = input('Filename: ')
starting_date = datetime.strptime(input('Starting date: '), "%d.%m.%Y")
n_days = int(input('How many days: '))

print("Please type in screen time in minutes on each day (TV computer mobile):")

current_date = starting_date
end_date = current_date + timedelta(days = n_days - 1)

dictionary = {}
total_minutes = 0
while current_date <= end_date:
    screen_time = input(f"Screen time {current_date.strftime('%d.%m.%Y')}: ").split(' ')
    total_minutes += int(screen_time[0]) + int(screen_time[1]) + int(screen_time[2])
    dictionary[current_date.strftime("%d.%m.%Y")] = '/'.join(screen_time)
    current_date += timedelta(days = 1)

with open(file_name, "w") as file:
    file.write(f"Time period: {starting_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {total_minutes / n_days}\n")
    for day, minutes in dictionary.items():
        file.write(f"{day}: {minutes}\n")
    print(f"Data stored in file {file_name}")
