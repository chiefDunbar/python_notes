# Write your solution here
def find_words(search_term: str):
    has_dot = search_term.find('.')
    has_star = search_term.find('*')
    if has_dot == -1 and has_star == -1:
        return base_case(search_term)
    elif has_dot > -1:
        return dot_case(search_term)
    elif has_star > -1:
        return star_case(search_term)

def load_file():
    words = []
    with open('words.txt') as file:
        for row in file:
            words.append(row.strip())
    return words
    
def base_case(search_term: str):
    words = load_file()
    result = []
    for word in words:
        if word == search_term:
            result.append(word)
    return result

def dot_case(search_term: str):
    result = []
    words = load_file()
    for word in words:
        if len(word) == len(search_term):
            add_word = True
            for index, character in enumerate(search_term):
                if character == '.':
                    continue
                elif word[index] != character:
                    add_word = False
                    break
            if add_word:
                result.append(word)
    return result

def star_case(search_term: str):
    words = load_file()
    result = []
    # starts_with = search_term.startswith('*')
    # ends_with = search_term.endswith('*')
    # if starts_with:
    #     search_term = search_term[1:]
    #     for word in words:
    #         if word[::-1].find(search_term[::-1]) == 0:
    #             result.append(word)
    # if ends_with:
    #     search_term = search_term[:-1]
    #     for word in words:
    #         if word.find(search_term) == 0:
    #             result.append(word)
    look_for = search_term.replace('*', '')
    for word in words:
        if search_term.startswith('*') and word.endswith(look_for):
            results.append(word)
        if search_term.endswith('*') and word.startswith(look_for):
            results.append(word)
    return result

        
if __name__ == '__main__':
    print(find_words("cat"))

            
                    



