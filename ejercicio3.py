class Pelicula():
    def __init__(self,gene,tiem,clas):
        self.genero = gene
        self.tiempo = tiem
        self.clasificacion = clas

    def info(self):
        return("PELICULA\n"+
               f"Genero: {self.genero}\n"+
               f"Tiempo: {self.tiempo} min\n"+
               f"Clasificacion: {self.clasificacion} años\n")
        
    
class cine(Pelicula):
    def __init__(self, gene, tiem, clas, proc):
        super().__init__(gene, tiem, clas)
        self.procedencia=proc

    def info(self):
        cartelera = super().info()
        print(f"{cartelera}Procedencia: {self.procedencia}")

cartel = cine("Humor",125,"16","Colombia")
cartel.info()

    
