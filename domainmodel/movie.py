from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(
            self, title: str, years: int
    ):
        if title == "" or type(title) is not str:
            self._title = None
        else:
            self._title = title.strip()

        if type(int(years)) != int or years < 1900:
            self._years = None
        else:
            self._years = int(years)

        self._description: str = None
        self._director: Director = None
        self._actors: [Actor] = list()
        self._genres: [Genre] = list()
        self._runtime_minutes: int = None
        self._rating: float = 0.0
        self._rating_count = 0

    @property
    def rating(self) -> int:
        return self._rating

    @rating.setter
    def rating(self, number):
        new_total = self.rating * self._rating_count + number
        self._rating_count += 1
        self._rating = round((new_total) / float(self._rating_count),1)

    @property
    def rating_count(self) -> int:
        return self._rating_count

    @property
    def years(self) -> int:
        return self._years

    @years.setter
    def years(self, years):
        if type(int(years)) != int and years < 1900:
            self._years = None
        else:
            self._years = int(years)

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, other):
        if other == "" or type(other) is not str:
            self._title = None
        else:
            self._title = other.strip()

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, text):
        if text == "" or type(text) is not str:
            self._description = None
        else:
            self._description = text.strip()

    @property
    def director(self) -> Director:
        return self._director

    @director.setter
    def director(self, other):
        if not isinstance(other, Director):
            pass
        else:
            self._director = other

    @property
    def actors(self):
        return self._actors

    @actors.setter
    def actors(self, other):
        if type(other) == Actor:
            self._actors.append(other)

    @property
    def genres(self):
        return self._genres

    @genres.setter
    def genres(self, other):
        if type(other) == Genre:
            self._genres.append(other)

    @property
    def runtime_minutes(self) -> int:
        return self._runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, time):
        if type(time) != int or time < 0:
            raise ValueError
        else:
            self._runtime_minutes = time

    def add_actor(self, actor):
        if not isinstance(actor, Actor):
            pass
        elif actor not in self._actors:
            self._actors.append(actor)

    def remove_actor(self, actor):
        if not isinstance(actor, Actor):
            pass
        elif actor in self._actors:
            self._actors.remove(actor)

    def add_genre(self, genre):
        if not isinstance(genre, Genre):
            pass
        elif genre not in self._genres:
            self._genres.append(genre)

    def remove_genre(self, genre):
        if not isinstance(genre, Genre):
            pass
        elif genre in self._genres:
            self._genres.remove(genre)

    def __change_rating__(self, rating_number, number_of_cutting_count):
        if type(rating_number) == float and 0 < rating_number < 11:
            self._rating = rating_number
            if number_of_cutting_count <= self._rating_count and type(number_of_cutting_count) == int:
                self._rating_count -= number_of_cutting_count


    def __repr__(self):
        if self._rating_count >= 3:
            return f"<Movie {self._title}, {self._years}, Rating={self._rating}>"
        else:
            return f"<Movie {self._title}, {self._years}, No-Enough-Rating>"


    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return other._title == self._title and other._years == self._years

    def __lt__(self, movie):
        if self._title > movie.title:
            return False
        elif self._title == movie.title:
            if self._years > movie.years:
                return False
            elif self._years == movie.years:
                return False
            else:
                return True
        else:
            return True

    def __hash__(self):
        a = hash(self._title)
        b = hash(self._years)
        return (a + b)


