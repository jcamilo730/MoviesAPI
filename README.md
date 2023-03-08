
# Documentacion del proyecto MoviesAPI

MoviesAPI es una API que permite realizar consultas a un catálogo de series y películas con información básica de las mismas (título, plataforma, año, sinopsis...).


Dentro del proyecto se encuentran dos carpetas, la de "Transformacion", en la que se encuentra lo relacionado a la transformacion del dataset original. Y la carpeta "moviesApi", donde se encuentran los archivos de la API ya terminada.
link api: https://5zqr2r.deta.dev

## 1. Transformacion:
Dentro de la carpeta "Datasets_original" se encuentran los datasets crudos como se recibieron, y en la carpeta "Datasets_Limpio" es donde se guardo el dataset limpio, despues de realizar las tranformaciones solicitadas.

En el archivo de jupyter notebook llamado "transformation.ipynb" se encuentra el codigo de python con el que se realizo la transformacion del dataset, cada transformacion se realizo en un bloque de codigo aparte y el ultimo bloque es para guardar el resultado en la ruta "Datasets_Limpio/platformsTitles.csv". Las transformaciones se les realizaron a los dataset por separado, por lo que al realizar la transformacion de uno, hay que volver a correr los bloques para realizar la transformacion del siguiente (la data ya transformada va quedando guardada dentro del mismo archivo platformsTitles.csv).

NOTA: dentro del mismo jupyter notebook "transformation.ipynb" esta especificado en que consistian cada una de las transformaciones.

  

## 2. MoviesAPI

En este directorio se encuentran los archivos de la API. En la carpeta "Dataset" esta el dataset limpio "platformsTitles.csv" que se subio DETA, y de donde la API obtiene la data para realizar las consultas.

Tambien se encuentran los archivos "main.py", "queries.py", y "requirements.txt" que se explicaran mas adelante. Las dependencias de python que se usaron para el desarrolo de la API fueron las siguientes:

-pandas

-fastapi

-numpy

-uvicorn (para el testeo local)

### 2.1 main.py

Es el main de la API donde se encuentran los endpoint creados para las consultas, cada uno de los metodos toma los parametros ingresados y llama a su vez al metodo correspondeinte de la clase "Queries" que esta en el archivo "queries.py"

### 2.2 queries.py

Es donde esta la clase "Queries" que contiene los metodos que realizan las consultas y retornan el resultado al main. Estas funciones consultan la informacion de la ruta "Datasets_Limpio/platformsTitles.csv" y va filtrando la data de acuerdo a los parametros ingresados.

### 2.3 requirements.txt

Es el txt con las dependencias usadas por la API. DETA utiliza esta informacion para poder hacer funcionar la API. Para esta API se especificaron las librerias de python: pandas y fastapi.

  

## 3. Funcionamiento de la API
A continuacion se explican las distintas consultas de la API junto con un ejemplo de su funcionamiento.

Link de la APPI: https://5zqr2r.deta.dev<br>

NOTA: Para una informacion aun mas detallada sobre el funcionamiento de la API se puede consultar el archivo [detailedAPI.md](https://github.com/jcamilo730/MoviesAPI/blob/437dc3c25978682f3074b91d0cbc70017b750dcf/detailedAPI.md)


### 3.1 /get_word_count={platform}_{keyword}
Get que retorna la cantidad de veces que aparece una keyword en los titulos de una plataforma.

A continuacion se esta realizando la busqueda de la palabra "love" en los titulos de la plataforma netflix:

    https://5zqr2r.deta.dev/get_word_count=netflix_love
output:

    "hay 196 titulos con la palabra love en la plataforma netflix"



### 3.2 /get_score_count=netflix_85_2010
Get que retorna la cantidad de películas de un cierto año con un puntaje mayor a X en una plataforma

A continuacion se esta realizando la busqueda de las peliculas del 2010 con un puntaje mayor a 85 en netflix:

    https://5zqr2r.deta.dev/get_score_count=netflix_85_2010

output:

    "hay 20 películas del 2010 en netflix con un puntaje mayor a 85"



### 3.3 /get_second_score=amazon
Get que retorna la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos. el resultado retorna un diccionario con todos los datos disponibles de la pelicula.

A continuacion se realiza la busqueda en la plataforma amazon:

    https://5zqr2r.deta.dev/get_second_score=amazon

output:

    id:
    	1: "as3367"
    show_id:
    	1: "s3367"
    type:
    	1: "movie"
    title:
    	1: "abilene town"
    director:
    	1: "edwin l. marin"
    cast
    	1: "ann dvorak, randolph scott, edgar buchanan, rhonda fleming, lloyd bridges"
    country {…}
    date_added {…}
    release_year:
    	1: 1946
    rating:
    	1: "13+"
    duration_int:
    	1: 89
    duration_type:
    	1: "min"
    listed_in:
    	1: "western"
    description:
    	1: "abilene, kansas, town marshal dan mitchell (scott) has managed to keep a tenuous peace by keeping saloons, gambling, and guns on one side of main street, and the stores, women, children, and farmers on the other side. violence and killings begin when homesteaders arrive in town in droves. dan convinces the shopkeepers to side with the homesteaders. to save his town, dan pits the saloon owners and cowboys against each other, resulting in a vicious bloodbath. in the midst of the chaos, dan must make a decision between the two women he loves."
    score:
    	1: 100



### 3.4 /get_longest=netflix_min_2016
Get que retorna los titulos que más duraron según el año, plataforma y tipo de duración especificado. retorna un diccionario con todos los datos disponibles de los titulos.

Esta busqueda arroja los titulos con mayor duracion en minutos del año 2016 en netflix:

    https://5zqr2r.deta.dev/get_longest=netflix_min_2016



### 3.5 /get_rating_count=18+
Get que retorna la cantidad de titulos por el rating de publico especificado.

Esta busqueda arroja la cantidad de titulos por el rating 18+:

    https://5zqr2r.deta.dev/get_rating_count=18+

output:

    "hay 1243 titulos con el rating 18+"
