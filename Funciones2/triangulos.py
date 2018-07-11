# pide una altura y dibuja un triángulo
altura = int(input("Dame la altura : "))
while altura <= 0:
    altura = int(input("Error. Dame la altura : "))

for i in range(1,altura + 1):
    for j in range(1, i + 1):
        print("* ",end="")
    print("")
