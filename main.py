#Импортируем SQl
import sqlite3


def sqrequst_title(request_title):
    '''Показать фильм с названием ___'''
    list = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f""" SELECT title, country, release_year, listed_in, description 
                    FROM netflix
                    WHERE title = {request_title}
                    """
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            dict = {"title": x[0], "country": x[1], "release_year": x[2], "genre": x[3], "description": x[4]}
            list.append(dict)
        return list


def sqrequst_release_year(request_release_year_one, request_release_year_two):
    '''Показать фильмы, выпущенные в промежуток с __ по __'''
    list = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f""" SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {request_release_year_one} and {request_release_year_two}
                    LIMIT 100
                    """
        cursor.execute(query)
        result = cursor.fetchall()
    res = result
    for x in res:
        dict_one = {"title": x[0], "release_year": x[1]}
        list.append(dict_one)
    return list


def sqrequst_rating(rating):
    '''Показать фильмы по возрастному рейтингу'''
    list = []
    res = []
    dict = {"children": ["G"], "family": ["G", "PG", "PG-13"], "adult": ["R", "NC-17"]}
    for x in dict[rating]:
        with sqlite3.connect('netflix.db') as connection:
            cursor = connection.cursor()
            query = f""" SELECT title, rating, description
                        FROM netflix
                        WHERE rating = '{x}'
                        """
            cursor.execute(query)
            result = cursor.fetchall()
            res.append(result)
    for x in res:
        for y in x:
            dict = {"description": y[2], "rating": y[1], "title": y[0]}
            list.append(dict)

    return list


def sqrequst_genre(genre=""):
    '''Показать фильмы по жанру'''
    list = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f""" SELECT title, description
                    FROM netflix
                    WHERE listed_in LIKE '%{genre}%'
                    ORDER BY date_added DESC
                    LIMIT 10
                    """
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            dict_one = {"title": x[0], "description": x[1]}
            list.append(dict_one)
        return list


def sqrequst_actor(actor_one="", actor_two=""):
    '''Показать актеров, котоыре работают с парой более 2х раз (не справился с задачей)'''
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f""" SELECT "cast"
                        FROM netflix
                        WHERE "cast" LIKE "%{actor_one}%"
                        AND "cast" LIKE "%{actor_two}%"
                        AND "cast" != ""
                        """
        cursor.execute(query)
        result = cursor.fetchall()
        return result


def sqrequst_search(type="", year="", genre=""):
    '''Показать фильмы по определенным параметрам'''
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = f""" SELECT title, description
                        FROM netflix
                        WHERE type LIKE "%{type}%"
                        AND release_year LIKE "%{year}%"
                        AND listed_in LIKE "%{genre}%"

                        """
        cursor.execute(query)
        result = cursor.fetchall()
        return result


if __name__ == '__main__':
    print(sqrequst_search('Movie'))
