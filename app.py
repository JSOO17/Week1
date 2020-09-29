import csv

def ignore_first(reader) -> list:
    data = list(reader)
    data.pop(0)
    return data


def initialize_reader() -> list:
    try:
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
    except UnicodeDecodeError:
        print("could not fetching")
    return reader


def field_count(field: int, filter: str):
    """
        Filter into one column

        ;field: field to filter

        ;filter: phrase to filter
    """
    reader = initialize_reader()
    count = 0
    for row in reader:
        if(row[field] == filter):
            count = count + 1
    print(f"There are {count} {filter}")


def less_criticized():
    """
        Get top 10 movies less criticized
    """
    reader = initialize_reader()
    movies_less = []
    for row in reader:
        if(row[2]):
            movies_less.append({"name": row[11], "num_critic_for_users": int(row[2])}) 
    new_list = sorted(movies_less, key=lambda i: i['num_critic_for_users'])
    topTenList = new_list[:10]
    top = 0
    print("Top 10 Movies less criticized \n")
    for movie in topTenList:
        top = top + 1
        print(f"Top {top} is {movie.get('name')} with {movie.get('num_critic_for_users')}")


def longest_duration():
    """
        Get top 10 movies more duration
    """
    reader = initialize_reader()
    movies_longest = []
    for row in reader:
        if(row[3]):
            movies_longest.append({"name": row[11], "duration": int(row[3])})
    new_list = sorted(movies_longest, key=lambda i: i['duration'], reverse=True)
    topTenList = new_list[:20]
    top = 0
    print("\nTop 20 Movies longest-running duration \n")
    for movie in topTenList:
        top = top + 1
        print(f"Top {top} is {movie.get('name')} with {movie.get('duration')}")


def raised_more_money():
    """
    raised more money
    """
    reader = initialize_reader()
    movies_raised = []
    for row in reader:
        if row[8]:
            movies_raised.append({"name": row[11], "gross": int(row[8])}) 
      
    new_list = sorted(movies_raised, key=lambda i: i['gross'], reverse=True)
    topTenList = new_list[:5]
    top = 0
    print("\nTop 20 Movies raised more money \n")
    for movie in topTenList:
        top = top + 1
        print(f"Top {top} is {movie.get('name')} with {movie.get('gross')}")


def least_money():
    """
        least money
    """
    reader = initialize_reader()
    movies_least = []
    for row in reader:
        if row[8]:
            movies_least.append({"name": row[11], "gross": int(row[8])}) 
    new_list = sorted(movies_least, key=lambda i: i['gross'])
    topTenList = new_list[:5]
    top = 0
    print("\nThe top 5 movies that made the least money  \n")
    for movie in topTenList:
        top = top + 1
        print(f"Top {top} is {movie.get('name')} with {movie.get('gross')}")


def expend_more_money():
    """
        expend more money
    """
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
            movies_expend = []
            for row in reader:
                if(row[22]):
                    movies_expend.append({ "name" : row[11], "budget" : int(row[22])}) 
            new_list = sorted(movies_expend, key=lambda i: i['budget'], reverse=True)
            topTenList = new_list[:3]
            top = 0
            print("\nTop 3 movies that expend more money to be produced  \n")
            for movie in topTenList:
                top = top + 1
                print("Top {0} is {1} with {2}".format(top, movie["name"], movie["budget"]))
    except UnicodeDecodeError:
        print("could not fetching")


def expend_less_money():
    """
        expend more money
    """
    reader = initialize_reader()
    movies_expend = []
    for row in reader:
        if(row[22]):
            movies_expend.append({"name": row[11], "budget": int(row[22])}) 
    new_list = sorted(movies_expend, key=lambda i: i['budget'])
    topTenList = new_list[:3]
    top = 0
    print("\nTop 3 movies that expend less money to be produced  \n")
    for movie in topTenList:
        top = top + 1
        print(f"Top {top} is {movie.get('name')} with {movie.get('budget')}")


