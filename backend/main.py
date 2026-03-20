from fastapi import FastAPI
from llamar_api import buscar_noticias
from noticias_a_db import guardar_noticias



app = FastAPI()


@app.get("/listo")
def home():
    return {"status": "ok", "mensaje": "API funcionando 🚀"}


@app.post("/obtener_noticias")
def  obtener_noticias(query: str):

    if not query:
        return {"error": "query vacío"}

    lista_de_noticias = buscar_noticias(query)
    guardar = guardar_noticias(lista_de_noticias)

    return {
        "mensaje":"noticias agregadas",
        "cantidad": guardar
    }





