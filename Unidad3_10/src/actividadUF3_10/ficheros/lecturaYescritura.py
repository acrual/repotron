fichero = open("ejemplo4.txt","a+")
while True:
    fichero.seek(0)
    leerEscribir = input("Quieres escribir o leer?(e/l): ")
    while leerEscribir != "e" and leerEscribir != "l":
        leerEscribir = input("Error. Quieres escribir o leer?(e/l): ")

    if leerEscribir == "e":
        nuevaLinea = "a"
        while nuevaLinea != "":
            nuevaLinea = input("Escribe la nueva línea o deja en blanco: ")
            fichero.write(nuevaLinea + "\n")
    else:
        linea = fichero.readline()
        while linea != "":
            print(linea, end="")
            linea = fichero.readline()

    continuar = input("Quieres continuar?(s/n): ")
    if continuar == "n":
        break
