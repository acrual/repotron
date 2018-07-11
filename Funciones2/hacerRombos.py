# hacer rombos de lado h
h = int(input("Dame la altura : "))
while h <= 0:
    h = int(input("Error. Dame la altura : "))

# La parte de arriba, que es un triángulo equilátero
for i in range(1, h+1):
    for j in range(1, h - i + 1):
        print("  ",end="")
    for j in range(1, 2 * i):
        print("* ",end="")
    print("")

for i in range(h-1,0,-1):
    for j in range(h-i+1,1,-1):
        print("  ",end="")
    for j in range(1, 2 * i):
        print("* ",end="")
    print("")
#    for i in range(h+1,2*h-1):
#        for j in range(1,)


# i=5 x=5 i = 2*h - 3
# i=6 x=3 i = 2*h - 5
# i=7 x=1 i = 2*h - 7
