import json
import os

ARCHIVO = "alumnos.json"

def cargar_datos()-> dict:
    if not os.path.exists(ARCHIVO):
        return{}
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f: 
            return json.load(f)
    
    except json.JSONDecodeError:
        return{}
    
def guardar_datos(datos:dict)-> None:
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)