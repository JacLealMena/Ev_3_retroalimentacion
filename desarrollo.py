import os, msvcrt
from funciones import *
while True:
    print("""
          GAXPLOSIVE
          1. Registrar pedido
          2. Listar todos los pedidos
          3. Buscar pedido por rut
          4. Imprimir hoja de ruta
          5 Salir del programa""")
    opc = input("> ")
    os.system("cls")
    if opc == "1":
        registrar_pedido()
    elif opc == "2":
        listar_pedido()
    elif opc == "3":
        buscar_pedido_rut()
    elif opc == "4":
        imprimir_hoja_ruta()
    elif opc == "5":
        salir()
    else:
        print(">>> Opción inválida! <<<")