from utils.screenControllers import limpiarPantalla, pausarPantalla
import correfiles.submenus as submenus
from correfiles.ingredientes import menuRegistroIngredientes as menuIngredientes
def menuPrincipal():
    limpiarPantalla()
    while True:
    
        print('='* 50)
        print(' Bienvenido al sistema de gestion de inventario')
        print('='* 50)
        print(' 1. Registro y Gestion de ingrediente')
        print(' 2. Seguimiento del historial de ingredientes')
        print(' 3. registro y gestion de categorias')
        print(' 4. Registro y gestion de chef')
        print(' 5. Registro y gestion de Hamburguesas')
        print(' 6. Modulo de reportes')
        print(' 7. Salir')
        print('='* 50)
    
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                menuIngredientes()
            case '2':
                submenus.segimiento()
            case '3':
                submenus.registroYGestionDeCategorias()
            case '4':
                submenus.registroYGestionDeChef()
            case '5':
                submenus.registroYGestionDeHamburguesas()
            case '6':
                submenus.moduloDeReportes()
            case '7':
                limpiarPantalla()
                print('='*30)
                print('Gracias ')
                print('='*30)
                break
            case _:
                limpiarPantalla()
                print('='*30)
                print('Opcion invalida')
                print('='*30)
                pausarPantalla()
                limpiarPantalla()
                continue


if __name__ or '__main__': 
    menuPrincipal()
    