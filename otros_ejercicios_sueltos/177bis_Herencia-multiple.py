# Ejemplo de herencia múltiple en Python
# La herencia múltiple permite que una clase herede de más de una clase base.
# Esto puede ser útil para combinar funcionalidades de diferentes clases.
# Sin embargo, se debe tener cuidado con la ambigüedad que puede surgir si
# las clases base tienen métodos o atributos con el mismo nombre.

class ClasePadre1:
    def metodo1(self):
        return "Método de ClasePadre1"

class ClasePadre2:
    def metodo2(self):
        return "Método de ClasePadre2"

# Clase que hereda de ambas
class ClaseHija(ClasePadre1, ClasePadre2):
    def metodo_hija(self):
        return "Método de ClaseHija"

# Crear un objeto de la clase hija
objeto = ClaseHija()
print(objeto.metodo1())  # Heredado de ClasePadre1
print(objeto.metodo2())  # Heredado de ClasePadre2
print(objeto.metodo_hija())  # Método propio de ClaseHija