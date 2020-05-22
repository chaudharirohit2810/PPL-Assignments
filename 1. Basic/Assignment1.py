
def eats(a, b):
    if a == 'goat' and b == 'tiger':
        return True
    if a == 'goat' and b == 'bundle of grass':
        return True
    return False


def isSafe(list):
    if len(list) == 3:
        return True
    for i in list:
        for j in list:
            if eats(i, j):
                return False
    return True

def printBank1(list):
    print('Animals at bank1 are', end=': ')
    for i in list:
        print(i, end=', ')
    print()

def printBank2(list):
    print('Animals at bank2 are', end=': ')
    for i in list:
        print(i, end=', ')
    print()

bank1 = ['bundle of grass', 'goat', 'tiger']
bank2 = []

while len(bank2) != 3:
    for i in bank1:
        printBank1(bank1)
        printBank2(bank2)
        v = bank1.pop()
        bank2.append(v)
        print('Bank1 to Bank2 : Farmer ->', v)
        if not isSafe(bank2):
            i = bank2.pop(0)
            print('Bank2 to Bank1: Farmer ->', i)
            bank1.insert(0, i)

print('\033[1mResult:')
printBank1(bank1)
printBank2(bank2)

