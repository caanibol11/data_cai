### MACHINE LEARNING OPERATIONS MLOPS

## DESCRIPCION DEL PROBLEMA
La plataforma multinacional de videojuegos STEAM solicita al departamente de Data Scientist, crear un modelo de recomendación de videojuegos para usuarios.
Para esto se disponibiliza 3 archivos datasets, los cuales se deben trabajar como parte de una ingeniería de datos, realizando un ETL y un EDA. Este análisis
debe ser visualizado por la herramienta FAST API y deployado en RENDER.

El proyecto  contiene 3 archivos en formato  JSON para desarrollar el análisis:

1. Australian_user_reviews.json es un dataset que contiene los comentarios que los usuarios realizaron sobre los juegos que consumen. También datos como
   recomendaciones del juego, emociones y  estadísticas para otros usuarios.
   También presenta el id del usuario que comenta con su url del perfil y el id del juego.

2. Australian_users_items.json es un dataset que contiene información sobre todos los juegos de usuarios y el tiempo de cada usuario  que jugó.

3. output_steam_games.json es un dataset que contiene datos de los juegos como títulos, el desarrollador, los precios, características técnicas, etiquetas, entre otros datos.

## DESARROLLO DEL PROYECTO
#ETL
* Se eliminaron campos  nulos y  duplicados 
* Se extrajo el campo "year" de la columna release_date
* Se eliminaron columnas no utilizadas.
* Se exportó para tener el dataset limpio y de acuerdo a las fuciones requeridas
* Se desanidaron columnas

#EDA 
* se uso la librería Seaborn para analizar graficos boxplot, barplot, stripplot, con los cuales se puede encontrar estadisticas, valores atípicos,
  distribución de las variables requeridas en las funciones.

# API - RENDER
* Se desarrolló el archivo main.py usando el software Visual Studio Code. En este archivo se configuró las funciones requeridas teniendo en cuenta
  el levantamiento del servidor local usando el framework FAST API. Se desarrollaron pruebas satisfacorias del funcioanmiento.
* Una vez se obtuvieron todos los archivos de python, se configuró el GIT HUB con el terminal y Git Bash
* Posteriormente se configuró em el sistema RENDER el deploy de la aplicación conectando con los archivos de GitHUB.

las funciones desarrolladas fueron las siguientes:

* def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
* def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado
* def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados
  con un análisis de sentimiento.
