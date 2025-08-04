import os
RUTA_CHEF = 'data/chefs.json'
RUTA_INGREDIENTES = 'data/ingredientes.json'
RUTA_CATEGORIA = 'data/categorias.json'
RUTA_HAMBURGUESAS = 'data/hamburguesas.json'

TIPO_DE_ELEMENTOS = {
    'chef':{
        "nombre": "Chef",
        'plural': 'chefs',
        'ruta': RUTA_CHEF,
        "especialidad": "comida"
    },
    'ingrediente':{
        "nombre": "ingrediente",
        'plural': 'ingredientes',
        'ruta': RUTA_INGREDIENTES,
        "descripcion": "Pan de hamburguesa clásico",
        "precio": 2.5,
        "stock": 500
    },
    'categoria':{
        "nombre": "categoria",
        'plural': 'categorias',
        'ruta': RUTA_CATEGORIA,
        "descripcion": "Hamburguesas clásicas y sabrosas"
    },
    'hamburguesa':{
        "nombre": "hamburguesa",
        'plural': 'hamburguesas',
        'ruta': RUTA_HAMBURGUESAS,
        "categoria": "categoria",
        "ingredientes": [],
        "precio": 10,
        "chef": "Chef"
    },

}
ETIQUETA_CAMPOS = {
    'chef': 'Chef',
    'ingrediente' : 'Ingrediente',
    'categoria' : 'Categoria',
    'hamburguesa' : 'Hamburguesa'
}
def crearDirectorios():
    os.makedirs("data", exist_ok=True)
crearDirectorios()