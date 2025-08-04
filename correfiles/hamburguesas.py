import utils.coreFiles as cf
from utils.screenControllers import pausarPantalla, limpiarPantalla
from config import TIPO_DE_ELEMENTOS, ETIQUETA_CAMPOS

def menuRegistroHamburguesa():
    limpiarPantalla()
    while True:
        print('='* 50)
        print(' Registro y gestion de hamburguesas')
        print('='* 50)
        print(' 1. Registrar hamburguesa')
        print(' 2. Listar hamburguesas')
        print(' 3. Editar hamburguesa')
        print(' 4. Eliminar hamburguesa')
        print(' 5. Volver al menu principal')
        print('='* 50)
        opcion = input("Ingrese la opcion que desee: ")
        match opcion:
            case '1':
                registroHamburguesa()
            case '2':
                listarHamburguesas()
            case '3':
                editarHamburguesa()
            case '4':
                eliminarHamburguesa()
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

def registroHamburguesa():
    limpiarPantalla()
    print('-----Registro de hamburguesas-----')
    hamburguesas = cf.obtenerHamburguesa()
    
    nombre = input('Ingrese el nombre de la hamburguesa: ').strip()
    if not nombre:
        print('El nombre no puede estar vacío')
        pausarPantalla()
        return
    categorias = cf.obtenerCategoria()
    if not categorias:
        print('No hay categorias registradas. Registre una categoria primero.')
        pausarPantalla()
        return
    
    print('Categorias disponibles:')
    for i, categoria in enumerate(categorias):
        print(f'{i+1}. {categoria["nombre"]}')
    
    while True:
        try:
            opcion_cat = int(input('Seleccione la categoria: '))
            if opcion_cat < 1 or opcion_cat > len(categorias):
                print('Opcion invalida')
                continue
            categoria_seleccionada = categorias[opcion_cat-1]["nombre"]
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    # Seleccionar ingredientes
    ingredientes = cf.obtenerIngredientes()
    if not ingredientes:
        print('No hay ingredientes registrados. Registre ingredientes primero.')
        pausarPantalla()
        return
    
    print('Ingredientes disponibles:')
    for i, ingrediente in enumerate(ingredientes):
        print(f'{i+1}. {ingrediente["nombre"]}')
    
    ingredientes_hamburguesa = []
    print('Seleccione los ingredientes (ingrese 0 para terminar):')
    while True:
        try:
            opcion_ing = int(input('Seleccione ingrediente (0 para terminar): '))
            if opcion_ing == 0:
                break
            if opcion_ing < 1 or opcion_ing > len(ingredientes):
                print('Opcion invalida')
                continue
            ingrediente_sel = ingredientes[opcion_ing-1]["nombre"]
            if ingrediente_sel not in ingredientes_hamburguesa:
                ingredientes_hamburguesa.append(ingrediente_sel)
                print(f'Ingrediente "{ingrediente_sel}" agregado')
            else:
                print('Este ingrediente ya fue agregado')
        except ValueError:
            print('Por favor ingrese un número válido')
    
    if not ingredientes_hamburguesa:
        print('Debe seleccionar al menos un ingrediente')
        pausarPantalla()
        return
    
    # Seleccionar chef
    chefs = cf.obtenerChef()
    if not chefs:
        print('No hay chefs registrados. Registre un chef primero.')
        pausarPantalla()
        return
    
    print('Chefs disponibles:')
    for i, chef in enumerate(chefs):
        print(f'{i+1}. {chef["nombre"]} - {chef["especialidad"]}')
    
    while True:
        try:
            opcion_chef = int(input('Seleccione el chef: '))
            if opcion_chef < 1 or opcion_chef > len(chefs):
                print('Opcion invalida')
                continue
            chef_seleccionado = chefs[opcion_chef-1]["nombre"]
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    # Precio
    while True:
        try:
            precio = float(input('Ingrese el precio de la hamburguesa: '))
            if precio < 0:
                print('El precio no puede ser negativo')
                continue
            break
        except ValueError:
            print('Por favor ingrese un precio válido')
    
    nuevaHamburguesa = {
        'nombre': nombre,
        'categoria': categoria_seleccionada,
        'ingredientes': ingredientes_hamburguesa,
        'chef': chef_seleccionado,
        'precio': precio
    }
    
    hamburguesas.append(nuevaHamburguesa)
    cf.guardarHamburguesa(hamburguesas)
    print('Hamburguesa registrada correctamente')
    pausarPantalla()

    while True:
        seguir = input('Desea seguir registrando hamburguesas? (s/n): ').lower()
        if seguir == 's':
            registroHamburguesa()
            break
        elif seguir == 'n':
            break
        else:
            print('Por favor ingrese s o n')

