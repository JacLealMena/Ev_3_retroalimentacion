import csv

#Variables
pedidos = []
precio_5k = 12500
precio_15k = 25500
comunas = ("Santiago","Colina","Pirque")

#Funciones Obligatorias
def registrar_pedido():
    print("REGISTRAR PEDIDO")
    print(">> CLIENTE")
    rut = int(input("Ingrese rut: > "))
    nombre = (input("Ingrese nombre: > "))
    direccion = (input("Ingrese dirección: > "))
    comuna = int(input("Ingrese comuna (1: santiago, 2: Colina, 3:Pirque) \n> "))
    print(">> PEDIDO")
    cantidad_5k = 0
    cantidad_15k = 0
    while True:
        print("""
              CILINDROS
              1. 5kg - $12.500
              2. 15kg - $25.500
              3. Terminar pedido
              """)
        opc2 = input("Ingrese cilindro a agregar\n> ")
        if opc2 == "1":
            cantidad = int("Ingrese cantidad\n> ")
            cantidad_5k += cantidad
        if opc2 == "2":
            cantidad = int("Ingrese cantidad\n> ")
            cantidad_15k += cantidad
        if opc2 == "3":
            break
        else:
            print(">>> Opción inválida! <<<")
    total = cantidad_5k*precio_5k + cantidad_15k*precio_15k
    pedido = [rut, nombre, direccion, comunas[comuna-1],cantidad_5k,cantidad_15k,total]
    pedidos.append(pedido)
    print(">> PEDIDO CREADO CON ÉXITO")

def listar_pedido():
    if not pedidos:
        print(">>> NO EXISTEN PEDIDOS <<<")
    else:
        print("LISTA DE PEDIDOS")
        for p in pedidos:
            print("RUT:",p[0])
            print("NOMBRE",p[1])
            print("DIRECCIÓN",p[2])
            print("COMUNA",p[3])
            print("CANT. 5KG",p[4])
            print("CANT. 15KG",p[5])
            print("TOTAL",p[6])

def buscar_pedido_rut():
    if not pedidos:
        print(">>> NO EXISTEN PEDIDOS <<<")
    else:
        print("BUSCAR PEDIDO POR RUT")
        rut_buscar = int(input("Ingrese RUT a buscar\n> "))
        tiene_pedidos = False
        for p in pedidos:
            if rut_buscar == p[0]:
                tiene_pedidos = True
                print("RUT:",p[0])
                print("NOMBRE",p[1])
                print("DIRECCIÓN",p[2])
                print("COMUNA",p[3])
                print("CANT. 5KG",p[4])
                print("CANT. 15KG",p[5])
                print("TOTAL",p[6])
        if tiene_pedidos == False: #if not tiene_pedidos: (tiene_pedidos tiene que ser False)
            print(">> RUT NO EXISTE")

def imprimir_hoja_ruta():
    if not pedidos:
        print(">> NO EXISTEN PEDIDOS")
    else:
        comuna = int(input("Ingrese comuna (1: santiago, 2: Colina, 3:Pirque) \n> "))
        nombre_archivo = input("Ingrese nombre archivo") + ".csv"
        try:    
            with open(nombre_archivo, "x", newline='') as archivo_csv:
                writer = csv.writer(archivo_csv)
                for p in pedidos:
                    if p[3] == comunas[comuna-1]:
                        writer.writerow(p)
            print(">> ARCHIVO CREADO CON ÉXITO")
        except:
            print(">>> ERROR! EL NOMBRE DEL ARCHIVO YA EXISTE! <<<")

#Funciones Extras
def salir():
    print(">> Ha salido")
    exit()

#Faltan las validaciones!!