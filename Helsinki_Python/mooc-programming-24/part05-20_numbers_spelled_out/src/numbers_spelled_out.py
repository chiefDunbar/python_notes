# Write your solution here
def dict_of_numbers():
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    number_dict = {}
    
    for i in range(20):
        number_dict[i] = units[i]
    
    for i in range(20, 100):
        ten_unit = i // 10
        unit = i % 10
        if unit == 0:
            number_dict[i] = tens[ten_unit]
        else:
            number_dict[i] = f"{tens[ten_unit]}-{units[unit]}"
    
    return number_dict