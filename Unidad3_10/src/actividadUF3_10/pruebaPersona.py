from Persona import Persona

persona1 = Persona("12345678R", "pepito", 40)
persona2 = Persona("98765432R", "pepita", 35)

print(persona1)
print(persona2)

val = int(input("Cuanto quieres incrementar? "))
persona1.incrementarEdad(val)
persona2.incrementarEdad(val)

print(persona1)
print(persona2)
