numAdivinar = 10
num = int(input("Introduce número : "))
while num != numAdivinar:
    if num < numAdivinar:
        print("Un poco más alto ")
    elif num > numAdivinar:
        print("Un poco más bajo ")
    num = int(input("Introduce número : "))
print("ACERTASTE!!")
