# hacer triángulos de números pidiendo un lado
h = int(input("Dame la altura: "))
while h <= 0:
    h = int(input("Error. Dame la altura: "))

for i in range(1,h+1):
    for j in range(1, h - i + 1):
        print(" ",end="")
    for j in range(1, i+1):
        print(j,end="")
    print("")
