import math
def sumOfFactors(a):
    res = 1
    for i in range(2, math.ceil(math.sqrt(a))):
        if a % i == 0:
            res += i
            res += int(a / i)
    return res



print('First 10 pairs of Ammicable numbers are')
temp = 0
k = 0
for x in range(1, 100000):
    y = sumOfFactors(x)
    if sumOfFactors(y) == x and x != y and temp != x:
        temp = y
        k = k + 1
        print(k, '. ', x,' ', y, sep='')
    if k == 10 :
        break
