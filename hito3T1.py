'''CUESTION 3: Simular el funcionamiento de una cuenta bancaria (2.5 puntos): al iniciar el
programa, pediremos el saldo inicial de la cuenta (puede ser un número decimal), si el saldo es
menor que 0 se volverá a pedir hasta que sea correcto.
Posteriormente mostraremos un menú con las opciones, 1-ingresar dinero, 2-retirar dinero y
3- mostrar saldo y 4-salir, si la opción no es correcta se volver a pedir de nuevo hasta que sea
correcta. No se pueden ingresar cantidades negativas y no podemos retirar dinero si nos
quedamos en números rojos.
Máxima puntuación (3 puntos): incluir una opción más en el menú, estadísticas, que nos
muestre cuantos ingresos y retiradas se han efectuado'''

#inicializamos  algunos valores que nos servirán más adelante
contador_mas=0
contador_menos=0

#le damos la bienvenida al usuario y le preguntamos cual es el saldo
print("Bienvenido gracias por contar con nuestro servicio!")
saldo= float(input("Cual es el saldo de la cuenta?: "))

#solo permitimos un saldo mayor que 0 

while saldo<0:
    saldo= float(input("Cual es el saldo d ela cuenta?: "))

#creamos el menu y lo imprimimos 

menu=["Ingresar dinero", "Retirar dinero", "Mostrar saldo", "Salir", "Estadisticas"]
for i, opcion in enumerate(menu,1):
    print (f"{i}- {opcion}")

#le preguntamos al usuario que opcion desea 
#si no es una opción entre el 1 y el 5 no permitimos que este opere
elegir= int(input("Elige una opción valida: "))
while elegir not in range (1,5):

    elegir= int(input("ERROR Elige una opción valida: "))

#mientras la opción sea valida podemos continuar
while elegir!=4:
    #si el usuario elige la opción 1 podrá ingresar dinero y además saldrá su nuevo saldo
    if elegir==1:
        print("INGRESAR DINERO")
        print (f"Su saldo es: {saldo}")
        mas=float(input("Introduzca el dinero que desea ingresar a su saldo: "))
        saldo_mas=saldo+mas
        print(f"Su nuevo saldo es: {saldo_mas}")
        saldo=saldo_mas
        contador_mas=contador_mas+1 #lo utilizaremos en la opción 5
        
    #si el usuario elige la opción 2 podrá retirar dinero y además saldrá su nuevo saldo
    elif elegir ==2:
        print("RETIRAR DINERO")
        print (f"Su saldo es: {saldo}")
        menos=float(input("Introduzca el dinero que desea retirar de su saldo: "))
        while menos>saldo:
            print("Saldo insuficiente")
            menos=float(input("Introduzca el dinero que desea retirar de su saldo: "))
        saldo_menos=saldo-menos
        print(f"Su nuevo saldo es: {saldo_menos}")
        saldo=saldo_menos
        contador_menos=contador_menos+1 #lo utilizaremos en la opción 5
        
    #si el usuario elige la opción 3 podrá revisar su saldo 
    elif elegir==3:
        print("MOSTRAR SALDO")
        print (f"Su saldo es: {saldo}")
        
    #si el usuario elige la opción 5 podrá revisar cuantos ingresos y retiradas ha realizado
    elif elegir==5:
        print("ESTADÍSTICAS")
        print(f"se han realizado {contador_mas} ingresos y {contador_menos} retiradas de dinero")
        

    elegir= int(input("Elige una opción valida: "))
    
#si el usuario elige la opción 4 saldrá del sistema
if elegir==4:
    print("SALIR")
    print("Gracias por utilizar nuestros servicios!")