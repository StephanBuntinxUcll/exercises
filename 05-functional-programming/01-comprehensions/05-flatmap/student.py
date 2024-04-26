from movie import movies
from util import Card

def genres(movies):
    return { g for genre in movies for g in genre.genres}

# print(genres(movies))

def actors(movies):
    return { actor for movie in movies for actor in movie.actors}

# print(actors(movies))

def repeat_consecutive(xs, n):
    return [ i for i in xs for z in range(n)]

print( repeat_consecutive([1,2,3], 3))

def repeat_alternating(xs, n):
    return [z for z in xs*n]

# print( repeat_alternating([4,5,6], 3))

def cards(values, suits):
    return { Card(value, suit) for value in values for suit in suits}



