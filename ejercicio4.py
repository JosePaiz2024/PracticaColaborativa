class Dispositivo():
    def __init__(self,tipo):
        self.tipo = tipo

    def info(self):
        return("DISPOSITIVO\n"+
               f"Dispositivo: {self.tipo}\n")
        
    
class tienda(Dispositivo):
    def __init__(self, tipo,clase):
        super().__init__(tipo)
        self.clase=clase

    def info(self):
        desc = super().info()
        print(f"{desc}Tipo: {self.clase}")

disp = tienda("Computadora","Portatil")
disp.info()