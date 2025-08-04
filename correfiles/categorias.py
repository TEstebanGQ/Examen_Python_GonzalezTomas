import utils.coreFiles as cf
from utils.screenControllers import pausarPantalla, limpiarPantalla
from config import TIPO_DE_ELEMENTOS, ETIQUETA_CAMPOS

def menuRegistroCategoria():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Registro y gestion de categorias')
        print('='* 50)
        print(' 1. Registrar categoria')
        print(' 2. Listar categorias')
        print(' 3. Editar categoria')
        print(' 4. Eliminar categoria')
        print(' 5. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                registroCategoria()
            case '2':
                listarCategorias()
            case '3':
                editarCategoria()
            case '4':
                eliminarCategoria()
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

def registroCategoria():
    limpiarPantalla()
    print('-----Registro de categorias-----')
    categorias = cf.obtenerCategoria()
    
    nombre = input('Ingrese el nombre de la categoria: ').strip()
    if not nombre:
        print('El nombre no puede estar vacío')
        pausarPantalla()
        return
    
    descripcion = input('Ingrese la descripcion de la categoria: ').strip()
    
    nuevaCategoria = {
        'nombre': nombre,
        'descripcion': descripcion
    }
    
    categorias.append(nuevaCategoria)
    cf.guardarCategoria(categorias)
    print('Categoria registrada correctamente')
    pausarPantalla()

    while True:
        seguir = input('Desea seguir registrando categorias? (s/n): ').lower()
        if seguir == 's':
            registroCategoria()
            break
        elif seguir == 'n':
            break
        else:
            print('Por favor ingrese s o n')

def editarCategoria():
    limpiarPantalla()
    print('-----Editar categoria-----')
    categorias = cf.obtenerCategoria()
    if not categorias:
        print('No hay categorias registradas')
        pausarPantalla()
        return
    
    print('Categorias registradas:')
    for i, categoria in enumerate(categorias):
        print(f'{i+1}. {categoria["nombre"]} - {categoria["descripcion"]}')
    
    while True:
        try:
            opcion = int(input('Ingrese el numero de la categoria a editar: '))
            if opcion < 1 or opcion > len(categorias):
                print('Opcion invalida')
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    categoria = categorias[opcion-1]
    print(f'Nombre: {categoria["nombre"]}')
    print(f'Descripcion: {categoria["descripcion"]}')
    
    while True:
        campo = input('Ingrese el campo a editar (nombre/descripcion) o "salir" para terminar: ').lower()
        if campo == 'nombre':
            nuevo_nombre = input('Ingrese el nuevo nombre: ').strip()
            if nuevo_nombre:
                categoria['nombre'] = nuevo_nombre
                print('Nombre actualizado')
            else:
                print('El nombre no puede estar vacío')
        elif campo == 'descripcion':
            categoria['descripcion'] = input('Ingrese la nueva descripcion: ')
            print('Descripción actualizada')
        elif campo == 'salir':
            break
        else:
            print('Campo invalido')
    
    cf.guardarCategoria(categorias)
    print('Categoria editada correctamente')
    pausarPantalla()

def listarCategorias():
    limpiarPantalla()
    print('-----Categorias registradas-----')
    categorias = cf.obtenerCategoria()
    if not categorias:
        print('No hay categorias registradas')
        pausarPantalla()
        return
    
    for categoria in categorias:
        print(f'Nombre: {categoria["nombre"]}')
        print(f'Descripcion: {categoria["descripcion"]}')
        print('---------------------------')
    pausarPantalla()
    
def eliminarCategoria():
    limpiarPantalla()
    print('-----Eliminar categoria-----')
    categorias = cf.obtenerCategoria()
    if not categorias:
        print('No hay categorias registradas')
        pausarPantalla()
        return
    
    print('Categorias registradas:')
    for i, categoria in enumerate(categorias, 1):
        print(f'{i}. {categoria["nombre"]} - {categoria["descripcion"]}')
    
    while True:
        try:
            opcion = int(input('Ingrese el numero de la categoria a eliminar: '))
            if opcion < 1 or opcion > len(categorias):
                print('Opcion invalida')
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    categoria_eliminada = categorias[opcion - 1]["nombre"]
    confirmacion = input(f'¿Está seguro de eliminar la categoria "{categoria_eliminada}"? (s/n): ').lower()
    
    if confirmacion == 's':
        cf.eliminarCategoria(opcion - 1)
        print('Categoria eliminada correctamente')
    else:
        print('Eliminación cancelada')
    
    pausarPantalla()