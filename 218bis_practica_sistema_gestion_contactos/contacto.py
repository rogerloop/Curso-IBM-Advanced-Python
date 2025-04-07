class Contacto:
    contador_contactos = 0

    def __init__(self, nombre, telefono, email):
        Contacto.contador_contactos += 1
        self.id_contacto = Contacto.contador_contactos
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return (f'Contacto: id_contacto = {self.id_contacto}, nombre = {self.nombre}, '
                f'telefono = {self.telefono}, email = {self.email}')
    
    def escribir_contacto(self):
        return f'{self.id_contacto},{self.nombre},{self.telefono},{self.email}'




    







