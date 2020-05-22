def isArmstrong(a):
    temp = a
    count1 = count(a)
    res = 0
    while a != 0:
        t = a % 10
        a = int(a / 10)
        res += int(pow(t, count1) + 0.5)
    return res == temp

def count(a):
    k = 0
    while a != 0:
        k = k + 1
        a = int(a/10)
    return k

print('Enter Range: ')
a = int(input())
b = int(input())
ans = []
print('Armstrong numbers in range', a, 'to', b, ': ')
for i in range(a, b + 1):
    if isArmstrong(i):
        print(i)
