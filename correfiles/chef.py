import utils.coreFiles as cf
from utils.screenControllers import pausarPantalla, limpiarPantalla
from config import TIPO_DE_ELEMENTOS, ETIQUETA_CAMPOS

def menuRegistroChef():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Registro y gestion de chefs')
        print('='* 50)
        print(' 1. Registrar chef')
        print(' 2. Listar chefs')
        print(' 3. Editar chef')
        print(' 4. Eliminar chef')
        print(' 5. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                registroChef()
            case '2':
                listarChefs()
            case '3':
                editarChef()
            case '4':
                eliminarChef()
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

def registroChef():
    limpiarPantalla()
    print('-----Registro de chefs-----')
    chefs = cf.obtenerChef()
    
    nombre = input('Ingrese el nombre del chef: ').strip()
    if not nombre:
        print('El nombre no puede estar vacío')
        pausarPantalla()
        return
    
    especialidad = input('Ingrese la especialidad del chef: ').strip()
    if not especialidad:
        print('La especialidad no puede estar vacía')
        pausarPantalla()
        return
    
    nuevoChef = {
        'nombre': nombre,
        'especialidad': especialidad
    }
    
    chefs.append(nuevoChef)
    cf.guardarChef(chefs)
    print('Chef registrado correctamente')
    pausarPantalla()

    while True:
        seguir = input('Desea seguir registrando chefs? (s/n): ').lower()
        if seguir == 's':
            registroChef()
            break
        elif seguir == 'n':
            break
        else:
            print('Por favor ingrese s o n')

def editarChef():
    limpiarPantalla()
    print('-----Editar chef-----')
    chefs = cf.obtenerChef()
    if not chefs:
        print('No hay chefs registrados')
        pausarPantalla()
        return
    
    print('Chefs registrados:')
    for i, chef in enumerate(chefs):
        print(f'{i+1}. {chef["nombre"]} - {chef["especialidad"]}')
    
    while True:
        try:
            opcion = int(input('Ingrese el numero del chef a editar: '))
            if opcion < 1 or opcion > len(chefs):
                print('Opcion invalida')
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    chef = chefs[opcion-1]
    print(f'Nombre: {chef["nombre"]}')
    print(f'Especialidad: {chef["especialidad"]}')
    
    while True:
        campo = input('Ingrese el campo a editar (nombre/especialidad) o "salir" para terminar: ').lower()
        if campo == 'nombre':
            nuevo_nombre = input('Ingrese el nuevo nombre: ').strip()
            if nuevo_nombre:
                chef['nombre'] = nuevo_nombre
                print('Nombre actualizado')
            else:
                print('El nombre no puede estar vacío')
        elif campo == 'especialidad':
            nueva_especialidad = input('Ingrese la nueva especialidad: ').strip()
            if nueva_especialidad:
                chef['especialidad'] = nueva_especialidad
                print('Especialidad actualizada')
            else:
                print('La especialidad no puede estar vacía')
        elif campo == 'salir':
            break
        else:
            print('Campo invalido')
    
    cf.guardarChef(chefs)
    print('Chef editado correctamente')
    pausarPantalla()

def listarChefs():
    limpiarPantalla()
    print('-----Chefs registrados-----')
    chefs = cf.obtenerChef()
    if not chefs:
        print('No hay chefs registrados')
        pausarPantalla()
        return
    
    for chef in chefs:
        print(f'Nombre: {chef["nombre"]}')
        print(f'Especialidad: {chef["especialidad"]}')
        print('---------------------------')
    pausarPantalla()
    
def eliminarChef():
    limpiarPantalla()
    print('-----Eliminar chef-----')
    chefs = cf.obtenerChef()
    if not chefs:
        print('No hay chefs registrados')
        pausarPantalla()
        return
    
    print('Chefs registrados:')
    for i, chef in enumerate(chefs, 1):
        print(f'{i}. {chef["nombre"]} - {chef["especialidad"]}')
    
    while True:
        try:
            opcion = int(input('Ingrese el numero del chef a eliminar: '))
            if opcion < 1 or opcion > len(chefs):
                print('Opcion invalida')
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    chef_eliminado = chefs[opcion - 1]["nombre"]
    confirmacion = input(f'¿Está seguro de eliminar al chef "{chef_eliminado}"? (s/n): ').lower()
    
    if confirmacion == 's':
        cf.eliminarChef(opcion - 1)
        print('Chef eliminado correctamente')
    else:
        print('Eliminación cancelada')
    
    pausarPantalla()