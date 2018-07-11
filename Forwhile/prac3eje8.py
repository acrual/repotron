# Dadas las edades y alturas de 5 alumnos, mostrar la edad y la estatura media,
# la cantidad de alumnos mayores de 18 años, y la cantidad de alumnos que miden más de 1.75.

sumAlturas = 0
contAltos = 0

for i in range(5):
    print("Dame la altura",i+1,":", end=" ")
    alt = float(input())
    sumAlturas = sumAlturas + alt
    if alt > 1.75:
        contAltos = contAltos + 1

sumEdades = 0
contEdad = 0
for i in range(2,7):
    print("Dame la edad",i+1,":", end=" ")
    eda = int(input())
    sumEdades = sumEdades + eda
    if eda >= 18:
        contEdad = contEdad + 1
print("La altura media es :", sumAlturas/5)
print("hay ",contAltos,"altos")
#división real
print("La edad media (real) es: ", sumEdades/5)
#división entera
print("La edad media (entero) es:", sumEdades//5)
print("hay ",contEdad,"adultos")
