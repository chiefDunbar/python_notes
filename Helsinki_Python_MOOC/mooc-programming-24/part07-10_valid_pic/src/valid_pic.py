# Write your solution here
from datetime import datetime

def is_it_valid(pid: str):
    if len(pid) == 10:
        pid = '0' + pid
    if len(pid) > 11:
        return False
    day = int(pid[0:2])
    month = int(pid[3:4])
    year = int(pid[4:6])
    century = pid[6]
    pi = pid[7:10]
    control = pid[10]

    dictionary = {'+': 1800, '-': 1900, 'A': 2000}

    if century not in ['+', '-', 'A']:
        return False
    
    year += dictionary[century]
    
    try:
        dob = datetime(year, month, day)
    except ValueError:
        return False
    
    
    nine = int(pid[0:6] + pi)
    index = nine % 31
    character = "0123456789ABCDEFHJKLMNPRSTUVWXY"[index] 
    if character != control:
        return False
    
    return True

if __name__ == '__main__':
    print(is_it_valid('230827-906F1'))