class Sabor:
    __idSabor: int
    __nombreSabor:str
    __ingredientes: str

    def __init__(self, idsabor, nombre, ingredientes):
        self.__idSabor = idsabor
        self.__nombreSabor = nombre
        self.__ingredientes = ingredientes

    def getIdSabor(self):
        return self.__idSabor
    
    def getNombre(self):
        return self.__nombreSabor
    
    def getIngredientes(self):
        return self.__ingredientes
    
    def __str__(self):
        return str(self.__idSabor) + ": " + self.__nombreSabor