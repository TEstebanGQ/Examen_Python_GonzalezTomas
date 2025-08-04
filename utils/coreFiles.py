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
    return cargarJson(RUTA_INGREDIENTES)

def obtenerCategoria() -> Dict:
    return cargarJson(RUTA_CATEGORIA)

def obtenerHamburguesa() -> Dict:
    return cargarJson(RUTA_HAMBURGUESAS)


def guardarChef(chef: Dict) -> None:
    guardarJson(RUTA_CHEF, chef)

def guardarIngredientes(ingrediente: Dict) -> None:
    guardarJson(RUTA_INGREDIENTES, ingrediente)

def guardarCategoria(categoria: Dict) -> None:
    guardarJson(RUTA_CATEGORIA, categoria)

def guardarHamburguesa(hamburguesa: Dict) -> None:
    guardarJson(RUTA_HAMBURGUESAS, hamburguesa)

def eliminarIngrediente(indice: int) -> None:
    ingredientes = obtenerIngredientes()
    if 0 <= indice < len(ingredientes):
        ingredientes.pop(indice)
        guardarIngredientes(ingredientes)

def eliminarChef(indice: int) -> None:
    chefs = obtenerChef()
    if 0 <= indice < len(chefs):
        chefs.pop(indice)
        guardarChef(chefs)

def eliminarCategoria(indice: int) -> None:
    categorias = obtenerCategoria()
    if 0 <= indice < len(categorias):
        categorias.pop(indice)
        guardarCategoria(categorias)

def eliminarHamburguesa(indice: int) -> None:
    hamburguesas = obtenerHamburguesa()
    if 0 <= indice < len(hamburguesas):
        hamburguesas.pop(indice)
        guardarHamburguesa(hamburguesas)