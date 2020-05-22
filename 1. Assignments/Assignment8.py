def decomposeMatrix(a, n):
    l = []
    u = []
    for i in range(0, n):
        b = []
        for j in range(0, n):
            b.append(0)
        l.append(b)

    for i in range(0, n):
        b = []
        for j in range(0, n):
            b.append(0)
        u.append(b)

    for i in range(0, n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += l[i][j] * u[j][k]
            u[i][k] = a[i][k] - sum
        for k in range(i, n):
            if i == k:
                l[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += l[k][j] * u[j][i]
                l[k][i] = int((a[k][i] - sum) / u[i][i])
    return l, u;


def printMatrix(a):
    for i in range(0, 3):
        for j in range(0, 3):
            print(a[i][j], end='\t')
        print()

a = []
b = []
for i in range(0, 3):
    b = []
    for j in range(0, 3):
        v = int(input())
        b.append(v)
    a.append(b)
l, u = decomposeMatrix(a, 3)
print('Original Matrix is : ')
printMatrix(a)
print()
print('L matrix is : ')
printMatrix(l)
print()
print('U matrix is : ')
printMatrix(u)
print()
