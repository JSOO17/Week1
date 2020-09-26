import csv

def ignore_first(reader):
    data = list(reader)
    data.pop(0)
    return data


def field_count(field, filter):
    """
        Filter into one column

        @field: field to filter

        @filter: phrase to filter
    """
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = csv.reader(f)
            count = 0
            for row in reader:
                if(row[field] == filter):
                    count = count + 1
            print("There are {0} {1}".format(count, filter))
    except UnicodeDecodeError:
        print("could not fetching")
    except TypeError:
        print("Field is Integer and Filter is String")


def less_criticized():
    """
        Get top 10 movies less criticized
    """
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
            movies_less = []
            for row in reader:
                if(row[2]):
                    movies_less.append({ "name" : row[11], "num_critic_for_users" : int(row[2])}) 
            new_list = sorted(movies_less, key=lambda i: i['num_critic_for_users'])
            topTenList = new_list[:10]
            top = 0
            print("Top 10 Movies less criticized \n")
            for movie in topTenList:
                top = top + 1
                print("Top {0} is {1} with {2}".format(top, movie["name"], movie["num_critic_for_users"]))
    except UnicodeDecodeError:
        print("could not fetching")


def longest_duration():
    """
        Get top 10 movies more duration
    """
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
            movies_longest = []
            for row in reader:
                if(row[3]):
                    movies_longest.append({ "name" : row[11], "duration" : int(row[3])}) 
            new_list = sorted(movies_longest, key=lambda i: i['duration'], reverse=True)
            topTenList = new_list[:20]
            top = 0
            print("\nTop 20 Movies longest-running duration \n")
            for movie in topTenList:
                top = top + 1
                print("Top {0} is {1} with {2}".format(top, movie["name"], movie["duration"]))
    except UnicodeDecodeError:
        print("could not fetching")


def raised_more_money():
    """
        raised more money
    """
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
            movies_raised = []
            for row in reader:
                if(row[8]):
                    movies_raised.append({ "name" : row[11], "gross" : int(row[8])}) 
            new_list = sorted(movies_raised, key=lambda i: i['gross'], reverse=True)
            topTenList = new_list[:5]
            top = 0
            print("\nTop 20 Movies raised more money \n")
            for movie in topTenList:
                top = top + 1
                print("Top {0} is {1} with {2}".format(top, movie["name"], movie["gross"]))
    except UnicodeDecodeError:
        print("could not fetching")


def least_money():
    """
        least money
    """
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
            movies_least = []
            for row in reader:
                if(row[8]):
                    movies_least.append({ "name" : row[11], "gross" : int(row[8])}) 
            new_list = sorted(movies_least, key=lambda i: i['gross'])
            topTenList = new_list[:5]
            top = 0
            print("\nThe top 5 movies that made the least money  \n")
            for movie in topTenList:
                top = top + 1
                print("Top {0} is {1} with {2}".format(top, movie["name"], movie["gross"]))
    except UnicodeDecodeError:
        print("could not fetching")


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
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
            movies_expend = []
            for row in reader:
                if(row[22]):
                    movies_expend.append({ "name" : row[11], "budget" : int(row[22])}) 
            new_list = sorted(movies_expend, key=lambda i: i['budget'])
            topTenList = new_list[:3]
            top = 0
            print("\nTop 3 movies that expend less money to be produced  \n")
            for movie in topTenList:
                top = top + 1
                print("Top {0} is {1} with {2}".format(top, movie["name"], movie["budget"]))
    except UnicodeDecodeError:
        print("could not fetching")


def years_movies_released():
    """
        What year was the one who had less and more movies released
    """
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
            years_list = (list(row[23] for row in reader))
            years_dicts = (list({"year": i, "movies_released": years_list.count(i)} for i in years_list))
            new_list = sorted(years_dicts, key=lambda i: i['movies_released'])
            year_less_movies = new_list[:1]
            print("The year {0} had less movies releaded with {1}".format(year_less_movies[0].get("year"), year_less_movies[0].get("movies_released")))
            new_list = sorted(years_dicts, key=lambda i: i['movies_released'], reverse=True)
            year_more_movies = new_list[:1]
            print("The year {0} had more movies releaded with {1}".format(year_more_movies[0].get("year"), year_more_movies[0].get("movies_released")))
            
    except UnicodeDecodeError:
        print("could not fetching")


def ranking_actors_performed():
    """
        ranking actors Number of movies where the actor performed
    """
    try:   
        with open('movie_metadata.csv', encoding="utf8") as f:
            reader = ignore_first(csv.reader(f))
            names_list = (list(row[10] for row in reader)) 
            names_for = list(names_list)
            names = []
            for name in names_for:
                if {"name_actor": name, "movies_performed": names_for.count(name)} not in names:
                    names.append({"name_actor": name, "movies_performed": names_for.count(name)})
                else:
                    names_list.remove(name)
            new_list = sorted(names, key=lambda i: i['movies_performed'], reverse=True)
            ranking_ten_list = new_list[:10]
            rank = 0
            print("\nRanking actors Number of movies where the actor performed \n")
            for actor in ranking_ten_list:
                rank = rank + 1
                print("Rank {0} is {1} with {2}".format(rank, actor["name_actor"], actor["movies_performed"]))
                
    except UnicodeDecodeError:
        print("could not fetching")



#field_count(field=0, filter=" Black and White")

#field_count(field=1, filter="Director")

#less_criticized()

#longest_duration()

#raised_more_money()

#least_money()

#expend_more_money()

#expend_less_money()

#years_movies_released()

ranking_actors_performed()