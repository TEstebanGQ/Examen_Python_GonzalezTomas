import json
import os
from typing import Dict
from config import *

def cargarJson(ruta):
    if not os.path.exists(ruta):
        return [] 
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)  
            
    except (json.JSONDecodeError, FileNotFoundError):
        print(f" Archivo {ruta} corrupto o vacío. Se reiniciará.")
        return []  
    
def guardarJson(ruta, datos):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)  

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
def obtenerChef() -> Dict:
    return cargarJson(RUTA_CHEF)

def obtenerIngredientes() -> Dict:
    return cargarJson(RUTA_INGREDIEMTES)

def obtenerCategoria() -> Dict:
    return cargarJson(RUTA_CATEGORIA)

def obtenerHamburguesa() -> Dict:
    return cargarJson(RUTA_HAMBUGUESAS)


def guardarChef(chef: Dict) -> None:
    guardarJson(chef, RUTA_CHEF)

def guardarIngredientes(ingrediente: Dict) -> None:
    guardarJson(ingrediente, RUTA_INGREDIEMTES)

def guardarCategoria(categoria: Dict) -> None:
    guardarJson(categoria, RUTA_CATEGORIA)

def guardarHamburguesa(hamburguesa: Dict) -> None:
    guardarJson(hamburguesa, RUTA_HAMBUGUESAS)

