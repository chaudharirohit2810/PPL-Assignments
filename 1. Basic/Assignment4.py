import random
a = random.randint(0, 50)
c = 50
flag = False
for i in range(0, 3):
    print('Guess the number: ')
    b = int(input())
    if a == b:
        print('Bravo!! your guess was right')
        flag = True
        break
    else:
        if a <= c:
            print("Number is less than or equal to", c)
        else:
            print("Number is greater than", c)
        c = int(c / 2)

if not flag:
    print('Bad luck!! number was', a)
