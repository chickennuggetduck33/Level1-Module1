class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':
    pass
    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    thephantommenace = Movie("the phantom menace", 3.9)
    attackoftheclones = Movie("attack of the clones", 4)
    anewhope = Movie("a new hope", 4.6)
    revengeofthesith = Movie("revenge of the sith", 4.8)
    theempirestrikesback = Movie("the empire strikes back", 4.8)
    returnofthejedi = Movie("return of the jedi", 4.7)
    theforceawakens = Movie("the force awakens", 3.2)
    thelastjedi = Movie("the last jedi", 2.2)
    theriseofskywalker = Movie("the rise of skywalker", 3.3)
    # TODO 2) Use the Movie class to get the ticket price of one of your movies.
    thephantommenace.get_ticket_price()
    # TODO 3) Instantiate a NetflixQueue object.
    idk = NetflixQueue()
    # TODO 4) Add your movies to the Netflix queue.
    idk.add_movie(thephantommenace)
    idk.add_movie(attackoftheclones)
    idk.add_movie(revengeofthesith)
    idk.add_movie(anewhope)
    idk.add_movie(theempirestrikesback)
    idk.add_movie(returnofthejedi)
    idk.add_movie(theforceawakens)
    idk.add_movie(thelastjedi)
    idk.add_movie(theriseofskywalker)
    # TODO 5) Print all the movies in your queue.
    idk.print_movies()
    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    waffle = idk.get_best_movie()
    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."

