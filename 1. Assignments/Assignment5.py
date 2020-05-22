def isPresent(v, a):
    for i in range(0, len(v)):
        if a == v[i]:
            return True
    return False

l = [2, 4, 5, 6, 12, 16, 17, 20, 21]

print('Missing page numbers are: ')
for i in range(1, 26):
    if not isPresent(l, i):
        print(i)
