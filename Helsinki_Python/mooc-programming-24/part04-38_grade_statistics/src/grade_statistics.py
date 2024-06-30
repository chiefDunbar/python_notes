# Write your solution here
def marks_input():
    exam_points = []
    exercise_numbers = []
    while True:
        string = input('Exam points and exercises completed: ')
        if string == '':
            break
        split = string.split()
        exam_points.append(int(split[0]))
        exercise_numbers.append(int(split[1]))
    return exam_points, exercise_numbers

def get_exercise_points(exercise_numbers):
    exercise_points = []
    for number in exercise_numbers:
        exercise_points.append(number // 10)
    return exercise_points

def get_grades():
    exam_points, exercise_numbers = marks_input()
    exercise_points = get_exercise_points(exercise_numbers)
    final_grades = []
    final_points = []
    for exam_point, exercise_point in zip(exam_points, exercise_points):
        final_point = exam_point + exercise_point
        final_points.append(final_point)
        if exam_point < 10:
            final_grades.append(0)
            continue
        elif final_point <= 14:
            final_grades.append(0)
        elif final_point <= 17:
            final_grades.append(1)
        elif final_point <= 20:
            final_grades.append(2)
        elif final_point <= 23:
            final_grades.append(3)
        elif final_point <= 27:
            final_grades.append(4)
        elif final_point <= 30:
            final_grades.append(5)
    return final_grades, final_points

def get_pass_percentage(grades):
    passed = 0
    for grade in grades:
        if grade != 0:
            passed += 1
    return passed / len(grades) * 100

def print_grade_distribution(grades):
    print('Grade distribution:')
    for index in range(5, -1, -1):
        print(f'  {index}: ' + '*' * grades.count(index))

def print_statistics():
    grades, points = get_grades()
    print('Statistics:')
    points_average = sum(points) / len(points)
    pass_percentage = get_pass_percentage(grades)
    print(f'Points average: {points_average:.1f}')
    print(f'Pass percentage: {pass_percentage:.1f}')
    print_grade_distribution(grades)

def main():
    print_statistics()

main()