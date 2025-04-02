# Ejemplo de uso de decoradores en Python para autenticar usuarios y registrar logs

print("Ejemplo: Autenticación y registro de logs en una aplicación web")
# Importar librerías necesarias

import datetime

# Decorador para verificar si el usuario está autenticado
def requiere_autenticacion(funcion):
    def wrapper(usuario, *args, **kwargs):
        if not usuario.get('autenticado', False):
            print(f"[{datetime.datetime.now()}] Acceso denegado: Usuario no autenticado")
            return "Error: Usuario no autenticado"
        return funcion(usuario, *args, **kwargs)
    return wrapper

# Decorador para registrar logs de las funciones
def registrar_log(funcion):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.datetime.now()}] Ejecutando función: {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"[{datetime.datetime.now()}] Función {funcion.__name__} ejecutada con éxito")
        return resultado
    return wrapper

# Función principal: Ver datos del usuario
@requiere_autenticacion
@registrar_log
def ver_datos_usuario(usuario):
    print(f"Mostrando datos del usuario: {usuario['nombre']}")
    return f"Datos del usuario: {usuario['nombre']}"

# Función principal: Eliminar cuenta del usuario
@requiere_autenticacion
@registrar_log
def eliminar_cuenta(usuario):
    print(f"Eliminando cuenta del usuario: {usuario['nombre']}")
    return f"Cuenta de {usuario['nombre']} eliminada"

# Simulación de usuarios
usuario_autenticado = {'nombre': 'Roger', 'autenticado': True}
usuario_no_autenticado = {'nombre': 'Anna', 'autenticado': False}

# Llamadas a las funciones
print(ver_datos_usuario(usuario_autenticado))  # Usuario autenticado
print(ver_datos_usuario(usuario_no_autenticado))  # Usuario no autenticado
print(eliminar_cuenta(usuario_autenticado))  # Usuario autenticado
print(eliminar_cuenta(usuario_no_autenticado))  # Usuario no autenticado