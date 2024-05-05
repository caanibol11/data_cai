from fastapi import FastAPI 
import pandas as pd

from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates") ## carpeta templates

@app.get("/",tags=["Página Principal"])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/funcion_uno', tags=['generos'])
async def PlayTimeGenre(genero: str):
    # Cargar los datos del archivo CSV (reemplaza 'data.csv' con tu archivo)
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
