file  = open('test1.py' , 'w')

try:
    file.write('test 1')
finally:
    file.close()


with open('test2.py', 'w') as file:
    file.write('test 2')