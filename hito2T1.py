'''CUESTIÓN 2: Juego de piedra papel o tijera (2,5 puntos). El usuario introduce un valor (1-
Piedra|2- Papel|3-Tijera), si no es correcto se volver a pedir de nuevo hasta que se correcta.
La “maquina” generará un valor aleatorio (de 1 a 3) para elegir piedra, papel o tijera. Al
finalizar, mostrará la opción del usuario y de la máquina e indicará si hemos ganado, perdido o
empatado.'''

#inicializamos los valores

P="Piedra"
Pa="Papel"
T="Tijera"

import random #importamos un random para que se pueda generar el numero random
#generamos el menú
menu= ["Piedra", "Papel", "Tijera"]
for i,valor in enumerate(menu,1):
    print(f"{i}- {valor}")

#le pedimos al usuario un valor del 1 al 3
usuario= int(input("Introduzca un valor del 1 al 3 dadas las opciones: "))
#en caso de que el valor introducido por el usuario no sea del 1 al 3 dará error y volverá a preguntarlo
while usuario != 1 and usuario !=2 and usuario!= 3:
    print("ERROR, escoja un valor válido ")
    usuario= int(input("Introduzca un valor del 1 al 3 dadas las opciones: "))

#si el usuario introduce 1 tenemos que hacer que la maquina genere un numero random y en el caso de que gane imprima ganar, en caso de empate imprima empate y en caso de perder impirma perdiste.  
  
if usuario ==1:
    numero_maquina= random.randint(1, 3)
    print(f"Tu: {P}")
    if numero_maquina==1:
            print(f"Máquina: {P}")
            resultado=print ("Empate")
    elif numero_maquina==2:
            print(f"Máquina: {Pa}")
            resultado=print ("Perdiste")
    elif numero_maquina==3:
        print(f"Máquina: {T}")
        resultado=print ("Ganaste!!")
#si el usuario introduce 2 tenemos que hacer que la maquina genere un numero random y en el caso de que gane imprima ganar, en caso de empate imprima empate y en caso de perder impirma perdiste. 
       
elif usuario==2:
    numero_maquina= random.randint(1, 3)
    print(f"Tu: {Pa}")
    if numero_maquina==1:
        print(f"Máquina: {P}")
        resultado=print ("Ganaste!!")
    elif numero_maquina==2:
        print(f"Máquina: {Pa}")
        resultado=print ("Empate")
    elif numero_maquina==3:
        print(f"Máquina: {T}")
        resultado=print ("Perdiste")

#si el usuario introduce 3 tenemos que hacer que la maquina genere un numero random y en el caso de que gane imprima ganar, en caso de empate imprima empate y en caso de perder impirma perdiste.
        
elif usuario==3:
    numero_maquina= random.randint(1, 3)
    print(f"Tu: {T}")
    if numero_maquina==1:
        print(f"Máquina: {P}")
        resultado=print ("Perdiste")
    elif numero_maquina==2:
        print(f"Máquina: {Pa}")
        resultado=print ("Ganaste!!")
    elif numero_maquina==3:
        print(f"Máquina: {T}")
        resultado=print ("Empate")


    


