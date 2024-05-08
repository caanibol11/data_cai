from fastapi import FastAPI 
import pandas as pd

from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates") ## carpeta templates

@app.get("/",tags=["FUNCIONES PROYECTO MLOPS"])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/funcion_uno', tags=['generos'])
async def PlayTimeGenre(genero: str):
    # Cargar los datos del archivo CSV 
    df = pd.read_csv('./datasets/funcion_uno.csv')

    # Filtrar el DataFrame por género
    df_genre = df[df['genres'] == genero]

    # Agrupar por año de lanzamiento y calcular la suma de las horas jugadas para cada año
    horas_anio = df_genre.groupby('year')['playtime_forever'].sum()

    # Encontrar el año con la suma máxima de horas jugadas
    max_year = horas_anio.idxmax()

    # Devolver el resultado en un diccionario
    result = {"Año de lanzamiento con más horas jugadas para Género " + genero: max_year}
    return result


@app.get('/funcion_dos', tags=['generos'])
async def UserForGenre(genero: str):
    # Cargar los datos del archivo CSV 
    df = pd.read_csv('./datasets/funcion_dos.csv')

    # Filtrar el DataFrame por género
    df_genre = df[df['genres'] == genero]

    # Agrupar por usuario y año de lanzamiento, y calcular la suma de las horas jugadas para cada usuario y año
    horas_usuario_anio = df_genre.groupby(['user_id', 'year'])['playtime_forever'].sum()

    # Encontrar el usuario con la máxima suma de horas jugadas para el género dado
    max_usuario = horas_usuario_anio.groupby(level='user_id').sum().idxmax()

    # Filtrar las horas jugadas del usuario con la máxima suma
    horas_usuario_max = horas_usuario_anio.loc[max_usuario].reset_index()

    # Convertir los datos a un formato de lista de diccionarios
    horas_por_anio = horas_usuario_max.to_dict(orient='records')

    # Devolver el resultado en un diccionario
    result = {
       "Usuario con más horas jugadas para Género " + genero: max_usuario,
        "Horas jugadas": horas_por_anio
    }

    return result

@app.get('/funcion_tres', tags=['sentimiento'])
async def sentiment_analysis(año: int):
    # Cargar los datos del archivo CSV 
    df= pd.read_csv('./datasets/funcion_tres.csv')

    # Filtrar el DataFrame por el año de lanzamiento
    df_year = df[df['year'] == año]

    # Contar la cantidad de registros de reseñas categorizados con análisis de sentimiento
    sentiment_counts = df_year['sentiment_analysis'].value_counts()

    # Crear un diccionario con los recuentos de sentimientos
    result = sentiment_counts.to_dict()

    return result