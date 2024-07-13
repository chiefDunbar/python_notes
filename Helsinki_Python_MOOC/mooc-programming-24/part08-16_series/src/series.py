class Series:

    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        
    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)
    
    def average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0
            
    def __str__(self):
        line_one = f"{self.title} ({self.seasons} seasons)\n"
        line_two = f"genres: {', '.join(self.genres)}\n"
        line_three = f"{len(self.ratings)} ratings, average {self.average_rating():.1f} points" if self.ratings else "no ratings"
        return line_one + line_two + line_three

def minimum_grade(rating: float, series_list: list):
    return [series for series in series_list if series.average_rating() >= rating]

def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genres]
