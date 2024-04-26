from movie import movies

def movie_count(movies, director):
    return len([movie.title for movie in movies if movie.director == director])

# print(movie_count(movies, "Paul Thomas Anderson"))


def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies for actors in movie.actors if actors == actor ])

# print(longest_movie_runtime_with_actor(movies, 'Tom Cruise'))

def has_director_made_genre(movies, director, genre):
    return any([[movie.title for gen in movie.genres if gen == genre] for movie in movies if movie.director == director])

# print(has_director_made_genre(movies, 'Sergio Leone', 'D'))

def is_prime(n):
    return not any([ i for i in range(2,n) if n % i == 0])

print(is_prime(13))

