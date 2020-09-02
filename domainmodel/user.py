from domainmodel.movie import Movie
from domainmodel.review import Review

class User:
    def __init__(self,username: str, password: str):
        if username == "" or type(username) is not str:
            self._username = None
        else:
            self._username = username.strip().lower()

        self._password = password
        self._watched_movies = []
        self._reviews = []
        self._time_spent_watching_movies_minutes: int = 0

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def watched_movies(self):
        return self._watched_movies

    @property
    def time_spent_watching_movies_minutes(self):
        return self._time_spent_watching_movies_minutes

    @property
    def reviews(self):
        return self._reviews

    def __repr__(self):
        return f"<User {self._username}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other._username == self._username

    def __lt__(self, other):
        if self._username > other._username:
            return False
        else:
            return True

    def __hash__(self):
        return hash(self._username + self._password)

    def watch_movie(self,movie):
        if not isinstance(movie, Movie):
            pass
        else:
            self._watched_movies.append(movie)
            if movie.runtime_minutes != None:
                if movie.runtime_minutes > 0:
                    self._time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self,review):
        if not isinstance(review, Review):
            pass
        else:
            self._reviews.append(review)

    def vote_movie(self, movie, vote_number: int):
        if not isinstance(movie, Movie):
            pass
        else:
            if movie not in self._watched_movies:
                pass
            else:
                if type(vote_number) == int:
                    if 0 < vote_number < 11:
                        movie.rating= float(vote_number)


