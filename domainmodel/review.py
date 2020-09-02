from datetime import datetime

from domainmodel.movie import Movie


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        self._movie = movie
        self._review_text = review_text

        if isinstance(rating, int):

            if 1 < int(rating) < 10:
                self._rating = int(rating)
            else:
                self._rating = None
        else:
            self._rating = None

        self._timestamp = datetime.now()

    @property
    def movie(self):
        return self._movie

    @property
    def review_text(self):
        return self._review_text

    @property
    def rating(self):
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp

    def __repr__(self):
        return f"<Review {self._movie}, {self._review_text}, {self._rating}, {self._timestamp}>"

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return other._movie == self._movie and other._review_text == self._review_text \
               and other._rating == self._rating and other._timestamp == self._timestamp



