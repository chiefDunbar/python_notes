# Write your solution here
def filter_solutions():
    correct = []
    incorrect = []
    with open('solutions.csv') as file:
        for line in file:
            row = line
            row = row.strip().split(';')
            question = row[1]
            answer = 0
            plus = question.find('+')
            if question.find('+') != -1:
                answer = int(question[:plus]) + int(question[plus + 1:])
            else:
                minus = question.find('-')
                answer = int(question[:minus]) - int(question[minus + 1:])
            if answer == int(row[2]):
                correct.append(line.strip())
            else:
                incorrect.append(line.strip())

    with open('correct.csv', 'w') as file:
        for row in correct:
            file.write(f'{row}\n')
    with open('incorrect.csv', 'w') as file:
        for row in incorrect:
            file.write(f'{row}\n')

#filter_solutions()
