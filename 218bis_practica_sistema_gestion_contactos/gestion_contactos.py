import os.path
from contacto import Contacto


class GestionContactos:
    # Ruta absoluta al archivo contactos.txt en el subdirectorio actual
    NOMBRE_ARCHIVO = os.path.join(os.path.dirname(__file__), 'contactos.txt')

    def __init__(self):
        self.contactList = []
        # Reviso si existe archivo contactos.txt
        # Si existe obtengo los contactos del archivo con el método obtener
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.contactList = self.obtener_contactos()

    def obtener_contactos(self):
        contactList = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo:
                for linea in archivo:
                    # Uso Strip para eliminar caracteres en blanco delante o detrás.
                    # Uso Split para usar el separador coma como separador entre valores de cada variable
                    # y asignar los valores a cada variable en una tupla
                    id_contacto, nombre, telefono, email = linea.strip().split(',')
                    contacto = Contacto(nombre, telefono, email)
                    contactList.append(contacto)

        except Exception as e:
            print(f'Error al leer archivo contactos: {e}')
        return contactList

    def guardar_contacto_archivo(self, contactList):
        try:
            # Sobrescribimos el archivo para evitar duplicados
            with open(self.NOMBRE_ARCHIVO, 'w', encoding='utf8') as archivo:
                for contacto in contactList:
                    archivo.write(f'{contacto.escribir_contacto()}\n')

        except Exception as e:
            print(f'Error al guardar contactos en archivo: {e}')

    def agregar_contactos(self, contacto):
        # Verificar si el contacto ya existe en la lista
        if not any(c.nombre == contacto.nombre and c.telefono == contacto.telefono and c.email == contacto.email for c in self.contactList):
            self.contactList.append(contacto)
            self.guardar_contacto_archivo(self.contactList)
            print(f'Contacto agregado: {contacto}')
        else:
            print('El contacto ya existe en la lista.')

    def mostrar_contactList(self):
        print(' ----   Contactos en el fichero  ----')
        for contacto in self.contactList:
            print(contacto)

    def get_contactList(self):
        return self.contactList