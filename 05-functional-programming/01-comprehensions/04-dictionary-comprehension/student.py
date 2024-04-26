from movie import movies


def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}


def director_to_titles(movies):
    return {m.director: [movie.title for movie in movies if movie.director == m.director] for m in movies}

print(director_to_titles(movies))

