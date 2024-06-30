# Write your solution here
import urllib.request
import json
from math import floor

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read())
    result = []
    for dics in data:
        if dics['enabled'] == True:
            result.append((dics['fullName'], dics['name'], dics['year'], sum(dics['exercises'])))
    return result

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = json.loads(my_request.read())
    result = {}
    result["weeks"] = len(data)
    result["students"] = 0
    result["hours"] = 0
    exercises = 0
    for key, value in data.items():
        if value['students'] > result["students"]:
            result["students"] = value['students']
        result["hours"] += value['hour_total']
        exercises += value['exercise_total']
    result["hours_average"] = floor(result["hours"] / result["students"])
    result["exercises"] = exercises 
    result["exercises_average"] = floor(result["exercises"] / result["students"])
    return result
if __name__ == '__main__':
    print(retrieve_course('docker2019'))
    