from ManejadorHelados import ManejaHelados as MH
from ManejadorSabores import ManejaSabores as MS
from menu import menuOpciones

listasabores = MS ()
listasabores.cargarSabores()
listahelados = MH()
menu = menuOpciones()
menu.opciones(listasabores,listahelados)

