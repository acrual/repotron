# pide una altura y dibuja un triángulo equilátero
altura = int(input("Dame la altura : "))
while altura <= 0:
    altura = int(input("Error. Dame la altura : "))

for i in range(1, altura+1):
    for j in range(1, altura - i + 1):
        print("  ",end="")
    for j in range(1, 2 * i):
        print("* ",end="")
    print("")
