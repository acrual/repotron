# pide un lado y escribe 3 asteriscos en horizontal y vertical
lado = int(input("Dame el lado :"))
while lado < 1:
    lado = int(input("Error. Dame el lado :"))

for i in range(1,lado + 1):
    print("*",end = "")

print("")
for i in range(1,lado + 1):
    print("*")
