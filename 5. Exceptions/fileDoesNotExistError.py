import io

# File does not exist exception when passes file that does not exist in given directory
file = input('Enter file path: ')
try:
    # If file exists
    fp = open(file)
    print('File opened successfully')
except IOError as e:
    # If file does not exist
    print('Error: ', e)
