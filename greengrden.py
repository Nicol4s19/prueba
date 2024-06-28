import csv
agregar_cliente=True
agregar_compra=True
lista_productos=[]
data=[]
lista_productos_cliente=[]
valor=0
valor_de_venta=0
valor_de_compra=0

def no_valido():
    print("*** NO VALIDO *** Intente de nuevo")

def no_disponible():
    print("*** NO DISPONIBLE *** Intente de nuevo")

def menu_producto():
    print('Productos',
    "Productos:      Valor:",
    "1.Abono         $1200",
    "2.Tierra        $1000",
    "3.Lirio         $1100",
    "4.Rosas Rojas   $1700",
    "5.Margaritas    $1100",
    "6.Salir"
    )

print(" Empresa Green Garden ")
print(" Gestion de pedidos ")

#se solicita la informacion del cliente

while agregar_cliente:
    lista_productos_cliente.clear()
    print("Ingrese datos del cliente:")

    nombre=input("Nombre: ")
    while not nombre.isalpha():
        no_valido()
        nombre=input("Nombre: ")
    
    direccion=input("Ingrese su direccion: ")

    telefono=input("Telefono: ")
    while not telefono.isdigit() or len(telefono)<9 or len(telefono)>9:
        if len(telefono)<9 or len(telefono)>9:
            print("Debe contener 9 digitos porfavor intente nuevamente")
        else:
            no_valido()
        telefono=input("Numero de telefono: ")

#se solicitan los datos de compra del cliente:
        agregar_compra=True
        lista_productos.clear()
        valor_de_venta=0
        while agregar_compra:
            menu_producto()

            producto=input("Ingrese el numero del producto: ")
            if int(producto)==0:
                agregar_cliente=False
            break

        while not producto.isdigit() or int(producto)<0 or int(producto)>5:
            if producto.isdigit():
                if int(producto)<0 or int(producto)>5:
                     no_disponible()

                elif producto.lower()=="m":
                    menu_producto
                else:
                    no_valido
                producto=input("Ingrese el numnero del producto: \nletra'm' para visualizar el menu\n")

        unidades_producto=input("Unidades: ")
        while not unidades_producto.isdigit() or int(producto)<0:
            if unidades_producto.isdigit():
                if int(producto)<0:
                    no_disponible()
            else:
                no_valido()
            unidades_producto=input("unidades: ")
        
        
        if int(producto)==1:
            valor=1200
        elif int(producto)==2:
            valor=1000
        elif int(producto)==3:
            valor=1100
        elif int(producto)==4:
            valor=1700
        elif int(producto)==5:
            valor=1100
valor_de_venta+=valor*int(unidades_producto)
valor_de_compra=valor*int(unidades_producto)

lista_productos_cliente.append([f"code: {producto}", f"units: {unidades_producto}"])
lista_productos.append([f"producto{producto}", f"cantidad: {unidades_producto}", f"valor: {valor_de_compra}$"])

compra=input("Agregar compra: \n1. si\n2. no\n")
while not compra.isdigit() or int(compra) !=1 and int(compra) !=2:
    if not compra.isdigit():
        no_valido()
    elif int(compra) !=1 or int(compra) !=2:
        no_disponible()

        compra=input("Agregar compra: \n1. si\n2. no\n")
        if int(compra)==2:
            agregar_compra=False

data.append([nombre,telefono,direccion,lista_productos_cliente])


print("********boleta********")
print("productos: ")
for i in lista_productos:
    print(i)
    print(f"Precio final: {valor_de_venta}$\n")

nuevo_cliente=input("ingresar nuevo cliente: \n1. si \n2. no\n")
while not nuevo_cliente.isdigit() or int(nuevo_cliente) !=1 or int(nuevo_cliente)!=2:
    if not nuevo_cliente.isdigit():
        no_valido()
    elif int(nuevo_cliente)!=1 or int(nuevo_cliente)!=2:
        no_disponible()
nuevo_cliente=input("ingresar nuevo cliente: \n1. si \n2. no\n")
if int(nuevo_cliente)==2:
    agregar_cliente=False
print("\nSaliendo...")

with open('data.csv' , 'w') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    escritor_csv.writerow(['nombre', 'telefono', 'direccion', 'productos'])

    escritor_csv.writerows(data)