# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    
    if not employee.subordinates:
        return 0
    
    return len(employee.subordinates) + sum([count_subordinates(sub) for sub in employee.subordinates]) 