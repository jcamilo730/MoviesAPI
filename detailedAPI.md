# Documentacion MovieAPI

## GET	/get_word_count={platform}_{keyword}
Get que retorna la cantidad de veces que aparece una keyword en los titulos de una plataforma.
| Parametro | Tipo | Descripcion |
|--|--|--|
| platform | str | plataforma a buscar entre las siguientes:Amazon, Disney, Hulu, Netflix |
| keyword | str | la palabra a buscar en los titulos |

**En la variable {platform} la API solo leera la primera letra, asi que si lo desea puede realizar la busqueda solo con la letra inicial de la plataforma, o con el nombre completo*

### Ejemplo:
A continuación se esta realizando la busqueda de la palabra "love" en los titulos de la plataforma netflix.

    https://5zqr2r.deta.dev/get_word_count=netflix_love

Output:

    "hay 196 titulos con la palabra love en la plataforma netflix"

## GET	/get_score_count={platform}\_{score}_{year}
Get que retorna la cantidad de películas de un cierto año con un puntaje mayor a X en una plataforma
| Parametro | Tipo | Descripcion |
|--|--|--|
| platform | str | plataforma a buscar entre las siguientes: Amazon, Disney, Hulu, Netflix |
| score | int | el score con el que se quiere hacer la busqueda |
| year | int | el año de las peliculas que se quieren buscar |

**En la variable {platform} la API solo leera la primera letra, asi que si lo desea puede realizar la busqueda solo con la letra inicial de la pplataforma, o con el nombre completo*
### Ejemplo:
A continuación se esta realizando la busqueda de las peliculas del 2010 con un puntaje mayor a 85 en netflix.

    https://5zqr2r.deta.dev/get_score_count=netflix_85_2010

Output:

    "hay 20 películas del 2010 en netflix con un puntaje mayor a 85"

## GET	/get_second_score={platform}

Get que retorna la segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos. el resultado retorna un diccionario con todos los datos disponibles de la pelicula
| Parametro | Tipo | Descripcion |
|--|--|--|
| platform | str | plataforma a buscar entre las siguientes: Amazon, Disney, Hulu, Netflix |

**En la variable {platform} la API solo leera la primera letra, asi que si lo desea puede realizar la busqueda solo con la letra inicial de la pplataforma, o con el nombre completo*
### Ejemplo:
A continuación se realiza la busqueda en la plataforma amazon

    https://5zqr2r.deta.dev/get_second_score=amazon

Output:

    id:
        1:	"as3367"
    show_id:
        1:	"s3367"
    type:
        1:	"movie"
    title:
        1:	"abilene town"
    director:
        1:	"edwin l. marin"
    cast	
        1:	"ann dvorak, randolph scott, edgar buchanan, rhonda fleming, lloyd bridges"
    country	{…}
    date_added	{…}
    release_year:
        1:  1946
    rating:
        1:	"13+"
    duration_int:
        1:	89
    duration_type:
        1:	"min"
    listed_in:
        1:	"western"
    description:
        1:	"abilene, kansas, town marshal dan mitchell (scott) has managed to keep a tenuous peace by keeping saloons, gambling, and guns on one side of main street, and the stores, women, children, and farmers on the other side. violence and killings begin when homesteaders arrive in town in droves. dan convinces the shopkeepers to side with the homesteaders. to save his town, dan pits the saloon owners and cowboys against each other, resulting in a vicious bloodbath. in the midst of the chaos, dan must make a decision between the two women he loves."
    score:
        1:    100

## GET /get_longest={platform}\_{duration_type}_{year}

Get que retorna los titulos que más duraron según el año, plataforma y tipo de duración especificado. retorna un diccionario con todos los datos disponibles de los titulos
| Parametro | Tipo | Descripcion |
|--|--|--|
| platform | str | plataforma a buscar entre las siguientes: Amazon, Disney, Hulu, Netflix |
| duration_type | str | el tipo de duracion de los titulos a buscar, puede ser min o season |
| year | int | el año de los titulos a buscar |

**En la variable {platform} la API solo leera la primera letra, asi que si lo desea puede realizar la busqueda solo con la letra inicial de la pplataforma, o con el nombre completo*
### Ejemplo:
Esta busqueda arroja los titulos con mayor duracion en minutos del año 2016 en netflix

    https://5zqr2r.deta.dev/get_longest=netflix_min_2016


## GET /get_rating_count={rating}
Get que retorna la cantidad de titulos por el rating de publico especificado.
| Parametro | Tipo | Descripcion |
|--|--|--|
| rating | str | el rating de los titulos a buscar |

**Los ratings son los siguientes:*

g<br>
13+<br>
all<br>
18+<br>
r<br>
tv-y<br>
tv-y7<br>
nr<br>
16+<br>
tv-pg<br>
7+<br>
tv-14<br>
tv-nr<br>
tv-g<br>
pg-13<br>
tv-ma<br>
pg<br>
nc-17<br>
unrated<br>
16<br>
ages_16_<br>
ages_18_<br>
all_ages<br>
not_rate<br>
tv-y7-fv<br>
notrated<br>
ur<br>
### Ejemplo:
Esta busqueda arroja la cantidad de titulos por el rating 18+

    https://5zqr2r.deta.dev/get_rating_count=18+

Output:

    "hay 1243 titulos con el rating 18+"
