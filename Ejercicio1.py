class Animal():
    def __init__(self, estado):
        self.estado = estado

class Perro(Animal):
    def __init__(self, estado, nombre):
        super().__init__(estado)
        self.nombre = nombre

perrito = Perro("Doméstico", "Rex")
print(f"Animal: Perro")
print(f"Estado: {perrito.estado}")
print(f"Nombre: {perrito.nombre}")


    
