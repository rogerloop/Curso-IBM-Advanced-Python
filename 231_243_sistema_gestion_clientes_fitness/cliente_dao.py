# Esta clase servirá para poder interactuar para objeto tipo cliente 
# importación de clases con ".archivo" realtive Path
from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM clientes ORDER BY id'
    INSERTAR = 'INSERT INTO clientes(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALIZAR = 'UPDATE clientes SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    DELETE = 'DELETE FROM cliente WHERE id=%s'
    
    # Creamos el método de clase seleccionar    
    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Por cada registro que recuperemos de la tabla de la DB clientes vamos 
            # a crear un Objeto tipo Cliente aprovechando la clase
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes

        except Exception as e:
            print(f'Ocurrió un error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar (cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar un cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

# lineas para comprobar que código funcioina
if __name__ == '__main__':
    # prueba insertar cliente
    cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia=300)
    clientes_insertados =ClienteDAO.insertar(cliente1)
    print(f'Clientes insertados : {clientes_insertados}')

    #seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)


