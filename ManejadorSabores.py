import csv
from claseSabor import Sabor

class ManejaSabores:
    __listaSabores:list
    def __init__(self):
        self.__listaSabores = []
    
    def cargarSabores(self):
        archivo = open('sabores.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            idsabor = int(fila[0])
            nomsabor = str(fila[1])
            ing = str(fila[2])
            instSabor = Sabor(idsabor,nomsabor,ing)
            self.__listaSabores.append(instSabor)
        archivo.close          

    def mostrarSabores(self):
        for sabor in self.__listaSabores:
            print(sabor)

    def buscarSabor(self, idsabor):
        i = 0
        while (i<len(self.__listaSabores)) and (self.__listaSabores[i].getIdSabor() != idsabor):
            i += 1
        return None if i == len(self.__listaSabores) else self.__listaSabores[i]