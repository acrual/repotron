fichero = open("ejemplo3.txt","w")
nuevaLinea = "a"
while nuevaLinea != "":
    nuevaLinea = input("Escribe la nueva línea: ")
    fichero.write(nuevaLinea + "\n")
fichero.close()
