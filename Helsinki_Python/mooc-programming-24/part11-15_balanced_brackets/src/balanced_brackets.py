def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    if my_string[0] not in "([])":
        return balanced_brackets(my_string[1:])
    if my_string[-1] not in "([])":
        return balanced_brackets(my_string[:-1])

    if (my_string[0] == '(' or my_string[-1] == ')') and not (my_string[0] == '(' and my_string[-1] == ')'):
        return False
    if (my_string[0] == '[' or my_string[-1] == ']') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False

    return balanced_brackets(my_string[1:-1])

