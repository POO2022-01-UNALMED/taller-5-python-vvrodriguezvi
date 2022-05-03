from zooAnimales.animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    totalPeces = 0
    bacalaos = 0
    
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.totalPeces+=1
        self.listado.append(self)

    def movimiento(self):
        return "nadar"
       
    def setColorEscamas(self,a): 
        self._colorEscamas=a
    
    def getCantidadAletas(self):
         return self._cantidadAletas

    def getColorEscamas(self): 
        return self._colorEscamas
    
    def setCantidadAletas(self,a):
         self._cantidadAletas=a

    #Metodos de clase 

    @classmethod
    def cantidadPeces(cls): 
        return cls.totalPeces 
    
    @classmethod
    def crearBacalao(cls,nombre, edad, genero):
        cls.bacalaos+=1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones+=1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)
        
