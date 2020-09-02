import pytest
from domainmodel.movie import Movie
from domainmodel.user import User




def test_rating_working():
    movie = Movie("Moana", 2016)

    user1 = User('a', 'pw12345')
    user2 = User('v', 'pw12345')
    user3 = User('b', 'pw12345')

    user1.watch_movie(movie)
    user2.watch_movie(movie)
    user3.watch_movie(movie)

    user1.vote_movie(movie, 8)
    assert movie.rating == 8
    user2.vote_movie(movie, 7)
    user3.vote_movie(movie, 5)

    assert movie.rating == 4.2
    assert movie.__repr__() == '<Movie Moana, 2016, 4.2>'


def test_rating_out_bound():
    movie = Movie("Moana", 2016)
    user1 = User('a', 'pw12345')
    user1.watch_movie(movie)
    user1.vote_movie(movie,100)
    assert movie.rating == 0
    user1.vote_movie(movie, -7)
    assert movie.rating == 0
    user1.vote_movie(movie, 'hello')
    assert movie.rating == 0

def test_voting_below_three():
    movie = Movie("Moana", 2016)

    user1 = User('a', 'pw12345')
    user2 = User('v', 'pw12345')

    user1.watch_movie(movie)
    user2.watch_movie(movie)

    user1.vote_movie(movie, 8)
    user2.vote_movie(movie, 7)

    assert movie.__repr__() == '<Movie Moana, 2016, No-Enough-Rating>'


def test_voting_before_watch():
    movie = Movie("Moana", 2016)

    user1 = User('a', 'pw12345')
    user2 = User('v', 'pw12345')
    user3 = User('b', 'pw12345')


    user1.vote_movie(movie, 8)
    user2.vote_movie(movie, 7)
    user3.vote_movie(movie, 5)

    assert movie.rating == 0.0

def test_change_rating():
    movie = Movie("Moana", 2016)

    user1 = User('a', 'pw12345')
    user2 = User('v', 'pw12345')
    user3 = User('b', 'pw12345')

    user1.watch_movie(movie)
    user2.watch_movie(movie)
    user3.watch_movie(movie)

    user1.vote_movie(movie, 8)
    assert movie.rating == 8
    user2.vote_movie(movie, 7)
    user3.vote_movie(movie, 5)

    assert movie.rating == 4.2

    movie.__change_rating__(3.0,1)
    assert movie.rating == 3.0



