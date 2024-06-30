# Write your solution here
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
            temp = {}
            temp['task'] = int(row[1])
            temp['points'] = int(row[2])
            temp['time'] = datetime.strptime(row[3], time_format)
            submissions[row[0]].append(temp)
    return submissions

def final_points():
    points = {}
    start_times = load_start_times()
    submissions = load_submissions()

    for name, start_time in start_times.items():
        name_submissions = submissions[name]
        task_points = {}
        for submission in name_submissions:
            if submission['time'] - start_time <= timedelta(hours = 3):                   # if submission done in valid   
                if submission['task'] not in task_points:                       # if new task
                    task_points[submission['task']] = submission['points']      
                elif task_points[submission['task']] < submission['points']:    # if higher task points found    
                    task_points[submission['task']] = submission['points']
        total_points = 0
        for point in task_points.values():
            total_points += point
        points[name] = total_points 
    
    return points

if __name__ == '__main__':
    print(final_points())