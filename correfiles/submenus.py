from utils.screenControllers import limpiarPantalla, pausarPantalla
from correfiles.categorias import menuRegistroCategoria
from correfiles.chef import menuRegistroChef
from correfiles.hamburguesas import menuRegistroHamburguesa

def seguimiento():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Seguimiento del Historial de ingredientes ')
        print('='* 50)
        print(' 1. Registrar ingredientes utilizados ')
        print(' 2. Ver ingredientes utilizados ')
        print(' 3. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                registrarIngredientesUtilizados()
            case '2':
                verIngredientesUtilizados()
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

def registrarIngredientesUtilizados():
    limpiarPantalla()
    pausarPantalla()

def verIngredientesUtilizados():
    limpiarPantalla()
    pausarPantalla()

def registroYGestionDeCategorias():
    menuRegistroCategoria()

def registroYGestionDeChef():
    menuRegistroChef()

def registroYGestionDeHamburguesas():
    menuRegistroHamburguesa()

def moduloDeReportes():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Modulo de reportes ')
        print('='* 50)
        print(' 1. Encontrar todos los ingredientes con stock menor a 400.')
        print(' 2. Encontrar todas las hamburguesas de la categoría "Vegetariana".')
        print(' 3. Encontrar todos los chefs que se especializan en "Carnes".')
        print(' 4. Aumentar en 1.5 el precio de todos los ingredientes.')
        print(' 5. Encontrar todas las hamburguesas preparadas por "ChefB".')
        print(' 6. Encontrar el nombre y la descripción de todas las categorías.')
        print(' 7. Eliminar todos los ingredientes que tengan un stock de 0.')
        print(' 8. Agregar un nuevo ingrediente a la hamburguesa "Clásica".')
        print(' 9. Encontrar todas las hamburguesas que contienen "Pan integral" como ingrediente.')
        print(' 10. Cambiar la especialidad del "ChefC" a "Cocina Internacional".')
        print(' 11. Encontrar el ingrediente más caro.')
        print(' 12. Encontrar las hamburguesas que no contienen "Queso cheddar" como ingrediente.')
        print(' 13. Incrementar el stock de "Pan" en 100 unidades.')
        print(' 14. Eliminar las hamburguesas que contienen menos de 5 ingredientes.')
        print(' 15. Agregar un nuevo chef a la colección con una especialidad en "Cocina Asiática".')
        print(' 16. Listar las hamburguesas en orden ascendente según su precio.')
        print(' 17. Encontrar todos los ingredientes cuyo precio sea entre $2 y $5.')
        print(' 18. Actualizar la descripción del "Pan" a "Pan fresco y crujiente".')
        print(' 19. Encontrar la hamburguesa más cara que fue preparada por un chef especializado en "Gourmet".')
        print(' 20. Listar todos los ingredientes junto con el número de hamburguesas que los contienen.')
        print(' 21. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                reporte1()
            case '2':
                reporte2()
            case '3':
                reporte3()
            case '4':
                reporte4()
            case '5':
                reporte5()
            case '6':
                reporte6()
            case '7':
                reporte7()
            case '8':
                reporte8()
            case '9':
                reporte9()
            case '10':
                reporte10()
            case '11':
                reporte11()
            case '12':
                reporte12()
            case '13':
                reporte13()
            case '14':
                reporte14()
            case '15':
                reporte15()
            case '16':
                reporte16()
            case '17':
                reporte17()
            case '18':
                reporte18()
            case '19':
                reporte19()
            case '20':
                reporte20()
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


def reporte1():
    limpiarPantalla()
    pausarPantalla()

def reporte2():
    limpiarPantalla()
    pausarPantalla()

def reporte3():
    limpiarPantalla()

    pausarPantalla()

def reporte4():
    limpiarPantalla()
    pausarPantalla()

def reporte5():
    limpiarPantalla()
    pausarPantalla()

def reporte6():
    limpiarPantalla()
    pausarPantalla()

def reporte7():
    limpiarPantalla()
    pausarPantalla()

def reporte8():
    limpiarPantalla()
    pausarPantalla()

def reporte9():
    limpiarPantalla()
    pausarPantalla()

def reporte10():
    limpiarPantalla()

    pausarPantalla()

def reporte11():
    limpiarPantalla()
    pausarPantalla()

def reporte12():
    limpiarPantalla()
    pausarPantalla()

def reporte13():
    limpiarPantalla()
    pausarPantalla()

def reporte14():
    limpiarPantalla()
    pausarPantalla()

def reporte15():
    limpiarPantalla()
    pausarPantalla()

def reporte16():
    limpiarPantalla()
    pausarPantalla()

def reporte17():
    limpiarPantalla()
    pausarPantalla()

def reporte18():
    limpiarPantalla()
    pausarPantalla()

def reporte19():
    limpiarPantalla()
    pausarPantalla()

def reporte20():
    limpiarPantalla()
    pausarPantalla()