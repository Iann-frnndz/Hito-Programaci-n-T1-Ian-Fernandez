'''CUESTIÓN 1: Mostrar figuras por pantalla (2,5 puntos): a través de un menú solicitaremos al
usuario que tipo de figura quiere mostrar (1-Cuadrado|2-Rectángulo), si la opción no es
correcta, se mostrará mensaje de error y se volverá a solicitar hasta que se correcta.
▪ Si ha seleccionada un cuadrado, pediremos su lado y mostraremos la figura, su área y
perímetro
▪ Si ha seleccionada un rectángulo, pediremos base y altura y mostraremos la figura, su área y
perímetro.'''


#Generamos lo que vamos a llamar el menú que se mostrará cada vez que el usuario inicie el programa o imprima una opción no valida

print("1)Cuadrado")
print("2)Rectangulo")
print("3)Salir")

#comenzamos el programa preguntando que figura se desea imprimir 

pregunta= int(input("Que figura desea imprimir?: "))

#si la respuesta ingresada por el usuario no es ni 1 ni 2 escribimos un bucle 

while pregunta != 1 and pregunta !=2:

    # si la respuesta es exactamente 3 el programa terminará sin ejecutar nada más

    if pregunta==3: 
        break
    else:
        #en cambio si el usuario ingresa un numero no valido volvemos a imprimir el menú y volveremos a preguntar al usuario.

        print("ERROR ingrese una opción valida")
        print("1)Cuadrado")
        print("2)Rectangulo")
        print("3)Salir")
        pregunta=int(input("Que figura desea imprimir?: "))
    
#si la respuesta del usuario es "1" imprimiremos un cuadrado
if pregunta==1:
#le pedimos el lado del cuadrado que queremos imprimir
    lado= int(input("Cual es el su lado?: "))
    for i in range (1,lado+1): #para que imprima las columnas
        for j in range (1,lado+1): #para que imprima las filas
            print("*", end=" ")
        print(" ") #para que haya espacios entre los "*" y quede más visual
        #ahora imprimimos su área y perímetro con calculos sencillos
    print(f"El area de este cuadrado es: {lado*lado} y su perímetro es: {lado*4}")

#si la respuesta del usuario es "2" imprimiremos un rectángulo

elif pregunta==2:
#le pedimos al usuario la base y la altura del rectángulo
    base=int(input("Cual es la base de tu rectángulo?: "))
    altura=int(input("Cual es la altura de tu rectángulo?: "))
    for i in range (1, altura+1):#para que imprima las columnas
        for j in range (1, base+1):#para que imprima las filas
            print("*", end=" ") 
        print(" ")#para que haya espacios entre los "*" y quede más visual
     #ahora imprimimos su área y perímetro con calculos sencillos
    print(f"El área de tu rectángulo es {base*altura} y su perímetro es {base*2+altura*2}")

    