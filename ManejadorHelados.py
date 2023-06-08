from claseHelado import Helado
from ManejadorSabores import ManejaSabores
from collections import Counter

class ManejaHelados:
    __listaHelados: list
    def __init__(self):
        self.__listaHelados = []

    def registrarHelado(self, listaSabores):
        gramos = float(input("Ingrese la cantidad de gramos del helado (100gr, 150 gr, 250 gr, 500 gr y 1000gr): "))
        if gramos > 1000 and gramos < 100:
            print("Cantidad de gramos no valida.")
        else:
            precio = float(input("Ingrese el precio del helado: "))
            helado = Helado(gramos, precio)
            cantsabores = int(input("Ingrese la cantidad de sabores 1...4: "))
            if cantsabores > 0 and cantsabores < 5:
                listaSabores.mostrarSabores()
                for i in range(cantsabores):
                    idsabor = int(input("Ingrese el numero id del sabor: "))
                    sabor = listaSabores.buscarSabor(idsabor)
                    helado.addSabor(sabor)
                self.__listaHelados.append(helado)

    def saboresMasPedidos(self):
        print("Sabores de helado mas pedidos: ")
        saboresContador = Counter()
        for helado in self.__listaHelados:
            for sabor in helado.getSabores():
                    saboresContador[sabor] += 1
        saboresOrdenados = saboresContador.most_common(5)
        for sabor, contador in saboresOrdenados:
                print("{}: {} veces".format(sabor, contador))

    def mostrarHelados(self):
        for helado in self.__listaHelados:
            print(helado)

    def calcularGramos(self, ingsabor):
        acumgramos = 0
        for helado in self.__listaHelados:
            for sabor in helado.getSabores():
                if(sabor.getIdSabor() == ingsabor):
                    acumgramos += helado.estimarGramos()
        print("La cantidad de gramos para el sabor {} es: {}".format(ingsabor, acumgramos))



    def mostrarSaboresTamano(self, ingtipo):
        print("||-----Sabores vendidos para helados del tipo {}gr-----||:".format(ingtipo))
        saboresMostrados = ''
        for helado in self.__listaHelados:
            if helado.getGramos() == ingtipo:
                for sabor in helado.getSabores():
                    if sabor.getNombre() not in saboresMostrados:
                        print("\t{}".format(sabor.getNombre()))
                        saboresMostrados += sabor.getNombre() + ', '

    def determinarRecaudacion(self):

        recaudacion100gr = 0
        recaudacion150gr = 0
        recaudacion250gr = 0
        recaudacion500gr = 0
        recaudacion1000gr = 0

        for helado in self.__listaHelados:
            if helado.getGramos() == 100:
                recaudacion100gr += helado.getPrecio()
            elif helado.getGramos() == 150:
                recaudacion150gr += helado.getPrecio()
            elif helado.getGramos() == 250:
                recaudacion250gr += helado.getPrecio()
            elif helado.getGramos() == 500:
                recaudacion500gr += helado.getPrecio()
            elif helado.getGramos() == 1000:
                recaudacion1000gr += helado.getPrecio()

        print("La recaudación para el tipo {}gr es: {}".format(100, recaudacion100gr))
        print("La recaudación para el tipo {}gr es: {}".format(150, recaudacion150gr))
        print("La recaudación para el tipo {}gr es: {}".format(250, recaudacion250gr))
        print("La recaudación para el tipo {}gr es: {}".format(500, recaudacion500gr))
        print("La recaudación para el tipo {}gr es: {}".format(1000, recaudacion1000gr))




#def determinarRecaudacion(self):
#    recaudacionxtipo = {}
#    for helado in self.__listaHelados:
#        tipohelado = helado.getGramos()
#        preciohelado = helado.getPrecio()
#        if tipohelado in recaudacionxtipo:
#            recaudacionxtipo[tipohelado] += preciohelado
#        else:
#            recaudacionxtipo[tipohelado] = preciohelado
#    
#    for tipo, recaudacion in recaudacionxtipo.items():
#        print("La recaudación para el tipo {}gr es: {}".format(tipo, recaudacion))