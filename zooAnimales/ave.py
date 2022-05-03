from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    totalAves = 0
    aguilas = 0
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.totalAves+=1
        self.listado.append(self)
        
    def movimiento(self):
        return "volar"
        
    def setColorPlumas(self,a): 
        self._colorPlumas=a
    
    def getColorPlumas(self):
         return self._colorPlumas

## metodos de clase
    
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return Ave(nombre, edad, "montañas", genero,"cafe glorioso")
        
    @classmethod
    def crearAguila(cls,nombre, edad, genero):
        cls.aguilas += 1
        return Ave(nombre, edad, "montañas", genero, "blanco y amarillo")
    
    @classmethod
    def cantidadAves(cls): 
        return cls.totalAves