def years_movies_released():
    """
        What year was the one who had less and more movies released
    """
    reader = initialize_reader()
    years_list = [row[23] for row in reader]
    years_dicts = [{"year": i, "movies_released": years_list.count(i)} for i in years_list]
    new_list = sorted(years_dicts, key=lambda i: i['movies_released'])
    year_less_movies = new_list[:1]
    print(f"The year {year_less_movies[0].get('year')} had less movies released with {year_less_movies[0].get('movies_released')}")
    new_list = sorted(years_dicts, key=lambda i: i['movies_released'], reverse=True)
    year_more_movies = new_list[:1]
    print(f"The year {year_more_movies[0].get('year')} had more movies released with {year_more_movies[0].get('movies_released')}")


def ranking_actors_performed():
    """
        ranking actors Number of movies where the actor performed
    """
    reader = initialize_reader()
    names_list = [row[10] for row in reader] 
    names_for = list(names_list)
    names = []
    for name in names_for:
        if {"name_actor": name, "movies_performed": names_for.count(name)} not in names:
            names.append({"name_actor": name, "movies_performed": names_for.count(name)})
        else:
            names_for.remove(name)
    new_list = sorted(names, key=lambda i: i['movies_performed'], reverse=True)
    ranking_ten_list = new_list[:10]
    rank = 0
    print("\nRanking actors Number of movies where the actor performed \n")
    for actor in ranking_ten_list:
        rank = rank + 1
        print(f"Rank {rank} is {actor.get('name_actor')} with {actor.get('movies_performed')}")


def ranking_actors_influence():
    """
        ranking actors social Media influence
    """
    reader = initialize_reader()
    actor_list = [{"name_actor": row[10], "number_influence": int(row[7])} for row in reader]
    actor_for = list(actor_list)
    actors = []
    for actor in actor_for:
        if actor.get('name_actor') not in (list(x.get('name_actor') for x in actors)):
            actors.append({"name_actor": actor.get('name_actor'), "number_influence": actor.get('number_influence')})
        else:
            actor_for.remove(actor)
    new_list = sorted(actors, key=lambda i: i['number_influence'], reverse=True)
    ranking_ten_list = new_list[:10]
    rank = 0
    print("\nRanking actors social Media influence \n")
    for actor in ranking_ten_list:
        rank = rank + 1
        print(f"Rank {rank} is {actor.get('name_actor')} with {actor.get('number_influence')} followers")


def ranking_best_movie():
    """
        ranking Best Movie
    """
    reader = initialize_reader()
    movie_list = [{"name_movie": row[11], "scored": float(row[25])} for row in reader]
    new_list = sorted(movie_list, key=lambda i: i["scored"], reverse=True)
    ranking_ten_list = new_list[:10]
    rank = 0
    print("\nRanking best movies \n")
    for movie in ranking_ten_list:
        rank = rank + 1
        print(f"Rank {rank} is {movie.get('name_movie')} with {movie.get('scored')}")


def search_by_tags(tags: list):
    """
        search by tags into names of movies
    """
    reader = initialize_reader()
    key_words = [{"movie": row[10], "key_words": row[16]} for row in reader]
    words = []
    for key_word in key_words:
        for tag in tags:
            key_words_iterable = key_word.get("key_words").split("|")
            if tag in key_words_iterable:
                if key_word not in words:
                    words.append(key_word)
    ten_list = words[:10]
    if ten_list:
        rank = 0
        text_tags = ", ".join(tags)
        print(f"\n Results search by tags {text_tags} \n")
        for movie in ten_list:
            rank = rank + 1
            print(movie.get("movie") + "\n")
    else:
        print("there aren´t results")


