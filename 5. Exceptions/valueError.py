
# This exception occurs when user tries to enter 
# input which is not number when number is expected

try:
    value = int(input('Enter a number: '))
    print('Number is: ', value)
except ValueError as e:
    print('Error:', e)