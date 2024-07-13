# write your solution here
student_info = input('Student information: ')
exercise_data = input('Exercises completed: ')

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
        exercises[row[0]] =  col

for id, name in names.items():
    if id in exercises:
        print(f'{name} {sum(exercises[id])}')