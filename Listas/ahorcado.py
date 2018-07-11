# juego del ahorcado

def mostrarMenu():

    print("")
    print("Menu :")
    print("1. Jugar partida")
    print("2. Muestra estadisticas")
    print("0. Salir")
    opcion = int(input("Escoge opcion : "))
    while opcion != 0 and opcion != 1 and opcion != 2:
        opcion = int(input("Error, por favor escoge la opcion correcta : "))
    return opcion

def encuentraLetra(letra, lista):
    i = 0
    enc = False
    while not enc and i < len(lista):
        if letra == lista[i]:
            enc = True
        else:
            i = i + 1
    return enc

def mostrarPalabra(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print("")

def pedirLetra():
    letra = input("Dame una letra : ")
    while letra < 'a' or letra > 'z':
        letra = input("Dame una letra minúscula correcta : ")
    return letra

def destaparLetra(letra, lista, pal):
    cont = 0
    for i in range(len(lista)):
        if letra == lista[i]:
            pal[i] = lista[i]
            cont = cont + 1
    return cont

def jugarPartida():
    palabra = ["c","a","c","e","r","o","l","a"]
    adivinanza = []
    letras_usadas = []
    for i in range(len(palabra)):
        adivinanza.append('*')

    hasGanado = True
    asteriscos = len(adivinanza)
    vidas = 5

    while vidas > 0 and asteriscos > 0:
        print("Te quedan ", vidas, " vidas ")
        if len(letras_usadas) > 0:
            print("Has usado las letras : ", end= " ")
            for i in range(len(letras_usadas)):
                print(letras_usadas[i], end = " ")
        print("")
        mostrarPalabra(adivinanza)

        letra = pedirLetra()
        while letra in letras_usadas:
            print("Ya has usado esa letra. ", end =" ")
            letra = pedirLetra()
        letras_usadas.append(letra)

        if encuentraLetra(letra,palabra):
            print("La letra ",letra,"está en la palabra")
            asteriscos = asteriscos - destaparLetra(letra, palabra, adivinanza)
        else:
            print("Fallaste")
            vidas = vidas - 1


    if vidas > 0:
        return True
    print("La palabra era ", end=" ")
    mostrarPalabra(palabra)
    return False

def mostrarEstadisticas(partidasJugadas, partidasGanadas, partidasPerdidas):
    print("Has ganado ", partidasGanadas, " partidas")
    print("Has perdido ", partidasPerdidas, " partidas")
    print("Has jugado ", partidasJugadas, " partidas")

jugadas = 0
ganadas = 0
perdidas = 0

opcion = 1
while opcion != 0:

    opcion = mostrarMenu()
    if opcion == 1:
        if jugarPartida():
            print("Has ganado")
            ganadas = ganadas + 1
        else:
            print("")
            print("Has palmado")
            perdidas = perdidas + 1
        jugadas = jugadas + 1

    elif opcion == 2:
        mostrarEstadisticas(jugadas, ganadas, perdidas)

    else:
        print("Adiós")

print("Muchas gracias por jugar")
print("")
