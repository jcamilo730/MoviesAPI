from fastapi import FastAPI


app = FastAPI()

##retorna un texto con los links del reositorio documentacion
@app.get('/')
def index():
    result = Queries.index()
    return result

##Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get('/get_word_count={platform}_{keyword}')
def get_word_count(platform: str, keyword: str):
    result = Queries.get_word_count(platform, keyword)#obtengo el resultado llamando la funcion de la clase Queries
    return result

##Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get('/get_score_count={platform}_{score}_{year}')
def get_score_count(platform: str, score: int, year: int):
    result = Queries.get_score_count(platform, score, year)
    return result

##La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
@app.get('/get_second_score={platform}')
def get_second_score(platform: str):
    result = Queries.get_second_score(platform)
    return result

##Película que más duró según año, plataforma y tipo de duración
@app.get('/get_longest={platform}_{duration_type}_{year}')
def get_longest(platform: str, duration_type: str, year: int):
    result = Queries.get_longest(platform, duration_type, year)
    return result

##Cantidad de series y películas por rating
@app.get('/get_rating_count={rating}')
def get_rating_count(rating: str):
    result = Queries.get_rating_count(rating)
    return result