def genre_money(year: int, less: bool=True):
    """
        What movie genre raised more money per year?
    """
    reader = initialize_reader()
    genres_dicts = [] 
    for row in reader:
        if(row[23]):
            if(int(row[23]) == year):
                if(row[8]):
                    genres = row[9].split("|")
                    for genre in genres:
                        if genre not in list(x.get('genre') for x in genres_dicts):
                            genres_dicts.append({"genre": genre, "gross": int(row[8])})
                        else:
                            for genre_dict in genres_dicts:
                                if genre_dict.get("genre") == genre:
                                        genre_dict["gross"] = genre_dict.get("gross") + int(row[8])
    if genres_dicts:
        if less:
            new_list = sorted(genres_dicts, key=lambda i: i["gross"])
            print(f"\nThe genre raised less money in {year} is {new_list[0].get('genre')} with $ {new_list[0].get('gross')}\n")
        else:
            new_list = sorted(genres_dicts, key=lambda i: i["gross"], reverse=True)
            print(f"\nThe genre raised more money in {year} is {new_list[0].get('genre')} with $ {new_list[0].get('gross')}\n")


def top_actors():
    """
       Top five ranking of actors by performance and popularity
    """
    reader = initialize_reader()
    actor_list = [{"actor": row[10], "scored": (float(row[4]) + float(row[25])) / 2 } for row in reader if row[4] and row[25]]
    actors = []
    for actor in actor_list:
        if actor.get('actor') not in list(x.get('actor') for x in actors):
            actors.append({"actor": actor.get('actor'), "scored": actor.get('scored')})
        else:
            actor_list.remove(actor)       
    new_list = sorted(actors, key=lambda i: i['scored'], reverse=True)
    top_five = new_list[:5]

    if actors:
        print(" \n Top 5 the best actors \n")
        top = 0
        for actor in top_five:
            top = top + 1
            print(f"Top {top} is {actor.get('actor')} with {actor.get('scored')} scored")


def genre_like_most():
    """
       What movie genre does the public like most?
    """
    reader = initialize_reader()
    genres_dicts = [] 
    for row in reader:
        if(row[23]):
            genres = row[9].split("|")
            for genre in genres:
                if genre not in list(x.get('genre') for x in genres_dicts):
                    genres_dicts.append({"genre": genre, "scored": float(row[25])})
                else:
                    for genre_dict in genres_dicts:
                        if genre_dict.get("genre") == genre:
                            genre_dict["scored"] = genre_dict.get("scored") + float(row[25])

            if genres_dicts:
                new_list = sorted(genres_dicts, key=lambda i: i["scored"], reverse=True)
                print(f"\n The movie genre that people like the most is {new_list[0].get('genre')} \n")               


def top_reputation_directors():
    """
       Which are the top five best reputation directors?
    """
    reader = initialize_reader()
    director_list = [{
                        "director": row[1],
                        "scored": (float(row[4]) + float(row[25])) / 2
                    } for row in reader if row[4] and row[25]]
    directors = []
    for director in director_list:
        iterable = (list(x.get('director') for x in directors))
        if director.get('director') not in iterable:
            directors.append({
                                "director": director.get('director'),
                                "scored": director.get('scored')
                            })
        else:
            director_list.remove(director)
    new_list = sorted(
                        directors,
                        key=lambda i: i['scored'],
                        reverse=True
                    )
    top_five = new_list[:5]
    if directors:
        print(" \n Top 5 the best directors \n")
        top = 0
        for director in top_five:
            top = top + 1
            top_director = director.get("director")
            top_scored = director.get("scored")
            print(f"Top {top} is {top_director} with {top_scored} scored")


# field_count(field=0, filter=" Black and White")

# field_count(field=1, filter="Director")

# less_criticized()

# longest_duration()

# raised_more_money()

# least_money()

# expend_more_money()

# expend_less_money()

# years_movies_released()

# ranking_actors_performed()

# ranking_actors_influence()

# ranking_best_movie()

# search_by_tags(["future", "epic"])

# genre_money(2014)

# genre_money(2013, less=False)

# genre_like_most()

# top_reputation_directors()

# top_actors()