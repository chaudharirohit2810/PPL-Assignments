import io

# If tried to open the file which requires permission such as /lib/test.txt
file = input('Enter file path: ')
try:
    fp = open(file, "w")
    fp.write("Rohit")
except PermissionError as e:
    print('Try to run with sudo!! Error: ', e)
