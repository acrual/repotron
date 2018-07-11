for j in range(1,1000):
    sum = 0
    for i in range(2,j):
        if (j%i) == 0:
            # print(i, "es divisor de",j)
            sum = sum + 1
    if sum == 0:
        print(j, "es primo")
