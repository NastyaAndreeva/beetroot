class Movie:
    def __init__(self, title, director, genre, release_year, duration, ratings):
        self.title = title
        self.director = director
        self.genre = genre
        self.ratings = ratings
        self.__release_year = release_year
        self.__duration = duration

    def display_movie_info(self):
        print("The title is: " + self.title)
        print(f"The director is: {self.director}")
        print("The genre is: " + self.genre)
        print(f"The ratings are: + {self.ratings}" )
        print("The release year is: " + str(self.__release_year))
        print("The duration is: " + self.__duration)

    def update_title(self, new_title):
        self.title = new_title

    def add_new_rating(self, new_rating):
        self.ratings.append(new_rating)

    def calculate_average_rating(self):
        return sum(self.ratings)/len(self.ratings)

movie_1 = Movie("Thor", "Director 1", "fantasy", 2019, "2 hours", [10, 9, 9.8, 8])
# movie_1.display_movie_info()
# print(movie_1.calculate_average_rating())
movie_1.add_new_rating(9.5)
movie_1.update_title("Love and Thunder")
movie_1.display_movie_info()




