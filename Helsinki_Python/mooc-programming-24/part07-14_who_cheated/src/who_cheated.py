# Write your solution here
import csv 
from datetime import datetime, timedelta


def load_start_times():
    time_format = "%H:%M"
    with open('start_times.csv') as file:
        start_times = {}
        for row in csv.reader(file, delimiter = ";"):
            start_times[row[0]] = datetime.strptime(row[1], time_format)
    return start_times

def load_submissions():
    time_format = "%H:%M"
    with open('submissions.csv') as file:
        submissions = {}
        for row in csv.reader(file, delimiter = ';'):
            if row[0] not in submissions:
                submissions[row[0]] = []
            row[-1] = datetime.strptime(row[-1], time_format)
            submissions[row[0]].append(row[1:])
    return submissions

def cheaters():
    start_times = load_start_times()
    submissions = load_submissions()
    difference = timedelta(hours = 3)
    cheaters = []
    for name, start_time in start_times.items():
        name_submissions = submissions[name]
        cheater = False
        for submission in name_submissions:
            end_time = submission[-1]
            if end_time - start_time > difference:
                cheater = True
                break
        if cheater:
            cheaters.append(name)
    return cheaters

if __name__ == '__main__':
    print(cheaters())