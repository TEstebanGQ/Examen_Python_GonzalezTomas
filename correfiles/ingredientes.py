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

def registroIngredientes():
    limpiarPantalla()
    print('-----Registro de ingredientes-----')
    ingredientes = cf.obtenerIngredientes()
    
    nombre = input('Ingrese el nombre del ingrediente: ').strip()
    if not nombre:
        print('El nombre no puede estar vacío')
        pausarPantalla()
        return
    
    descripcion = input('Ingrese la descripcion: ').strip()
    
    while True:
        try:
            precio = float(input('Ingrese el precio: '))
            if precio < 0:
                print('El precio no puede ser negativo')
                continue
            break
        except ValueError:
            print('Por favor ingrese un precio válido')
    
    while True:
        try:
            stock = int(input('Ingrese el stock: '))
            if stock < 0:
                print('El stock no puede ser negativo')
                continue
            break
        except ValueError:
            print('Por favor ingrese un stock válido')
    
    nuevoIngrediente = {
        'nombre': nombre,
        'descripcion': descripcion,
        'precio': precio,
        'stock': stock
    }
    
    ingredientes.append(nuevoIngrediente)
    cf.guardarIngredientes(ingredientes)
    print('Ingrediente registrado correctamente')
    pausarPantalla()

    while True:
        seguir = input('Desea seguir registrando ingredientes? (s/n): ').lower()
        if seguir == 's':
            registroIngredientes()
            break
        elif seguir == 'n':
            break
        else:
            print('Por favor ingrese s o n')

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
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    ingrediente = ingredientes[opcion-1]
    print(f'Nombre: {ingrediente["nombre"]}')
    print(f'Descripcion: {ingrediente["descripcion"]}')
    print(f'Precio: {ingrediente["precio"]}')
    print(f'Stock: {ingrediente["stock"]}')
    
    while True:
        campo = input('Ingrese el campo a editar (nombre/descripcion/precio/stock) o "salir" para terminar: ').lower()
        if campo == 'nombre':
            nuevo_nombre = input('Ingrese el nuevo nombre: ').strip()
            if nuevo_nombre:
                ingrediente['nombre'] = nuevo_nombre
                print('Nombre actualizado')
            else:
                print('El nombre no puede estar vacío')
        elif campo == 'descripcion':
            ingrediente['descripcion'] = input('Ingrese la nueva descripcion: ')
            print('Descripción actualizada')
        elif campo == 'precio':
            try:
                nuevo_precio = float(input('Ingrese el nuevo precio: '))
                if nuevo_precio >= 0:
                    ingrediente['precio'] = nuevo_precio
                    print('Precio actualizado')
                else:
                    print('El precio no puede ser negativo')
            except ValueError:
                print('Por favor ingrese un precio válido')
        elif campo == 'stock':
            try:
                nuevo_stock = int(input('Ingrese el nuevo stock: '))
                if nuevo_stock >= 0:
                    ingrediente['stock'] = nuevo_stock
                    print('Stock actualizado')
                else:
                    print('El stock no puede ser negativo')
            except ValueError:
                print('Por favor ingrese un stock válido')
        elif campo == 'salir':
            break
        else:
            print('Campo invalido')
    
    cf.guardarIngredientes(ingredientes)
    print('Ingrediente editado correctamente')
    pausarPantalla()

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
        print(f'Precio: ${ingrediente["precio"]:.2f}')
        print(f'Stock: {ingrediente["stock"]}')
        print('---------------------------')
    pausarPantalla()
    
def eliminarIngrediente():
    limpiarPantalla()
    print('-----Eliminar ingrediente-----')
    ingredientes = cf.obtenerIngredientes()
    if not ingredientes:
        print('No hay ingredientes registrados')
        pausarPantalla()
        return
    
    print('Ingredientes registrados:')
    for i, ingrediente in enumerate(ingredientes, 1):
        print(f'{i}. {ingrediente["nombre"]}')
    
    while True:
        try:
            opcion = int(input('Ingrese el numero del ingrediente a eliminar: '))
            if opcion < 1 or opcion > len(ingredientes):
                print('Opcion invalida')
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    ingrediente_eliminado = ingredientes[opcion - 1]["nombre"]
    confirmacion = input(f'¿Está seguro de eliminar "{ingrediente_eliminado}"? (s/n): ').lower()
    
    if confirmacion == 's':
        cf.eliminarIngrediente(opcion - 1)
        print('Ingrediente eliminado correctamente')
    else:
        print('Eliminación cancelada')
    
    pausarPantalla()