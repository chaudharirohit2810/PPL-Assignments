
# This exception occurs when we try to devide by 0
try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: ')) # Enter zero to get exception
    ans = a / b
    print(ans)
except ZeroDivisionError as e:
    print('Error:',e)