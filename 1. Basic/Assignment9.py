import math
def findDivisors(a):
    l = []
    k = 0
    for i in range(1, int(math.sqrt(a) + 0.5) + 1):
        if a % i == 0:
            l.append(i)
            if a != 1:
                l.append(int(a / i))
            k = k + 2
            if a == 1:
                k = k - 1
    return l, k

def harmonicMean(v, k):
    sum = 0.0
    for i in range(0, k):
        sum = sum + 1 / v[i]
    return float(k / sum)
k = 1
i = 1
print('Harmonic Divisor Numbers are : ')
while k != 11:
    v, count = findDivisors(i)
    v1 = harmonicMean(v, count)
    if v1 - int(v1) == 0:
        print(k,'. ', i, sep='')
        k = k + 1
    i = i + 1
