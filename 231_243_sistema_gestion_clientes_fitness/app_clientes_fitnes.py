from cliente_dao import ClienteDAO
from cliente import Cliente

print(f'\n***  Clientes Zona Fit (GYM  ***')
opcion = None   # genero bucle para mostrar menu
while opcion != 5:
    try:
        print(f'''\nOpciones:
                1. Listar clientes
                2. Agregar cliente
                3. Modificar cliente
                4. Eliminar cliente
                5. Salir
                ''')
        opcion = int(input('Esribe tu opción (1-5): '))
        if opcion == 1:     # Listar clientes
            clientes = ClienteDAO.seleccionar()
            print(f'\n***  Listado de Clientes  ***\n')
            for cliente in clientes:
                print(cliente)

        elif opcion == 2:   # Agregar clientes
            nombre_var = input('Escribe el nombre: ')
            apellido_var = input('Escribe el apellido: ')
            membresia_var = input('Escribe la membresia: ')
            cliente = Cliente (nombre=nombre_var, apellido=apellido_var,
                                membresia=membresia_var)   
            clientes_insertados = ClienteDAO.insertar(cliente)
            print(f'\nClientes insertados: {clientes_insertados}')

        elif opcion == 3:   # Modificar cliente
            id_var = int(input('Escribe el id del cliente a modificar: '))
            nombre_var = input('Escribe el nombre: ')
            apellido_var = input('Escribe el apellido: ')
            membresia_var = input('Escribe la membresia: ')
            cliente = Cliente (id=id_var, nombre=nombre_var, apellido=apellido_var, 
                               membresia=membresia_var)
            clientes_actualizados = ClienteDAO.actualizar(cliente)
            print(f'\nClientes modificados: {clientes_actualizados}')

        elif opcion == 4:   # Eliminar cliente
            id_var = int(input('Escribe el id del cliente a eliminar: '))
            cliente_eliminar = Cliente(id=id_var)
            clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
            print(f'\nCientes eliminados de la DB: {clientes_eliminados}')
            
        elif opcion == 5:
            print('\nEsperamos verte de nuevo pronto!\n')
            
        else:
            print(f'Opción {opcion} no disponible')

    except ValueError:
        print('Error: Introduce un número válido.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

