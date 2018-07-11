# FIBONACCI
def fibonacci():
    a = 0
    b = 1
    for i in range(100):
        a = a + b
        b = a + b
        print(a)
        print(b)

print("0")
print("1")
fibonacci()
