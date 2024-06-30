# Write your solution here
def find_movies(database: list, search_term: str):
    movies = []
    for movie in database:
        name = movie['name'].lower()
        search_term = search_term.lower()
        if name.find(search_term) != -1:
            movies.append(movie) 
    return movies