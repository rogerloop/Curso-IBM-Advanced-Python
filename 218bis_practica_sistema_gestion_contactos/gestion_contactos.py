import os.path


class GestionContactos:
    NOMBRE_ARHIVO = 'contactos.txt'

    
    def __init__(self):
        self.contactList = []
        # Reviso si existe archivo contactos.txt
        # Si existe obtengo los contactos del archivo con el método obtener
        if os.path.isfile(self.NOMBRE_ARHIVO):
            self.contactList = self.obtener_contactos()

    
    def obtener_contactos(self):
        contactList = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo
                for linea in archivo:
                    # Uso Strip para  eliminar caracteres en blanco delante o detras.
                    # Uso Split para usar el separador coma como separador entre valores de cada variable
                    #  y asignar los valores a cada variable en una tupla
                    id_contacto, nombre, telefono, email = linea.strip().split(',')
                    contacto = Contacto(nombre, telefono, email)
                    contactList.append(contacto)
                
        except Exception as e:
            print (f'Error al leer archivo contactos: {e}')
        return contactList
    
    
    def guardar_contacto_archivo(self, contactList):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo:
                for contacto in contactList:
                    archivo.write(f'{contacto.escribir_contacto()}\n')

        except Exception as e:
            print(f'Error al guardar contactos en archivo: {e}')
                                                       

    def agregar_contactos(self, nombre, telefono, email):
        self.contactList.append([contacto])
        self.guardar_contacto_archivo([contacto])

    
    def mostrar_contactList(self):
        print (' ----   Contactos en el fichero  ----')
        for contacto in self.contactList:
            print(contacto)

    
    def get_contactList(self):
        return self.contactList