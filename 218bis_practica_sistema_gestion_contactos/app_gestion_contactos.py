from gestion_contactos import GestionContactos # Import de class to work with
from contacto import Contacto

class AppGestionContacos:
    def __init__(self):
        self.gestion_contactos = GestionContactos()

    def mostrar_menu(self):
        print('*** App Gestión de Contactos ***')
        while True:
            try:
                print(f'''Opciones:
                      1. Agregar un contacto
                      2. Mostrar todos los contactos
                      3. Buscar un contacto
                      4. Eliminar un contacto
                      5. Salir de la App
                      ''')
                opcion = int(input('Escribe una opción (1-5): '))
                if opcion == 1:
                    self.agregar_contacto()
                elif opcion == 2:
                    self.mostrar_contactos()
                elif opcion == 3:
                    self.buscar_contacto()
                elif opcion == 4:
                    self.eliminar_contacto()
                elif opcion == 5:
                    print('Esperamos verte de nuevo pronto!')
                    return True
                else:
                    print(f'Opción {opcion} no disponible')
                    return False

            except ValueError:
                print('Error: Introduce un número válido.')
            except Exception as e:
                print(f'Ocurrió un error: {e}')

    def agregar_contacto(self):
        nombre = input('Nombre: ')
        telefono = input('Teléfono: ')
        email = input('Email: ')
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.gestion_contactos.agregar_contactos(nuevo_contacto)
        print('Contacto agregado correctamente. ')


# Programa Principal
if __name__ == '__main__':
    appContactos = AppGestionContacos()
    appContactos.mostrar_menu()

