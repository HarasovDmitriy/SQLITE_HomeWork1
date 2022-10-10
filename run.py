# Импортируем библиотеки
from flask import Flask
import json
# Импортируем функции из main
from main import sqrequst_title, sqrequst_release_year, sqrequst_rating, sqrequst_genre

app = Flask(__name__)

@app.route("/movie/<title>")
def page_title(title):
    '''Показать фильмы с названием __'''
    results = sqrequst_title(title)
    return json.dumps(results)

@app.route("/movie/<year_one>/to/<year_two>")
def page_year(year_one, year_two):
    '''Показать фильмы, выпущенные в промежуток с __ по __'''
    results = sqrequst_release_year(year_one, year_two)
    return json.dumps(results)

@app.route("/rating/<rating>")
def page_rating(rating):
    '''Показать фильмы с возрастным рейтингом __'''
    results = sqrequst_rating(rating)
    return json.dumps(results)

@app.route("/genre/<genre>")
def page_genre(genre):
    '''показать фильмы по жанру __'''
    results = sqrequst_genre(genre)
    return json.dumps(results)



app.run()