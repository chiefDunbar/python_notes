# wwite your solution here
# write your solution here
student_info = input('Student information: ')
exercise_data = input('Exercises completed: ')
exam_data = input('Exam points: ')

with open(student_info) as file:
    names = {}
    for student in file:
        student = student.strip().split(';')
        if student[0] == 'id':
            continue
        names[student[0]] = f'{student[1]} {student[2]}'

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
        print(f'{name} {grade}')