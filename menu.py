class menuOpciones:
    __opcion: int
    def __init__(self):
        self.__opcion = 0

    def opciones(self, listasabores, listahelados):
        while self.__opcion != 6:
            print("Menu de opciones: ")
            print("1)- Registrar un helado vendido.")
            print("2)- Mostrar el nombre de los 5 sabores de helado más pedidos.")
            print("3)- Ingresar un número de sabor y estimar el total de gramos vendidos.")
            print("4)- Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos")
            print("5)- Determinar el importe total recaudado por la Heladería, por cada tipo de helado")
            print("6)- Salir")
            self.__opcion = (int(input("Ingrese una opcion: ")))
            
            if self.__opcion == 1:
                listahelados.registrarHelado(listasabores)

            elif self.__opcion == 2:
                listahelados.saboresMasPedidos()

            elif self.__opcion == 3:
                listasabores.mostrarSabores()
                ingsabor = int(input("Ingrese un numero de sabor para estimar el total de gramos vendidos: "))
                listahelados.calcularGramos(ingsabor)

            elif self.__opcion == 4:
                tipohelado = float(input("Ingrese un tipo de helado (100gr, 150 gr, 250 gr, 500 gr o 1000gr): "))
                listahelados.mostrarSaboresTamano(tipohelado)

            elif self.__opcion == 5:
                listahelados.determinarRecaudacion()