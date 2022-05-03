class Animal:
    _totalAnimales = 0
    
    def __init__(self,nombre,edad,habitat,genero,zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    def movimiento():
        return "desplazarse"   
    
    def toString(self):
        if self._zona is not None: 
            return "Mi nombre es "+self.getNombre()+", tengo una edad de "+str(self.getEdad())+", habito en "+self.getHabitat()+" y mi genero es "+self.getGenero()+", la zona en la que me ubico es "+self.getZona()+", en el zoo "+"PENDIENTE"
        else:
            return "Mi nombre es "+self.getNombre()+", tengo una edad de "+str(self.getEdad())+", habito en "+self.getHabitat()+" y mi genero es "+self.getGenero()

    
    def setNombre(self,a): 
        self._nombre=a
    
    def getNombre(self): 
        return self._nombre
    
    def setEdad(self,a): 
        self._edad=a
    
    def getEdad(self): 
        return self._edad
    
    def setHabitat(self,a): 
        self._habitat=a
    
    def getHabitat(self): 
        return self._habitat
    
    def setGenero(self,a): 
        self._genero=a
    
    def getGenero(self): 
        return self._genero
    
    def setZona(self,a): 
        self._zona=a
    
    def getZona(self): 
        return self._zona
 
## metodos de clase

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    @classmethod
    def totalPorTipo(cls):
        hijos = cls.__subclasses__()
        return "Mamiferos : "+str(hijos[0].cantidadMamiferos())+"\nAves : "+str(hijos[1].cantidadAves())+"\nReptiles : "+str(hijos[2].cantidadReptiles())+"\nPeces : "+str(hijos[3].cantidadPeces())+"\nAnfibios : "+str(hijos[4].cantidadAnfibios())
        
    @classmethod
    def cantidadAnfibios(cls): return cls._totalAnfibios 