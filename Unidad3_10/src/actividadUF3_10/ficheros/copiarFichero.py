rutaOrigen = input("Dime el fichero origen: ")
rutaDestino = input("Dime el fichero destino: ")

try:
    fichero1 = open(rutaOrigen, "r")
    fichero2 = open(rutaDestino, "w")
    linea = fichero1.readline()
    conteo = 1
    while linea != "":
        if conteo % 2 == 0:
            fichero2.write(linea)
            print(linea)
        linea = fichero1.readline()
        conteo = conteo + 1
except FileNotFoundError:
    print("ERROR al abrir alguno de los ficheros")
finally:
    if not(fichero1.closed):
        fichero1.close()
    if not(fichero2.closed):
        fichero2.close()
