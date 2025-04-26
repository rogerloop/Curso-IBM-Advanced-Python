# Creamos la clase Cliente sobre la que girará la aplicación
# en la definición inicial damos valor None a los atributos para poder crear un Cliente con tan solo el Id

class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

# Agregamos metodo str para poder imprimir en cualquier momento el estado del objeto (o sea sus atributos) 

    def __str__(self):
        return (f'Id: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Membresía: {self.membresia}')
        