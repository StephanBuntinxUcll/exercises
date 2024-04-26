from movie import movies



def titles(movies):
    return [titles.title for titles in movies]

print(titles(movies))

def titles_and_years(movies):
    return [(movie.title, movie.year) for movie in movies]

# print(titles_and_years(movies))

def titles_and_actor_counts(movies):
    return[(movie.title , len(movie.actors)) for movie in movies]

# print(titles_and_actor_counts(movies))

def reverse_words(sentence):
    return " ".join([word[::-1] for word in (sentence.split(" "))])
     

print(reverse_words("hello world"))
