from gestion_contactos import GestionContactos # Import de class to work with
from contacto import Contacto

class AppGestionContactos:
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

    def mostrar_contactos(self):
        contactos = self.gestion_contactos.obtener_contactos()
        if contactos:
            print('***Lista de contactos: ')
            for contacto in contactos:
                print(f'ID: {contacto.id_contacto}, Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}')
        else:
            print('No hay contactos disponibles.')

    def buscar_contacto(self):
        nombre_buscar = input('Introduce el nombre del contacto a buscar: ').lower()
        contactos = self.gestion_contactos.get_contactList()
        resultados = [contacto for contacto in contactos if nombre_buscar in contacto.nombre.lower()]
    
        if resultados:
            print('*** Resultados de la búsqueda: ***')
            for contacto in resultados:
                print(f'ID: {contacto.id_contacto}, Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}')
        else:
            print(f'No se encontraron contactos con el nombre "{nombre_buscar}".')

    def eliminar_contacto(self):
        try:
            id_contacto = int(input('Introduce el ID del contacto que deseas eliminar: '))
            contactos = self.gestion_contactos.get_contactList()
            contacto_a_eliminar = next((contacto for contacto in contactos if contacto.id_contacto == id_contacto), None)
            
            if contacto_a_eliminar:
                self.gestion_contactos.contactList = [contacto for contacto in contactos if contacto.id_contacto != id_contacto]
                self.gestion_contactos.guardar_contacto_archivo(self.gestion_contactos.contactList)
                print(f'Contacto con ID {id_contacto} eliminado correctamente.')
            else:
                print(f'No se encontró un contacto con el ID {id_contacto}.')
        except ValueError:
            print('Error: Introduce un número válido para el ID.')
        except Exception as e:
            print(f'Ocurrió un error al eliminar el contacto: {e}')

# Programa Principal
if __name__ == '__main__':
    appContactos = AppGestionContactos()
    appContactos.mostrar_menu()

