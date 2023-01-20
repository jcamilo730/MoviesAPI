import pandas as pd
import numpy as np


class Queries :

    ##index
    def index () :
        message = '''repositorio de github: https://github.com/jcamilo730/Proyecto_01_API.git'''
        return message

    ##Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
    def get_word_count(platform: str, keyword: str) -> str :
        df = pd.read_csv('Datasets/platformsTitles.csv', sep=';')
        df = df[['id','title']]#se seleccionan las columnas con las que se van a trabajar

        #se filtra la plataforma mediante una nueva columna
        df['platform'] = df['id'].apply(lambda platF : platF[:1])
        df = df[df['platform'] == platform[:1]]
        
        #se realiza la busqueda del keyword en los titulos y se cuentan
        count = 0
        for index, row in df.iterrows() :
            if keyword in row['title'] :
                count += 1

        #creo y retorno el mensaje con la respuesta
        result = f'hay {count} titulos con la palabra {keyword} en la plataforma {platform}'
        return result

    ##Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
    def get_score_count(platform: str, score: int, year: int) -> str :
        df = pd.read_csv('Datasets/platformsTitles.csv', sep=';')
        df = df[['id', 'type', 'score', 'release_year']]#se seleccionan las columnas con las que se van a trabajar

        #se filtra la plataforma mediante una nueva columna
        df['platform'] = df['id'].apply(lambda platF : platF[:1])
        df = df[df['platform'] == platform[:1]]

        df = df[df['type'] == 'movie']#se filtran las peliculas
        df = df[df['release_year'] == year]#se filtra por año
        df = df[df['score'] > score]#se filtra por el score
        count = len(df.index)#se cuentan la cantidad de peliculas

        #creo y retorno el mensaje con la respuesta
        result = f'hay {count} películas del {year} en {platform} con un puntaje mayor a {score}'
        return result


    ##La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
    def get_second_score(platform: str) :
        df = pd.read_csv('Datasets/platformsTitles.csv', sep=';')

        #se filtra la plataforma mediante una nueva columna
        df['platform'] = df['id'].apply(lambda platF : platF[:1])
        df = df[df['platform'] == platform[:1]]

        df= df[df['type'] == 'movie']#se filtra las que son peliculas
        df = df[df['score'] == df['score'].max()] #se filtra el puntaje maximo

        df.sort_values(by= 'title', inplace=True, ignore_index=True)#se ordena alfabeticamente
        df = df.fillna(np.nan).replace([np.nan], [None])#se remplasan los nan por none para la transformacion
        df = df.drop(columns = ['platform'])#elimino la columna platform creada anteriormente

        result = df[1:2].to_dict()#se selecciona la segunda pelicula y se trandforma a diccionario
        return result


    ##Película que más duró según año, plataforma y tipo de duración
    def get_longest(platform: str, duration_type: str, year: int) :
        df = pd.read_csv('Datasets/platformsTitles.csv', sep=';')
        
        #se filtra la plataforma mediante una nueva columna
        df['platform'] = df['id'].apply(lambda platF : platF[:1])
        df = df[df['platform'] == platform[:1]]

        df = df[df['release_year'] == year]#se filtra el año
        df = df[df['duration_type'] == duration_type]#se filtra el tipo de duracion
        df = df[df['duration_int'] == df['duration_int'].max()]#se filtran las de mayor duracion
        df = df.drop(columns = ['platform'])#elimino la columna platform creada anteriormente

        df = df.fillna(np.nan).replace([np.nan], [None])#se remplasan los nan por none para la transformacion
        df = df.to_dict()

        return df


    ##Cantidad de series y películas por rating
    def get_rating_count(rating: str) -> int :
        df = pd.read_csv('Datasets/platformsTitles.csv', sep=';')

        df = df[df['rating'] == rating]#se filtra el rating pedido
        count = len(df.index)#se cuenta la cantidad de registros

        #creo y retorno el mensaje con la respuesta
        result = f'hay {count} titulos con el rating {rating}'
        return result