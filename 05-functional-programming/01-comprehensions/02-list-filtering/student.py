from movie import movies

def movies_from_year(movies, year):
    return [movie.title for movie in movies if movie.year == year]

# print(movies_from_year(movies, 2013))

def movies_with_actor(movies, actor):
    return [movie.title for movie in movies if actor in movie.actors]

# print(movies_with_actor(movies, 'Leonardo DiCaprio'))

def divisors(n):
     return [i for i in range(1, n+1) if n%i == 0 ]

# print(divisors(1))

print( 3%2)