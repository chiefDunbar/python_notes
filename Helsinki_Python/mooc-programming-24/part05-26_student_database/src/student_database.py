# Write your solution here
def add_student(students, student):
    if student not in students:
        students[student] = []

def print_student(students, student):
    if student in students:
        print(f'{student}: ')
        if len(students[student]) == 0:
            print(f' no completed courses')
            return
        print(f' {len(students[student])} completed courses:')
        average_grade = 0 
        for course in students[student]:
            print(f'  {course[0]} {course[1]}')
            average_grade += course[1]
        average_grade /= len(students[student])
        print(f' average grade {average_grade:.1f}')
    else:
        print(f'{student}: no such person in the database')

def add_course(students: dict, student: str, course: tuple):
    if student in students and course[1] != 0:
        for index, prev_course in enumerate(students[student]):
            if course[0] == prev_course[0]:
                if course[1] > prev_course[1]:
                    students[student][index] = course
                    return
                else:
                    return 
        students[student].append(course)


def summary(students: dict):
    print(f'students {len(students)}')
    max_courses = 0
    max_courses_student = ''
    for name, courses in students.items():
        if len(courses) > max_courses:
            max_courses = len(courses)
            max_courses_student = name
    print(f'most courses completed {len(students[max_courses_student])} {max_courses_student}')
    max_avg = 0
    max_avg_name = ''
    for name, courses in students.items():
        avg = 0
        for course in courses:
            avg += course[1]
        avg /= len(courses)
        if avg > max_avg:
            max_avg = avg
            max_avg_name = name
    print(f'best average grade {max_avg} {max_avg_name}')
        


if __name__ == '__main__':
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))
    print_student(students, "Peter")