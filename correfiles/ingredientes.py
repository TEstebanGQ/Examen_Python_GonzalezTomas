import utils.coreFiles as cf
from utils.screenControllers import pausarPantalla, limpiarPantalla
from config import TIPO_DE_ELEMENTOS, ETIQUETA_CAMPOS
def menuRegistroIngredientes():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Registro y gestion de ingredientes')
        print('='* 50)
        print(' 1. Registrar ingrediente')
        print(' 2. Listar ingredientes')
        print(' 3. Editar ingrediente')
        print(' 4. Eliminar ingrediente')
        print(' 5. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                registroIngredientes()
            case '2':
                listarIngredientes()
            case '3':
                editarIngrediente()
            case '4':
                eliminarIngrediente()
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

def registroIngredientes():
    limpiarPantalla()
    print('-----Registro nde ingredientes-----')
    ingredientes = cf.obtenerIngredientes()
    nuevoIngrediente = {
        'nombre': input('Ingrese el nombre del ingrediente: '),
        'descripcion' : input('Ingrese la descripcion: '),
        'precio' : input('Ingrese el precio: '),
        'stock' : input('Ingrese el stock: ')
    }
    ingredientes.append(nuevoIngrediente)
    cf.guardarIngredientes(ingredientes)
    print('Ingredientes registrados correctamente')

    while True:
        seguir = input('Desea seguir registrando ingredientes? (s/n): ')
        if seguir.lower() == 's':
            registroIngredientes()
        else:
            break
def editarIngrediente():
    limpiarPantalla()
    print('-----Editar ingrediente-----')
    ingredientes = cf.obtenerIngredientes()
    if not ingredientes:
        print('No hay ingredientes registrados')
        pausarPantalla()
        return
    print('Ingredientes registrados:')
    for i, ingrediente in enumerate(ingredientes):
        print(f'{i+1}. {ingrediente["nombre"]}')
        while True:
            try:
                opcion = int(input('Ingrese el numero del ingrediente a editar: '))
                if opcion < 1 or opcion > len(ingredientes):
                    print('Opcion invalida')
                else:
                    break
            except ValueError:
                print('Opcion invalida')
                break
            ingrediente = ingredientes[opcion-1]
            print(f'Nombre: {ingrediente["nombre"]}')
            print(f'Descripcion: {ingrediente["descripcion"]}')
            print(f'Precio: {ingrediente["precio"]}')
            print(f'Stock: {ingrediente["stock"]}')
            while True:
                opcion = input('Ingrese el campo a editar (nombre/descripcion/precio/stock):')
                if opcion.lower() == 'nombre':
                    ingrediente['nombre'] = input('Ingrese el nuevo nombre: ')
                elif opcion.lower() == 'descripcion':
                    ingrediente['descripcion'] = input('Ingrese la nueva descripcion: ')
                elif opcion.lower() == 'precio':
                    ingrediente['precio'] = float(input('Ingrese el nuevo precio: '))
                elif opcion.lower() == 'stock':
                    ingrediente['stock'] = float(input('Ingrese el nuevo stock: '))
                else:
                    print('Opcion invalida')
                break
            cf.guardarIngredientes(ingredientes)
            print('Ingrediente editado correctamente')

def listarIngredientes():
    limpiarPantalla()
    print('-----Ingredientes registrados-----')
    ingredientes = cf.obtenerIngredientes()
    if not ingredientes:
        print('No hay ingredientes registrados')
        pausarPantalla()
        return
    for ingrediente in ingredientes:
        print(f'Nombre: {ingrediente["nombre"]}')
        print(f'Descripcion: {ingrediente["descripcion"]}')
        print(f'Precio: {ingrediente["precio"]}')
        print(f'Stock: {ingrediente["stock"]}')
        print('---------------------------')
        pausarPantalla()
        return
    
def eliminarIngrediente():
    limpiarPantalla()
    while True:
        try:
            opcion = int(input('Ingrese el numero del ingrediente a eliminar: '))
            if opcion < 1:
                print('Opcion invalida')
                continue
            break
        except ValueError:
            print('Opcion invalida')
            ingredientes = cf.obtenerIngredientes()
            for i, ingrediente in enumerate(ingredientes, 1):
                print(f'{i}. {ingrediente["nombre"]}')
                pausarPantalla()
                continue
            cf.eliminarIngrediente(opcion - 1)
            print('Ingrediente eliminado correctamente')
            pausarPantalla()
            return





        


