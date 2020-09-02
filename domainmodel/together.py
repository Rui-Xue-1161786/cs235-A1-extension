from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie


class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__colleague_list = []

    def add_actor_colleague(self, other):
        if not isinstance(other, Actor):
            pass
        self.__colleague_list.append(other)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__colleague_list:
            return True
        return False

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @actor_full_name.setter
    def actor_full_name(self,other):
        if other == "" or type(other) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = other.strip()

    @property
    def colleague_list(self):
        return self.__colleague_list


    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return other.__actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        if self.actor_full_name > other.actor_full_name:
            return False
        else:
            return True

    def __hash__(self):
        return hash(self.__actor_full_name)


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    @director_full_name.setter
    def director_full_name(self, director_full_name):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Director):
            return False
        return other.__director_full_name == self.__director_full_name

    def __lt__(self, other):
        if self.director_full_name > other.director_full_name:
            return False
        else:
            return True

    def __hash__(self):
        return hash(self.__director_full_name)


class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    @genre_name.setter
    def genre_name(self,other):
        if other == "" or type(other) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = other

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        return other.__genre_name == self.__genre_name

    def __lt__(self, other):
        if self.__genre_name > other.__genre_name:
            return False
        else:
            return True

    def __hash__(self):
        return hash(self.__genre_name)


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

    def __repr__(self):
        return f"<Movie {self._title}, {self._years}>"

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
        return(a+b)
