def editarHamburguesa():
    limpiarPantalla()
    print('-----Editar hamburguesa-----')
    hamburguesas = cf.obtenerHamburguesa()
    if not hamburguesas:
        print('No hay hamburguesas registradas')
        pausarPantalla()
        return
    
    print('Hamburguesas registradas:')
    for i, hamburguesa in enumerate(hamburguesas):
        ingredientes_str = ', '.join(hamburguesa["ingredientes"])
        print(f'{i+1}. {hamburguesa["nombre"]} - ${hamburguesa["precio"]:.2f} - {hamburguesa["categoria"]}')
    
    while True:
        try:
            opcion = int(input('Ingrese el numero de la hamburguesa a editar: '))
            if opcion < 1 or opcion > len(hamburguesas):
                print('Opcion invalida')
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    hamburguesa = hamburguesas[opcion-1]
    print(f'Nombre: {hamburguesa["nombre"]}')
    print(f'Categoria: {hamburguesa["categoria"]}')
    print(f'Ingredientes: {", ".join(hamburguesa["ingredientes"])}')
    print(f'Chef: {hamburguesa["chef"]}')
    print(f'Precio: ${hamburguesa["precio"]:.2f}')
    
    while True:
        campo = input('Ingrese el campo a editar (nombre/categoria/ingredientes/chef/precio) o "salir" para terminar: ').lower()
        if campo == 'nombre':
            nuevo_nombre = input('Ingrese el nuevo nombre: ').strip()
            if nuevo_nombre:
                hamburguesa['nombre'] = nuevo_nombre
                print('Nombre actualizado')
            else:
                print('El nombre no puede estar vacío')
        elif campo == 'categoria':
            categorias = cf.obtenerCategoria()
            if categorias:
                print('Categorias disponibles:')
                for i, categoria in enumerate(categorias):
                    print(f'{i+1}. {categoria["nombre"]}')
                try:
                    opcion_cat = int(input('Seleccione nueva categoria: '))
                    if 1 <= opcion_cat <= len(categorias):
                        hamburguesa['categoria'] = categorias[opcion_cat-1]["nombre"]
                        print('Categoria actualizada')
                    else:
                        print('Opcion invalida')
                except ValueError:
                    print('Por favor ingrese un número válido')
            else:
                print('No hay categorias registradas')
        elif campo == 'ingredientes':
            ingredientes = cf.obtenerIngredientes()
            if ingredientes:
                print('Ingredientes disponibles:')
                for i, ingrediente in enumerate(ingredientes):
                    print(f'{i+1}. {ingrediente["nombre"]}')
                
                nuevos_ingredientes = []
                print('Seleccione los nuevos ingredientes (ingrese 0 para terminar):')
                while True:
                    try:
                        opcion_ing = int(input('Seleccione ingrediente (0 para terminar): '))
                        if opcion_ing == 0:
                            break
                        if opcion_ing < 1 or opcion_ing > len(ingredientes):
                            print('Opcion invalida')
                            continue
                        ingrediente_sel = ingredientes[opcion_ing-1]["nombre"]
                        if ingrediente_sel not in nuevos_ingredientes:
                            nuevos_ingredientes.append(ingrediente_sel)
                            print(f'Ingrediente "{ingrediente_sel}" agregado')
                        else:
                            print('Este ingrediente ya fue agregado')
                    except ValueError:
                        print('Por favor ingrese un número válido')
                
                if nuevos_ingredientes:
                    hamburguesa['ingredientes'] = nuevos_ingredientes
                    print('Ingredientes actualizados')
                else:
                    print('Debe seleccionar al menos un ingrediente')
            else:
                print('No hay ingredientes registrados')
        elif campo == 'chef':
            chefs = cf.obtenerChef()
            if chefs:
                print('Chefs disponibles:')
                for i, chef in enumerate(chefs):
                    print(f'{i+1}. {chef["nombre"]} - {chef["especialidad"]}')
                try:
                    opcion_chef = int(input('Seleccione nuevo chef: '))
                    if 1 <= opcion_chef <= len(chefs):
                        hamburguesa['chef'] = chefs[opcion_chef-1]["nombre"]
                        print('Chef actualizado')
                    else:
                        print('Opcion invalida')
                except ValueError:
                    print('Por favor ingrese un número válido')
            else:
                print('No hay chefs registrados')
        elif campo == 'precio':
            try:
                nuevo_precio = float(input('Ingrese el nuevo precio: '))
                if nuevo_precio >= 0:
                    hamburguesa['precio'] = nuevo_precio
                    print('Precio actualizado')
                else:
                    print('El precio no puede ser negativo')
            except ValueError:
                print('Por favor ingrese un precio válido')
        elif campo == 'salir':
            break
        else:
            print('Campo invalido')
    
    cf.guardarHamburguesa(hamburguesas)
    print('Hamburguesa editada correctamente')
    pausarPantalla()

def listarHamburguesas():
    limpiarPantalla()
    print('-----Hamburguesas registradas-----')
    hamburguesas = cf.obtenerHamburguesa()
    if not hamburguesas:
        print('No hay hamburguesas registradas')
        pausarPantalla()
        return
    
    for hamburguesa in hamburguesas:
        print(f'Nombre: {hamburguesa["nombre"]}')
        print(f'Categoria: {hamburguesa["categoria"]}')
        print(f'Ingredientes: {", ".join(hamburguesa["ingredientes"])}')
        print(f'Chef: {hamburguesa["chef"]}')
        print(f'Precio: ${hamburguesa["precio"]:.2f}')
        print('---------------------------')
    pausarPantalla()
    
def eliminarHamburguesa():
    limpiarPantalla()
    print('-----Eliminar hamburguesa-----')
    hamburguesas = cf.obtenerHamburguesa()
    if not hamburguesas:
        print('No hay hamburguesas registradas')
        pausarPantalla()
        return
    
    print('Hamburguesas registradas:')
    for i, hamburguesa in enumerate(hamburguesas, 1):
        print(f'{i}. {hamburguesa["nombre"]} - ${hamburguesa["precio"]:.2f}')
    
    while True:
        try:
            opcion = int(input('Ingrese el numero de la hamburguesa a eliminar: '))
            if opcion < 1 or opcion > len(hamburguesas):
                print('Opcion invalida')
                continue
            break
        except ValueError:
            print('Por favor ingrese un número válido')
    
    hamburguesa_eliminada = hamburguesas[opcion - 1]["nombre"]
    confirmacion = input(f'¿Está seguro de eliminar la hamburguesa "{hamburguesa_eliminada}"? (s/n): ').lower()
    
    if confirmacion == 's':
        cf.eliminarHamburguesa(opcion - 1)
        print('Hamburguesa eliminada correctamente')
    else:
        print('Eliminación cancelada')
    
    pausarPantalla()