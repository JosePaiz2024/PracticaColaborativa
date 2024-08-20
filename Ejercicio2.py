class Libro():
    def __init__(self, tipo):
        self.tipo = tipo

class Novela(Libro):
    def __init__(self, tipo, autor):
        super().__init__(tipo)
        self.autor = autor

editoria1 = Novela("Romantica", "William Shakespire")
print(f"autor: {editoria1.autor}")
print(f"tipo: {editoria1.tipo}")