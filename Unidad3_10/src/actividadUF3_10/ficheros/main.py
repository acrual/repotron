fichero = open("ejemplo1.txt","r")
linea = fichero.readline()
while linea != "":
    print(linea)
    linea = fichero.readline()
