class Persona:
    def __init__(self, edad, nombre, telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono

class Cliente(Persona):
    def __init__(self, edad, nombre, telefono, credito):
        super().__init__(edad, nombre, telefono)
        self.credito = credito

class Trabajador(Persona):
    def __init__(self, edad, nombre, telefono, salario):
        super().__init__(edad, nombre, telefono)
        self.salario = salario

cliente1 = Cliente(30, "Juan Perez", "555-1234", 5000)
print("Nombre: ", cliente1.nombre)
print("Edad: ", cliente1.edad)
print("Teléfono: ", cliente1.telefono)
print("Crédito: ", cliente1.credito)

trabajador1 = Trabajador(25, "Maria Garcia", "555-5678", 10000)
print("Nombre: ", trabajador1.nombre)
print("Edad: ", trabajador1.edad)
print("Teléfono: ", trabajador1.telefono)
print("Salario: ", trabajador1.salario)
