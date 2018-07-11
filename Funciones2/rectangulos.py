#pedir base y altura y dibujar rectángulo
base = int(input("Dame la base: "))
altura = int(input("Dame la altura: "))
while base <= 0 or altura <= 0:
    base = int(input("Error. Dame la base: "))
    altura = int(input("Dame la altura: "))

print("Rectángulo normal : ")

for i in range(1, altura + 1):
    for j in range(1, base + 1):
        print("* ",end="")
    print("")

print("Rectángulo invertido : ")

for i in range(1, base + 1):
    for j in range(1, altura + 1):
        print("* ",end="")
    print("")
