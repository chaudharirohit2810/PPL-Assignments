a = int(input('Enter value of a : '))
r = int(input('Enter value of r : '))

print('First 10 elements of geometric series are : ')
for i in range(0, 10):
    temp = a * pow(r, i)
    print(temp)

