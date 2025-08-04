
from utils.screenControllers import limpiarPantalla, pausarPantalla

def segimiento():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Seguimiento del Historial de ingredientes ')
        print('='* 50)
        print(' 1. Registar ingredientes utilizados ')
        print(' 2. Ver ingredientes utilizados ')
        print(' 3. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                pass
            case '2':
                pass
            case '3':
                limpiarPantalla()
                return 
            case _:
                limpiarPantalla()
                print('=' * 50)
                print('Opcion invalida, por favor intente de nuevo')
                print('=' * 50)
                pausarPantalla()
                limpiarPantalla()
                break

def registroYGestionDeCategorias():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Registro y gestion de categorias ')
        print('='* 50)
        print(' 1. Registrar categoria ')
        print(' 2. Ver categorias ')
        print(' 3. Editar categoria ')
        print(' 4. Eliminar categoria ')
        print(' 5. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                limpiarPantalla()
                return
            case _:
                limpiarPantalla()
                print('=' * 50)
                print('Opcion invalida, por favor intente de nuevo')
                print('=' * 50)
                pausarPantalla()
                limpiarPantalla()
                break

def registroYGestionDeChef():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Registro y gestion de chef ')
        print('='* 50)
        print(' 1. Registrar chef ')
        print(' 2. Ver chefs ')
        print(' 3. Editar chef ')
        print(' 4. Eliminar chef ')
        print(' 5. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                limpiarPantalla()
                return
            case _:
                limpiarPantalla()
                print('=' * 50)
                print('Opcion invalida, por favor intente de nuevo')
                print('=' * 50)
                pausarPantalla()
                limpiarPantalla()
                break
def registroYGestionDeHamburguesas():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Registro y gestion de hamburguesas ')
        print('='* 50)
        print(' 1. Registrar hamburguesa ')
        print(' 2. Ver hamburguesas ')
        print(' 3. Editar hamburguesa ')
        print(' 4. Eliminar hamburguesa ')
        print(' 5. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                limpiarPantalla()
                return
            case _:
                limpiarPantalla()
                print('=' * 50)
                print('Opcion invalida, por favor intente de nuevo')
                print('=' * 50)
                pausarPantalla()
                limpiarPantalla()
                break

def moduloDeReportes():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Modulo de reportes ')
        print('='* 50)
        print(' 1. Encontrar todos los ingredientes con stock menor a 400.')
        print(' 2. Encontrar todas las hamburguesas de la categoría “Vegetariana”.')
        print(' 3. Encontrar todos los chefs que se especializan en “Carnes”.')
        print(' 4. Aumentar en 1.5 el precio de todos los ingredientes.')
        print(' 5. Encontrar todas las hamburguesas preparadas por “ChefB”.')
        print(' 6. Encontrar el nombre y la descripción de todas las categorías.')
        print(' 7. Eliminar todos los ingredientes que tengan un stock de 0.')
        print(' 8. Agregar un nuevo ingrediente a la hamburguesa “Clásica”.')
        print(' 9. Encontrar todas las hamburguesas que contienen “Pan integral” como ingrediente.')
        print(' 10. Cambiar la especialidad del “ChefC” a “Cocina Internacional”.')
        print(' 11. Encontrar el ingrediente más caro.')
        print(' 12. Encontrar las hamburguesas que no contienen “Queso cheddar” como ingrediente.')
        print(' 13. Incrementar el stock de “Pan” en 100 unidades.')
        print(' 14. Eliminar las hamburguesas que contienen menos de 5 ingredientes.')
        print(' 15. Agregar un nuevo chef a la colección con una especialidad en “Cocina Asiática”.')
        print(' 16. Listar las hamburguesas en orden ascendente según su precio.')
        print(' 17. Encontrar todos los ingredientes cuyo precio sea entre $2 y $5.Actualizar la descripción del “Pan” a “Pan fresco y crujiente”.')
        print(' 18. Encontrar la hamburguesa más cara que fue preparada por un chef especializado en “Gourmet”.')
        print(' 20. Listar todos los ingredientes junto con el número de hamburguesas que los contienen.')
        print(' 21. voler al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                pass
            case '9':
                pass
            case '10':
                pass
            case '11':
                pass
            case '12':
                pass
            case '13':
                pass
            case '14':
                pass
            case '15':
                pass
            case '16':
                pass
            case '17':
                pass
            case '18':
                pass
            case '19':
                pass
            case '20':
                pass
            case '21':
                limpiarPantalla()
                return
            case _:
                limpiarPantalla()
                print('=' * 50)
                print('Opcion invalida, por favor intente de nuevo')
                print('=' * 50)
                pausarPantalla()
                limpiarPantalla()
                break

        



        

