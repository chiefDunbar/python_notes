# tee ratkaisu tänne
# tee ratkaisu tänne
# wwite your solution here
# write your solution here

student_info = input('Student information: ')
exercise_data = input('Exercises completed: ')
exam_data = input('Exam points: ')
course_info = input('Course information: ')

# course information
with open(course_info) as file:
    course = []
    for row in file:
        colon = row.strip().find(':')
        course.append(row[colon + 2:].strip())

# name information
with open(student_info) as file:
    names = {}
    for student in file:
        student = student.strip().split(';')
        if student[0] == 'id':
            continue
        names[student[0]] = f'{student[1]} {student[2]}'

# exercise points
with open(exercise_data) as file:
    exercises = {}
    for row in file:
        row = row.strip().split(';')
        if row[0] == 'id':
            continue
        col = []
        for c in row[1:]:
            col.append(int(c)) 
        exercises[row[0]] =  sum(col)

# exam points
with open(exam_data) as file:
    exams = {}
    for row in file:
        row = row.strip().split(';')
        if row[0] == 'id':
            continue
        col = []
        for c in row[1:]:
            col.append(int(c))
        exams[row[0]] = sum(col)

# string for results.txt
csv = ''
results = f"{course[0]}, {course[1]} credits"
results += f"\n{'=' * len(results)}"
results += f"\n{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}"
for id, name in names.items():
    if id in exercises  and id in exams: 
        points = int(exercises[id] * 10 / 40)  + exams[id]
        if points <= 14:
            grade = 0
        elif points <= 17:
            grade = 1
        elif points <= 20:
            grade = 2
        elif points <= 23:
            grade = 3
        elif points <= 27:
            grade = 4
        else:
            grade = 5
        results += f'\n{name:30}{exercises[id]:<10}{int(exercises[id] * 10 / 40):<10}{exams[id]:<10}{points:<10}{grade:<10}'
        csv += f'{id};{name};{grade}\n'
csv = csv.strip()
results = results.strip()
with open('results.txt', 'w') as file:
    file.write(results)

with open('results.csv', 'w') as file:
    file.write(csv)
