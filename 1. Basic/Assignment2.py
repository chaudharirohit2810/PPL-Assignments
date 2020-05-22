import random
while 1:
    print('Enter your choice: \n1. Play \n2. Quit')
    a = int(input())
    if a == 1 :
        print(random.randint(0, 6))
    else :
        break
print('Thank You!!')