# Filename:var.property
# author:liyuan

number = 23
#True if you need
running = False

#while
while running:
        guess = int(input('Enter an integer:'))

        if guess == number:
                print('Congratulations, you guessed it.')
                print("but you do not win any prizes!")
                running = False
        elif guess < number:
                print('No,higher than that')
        else:
                print('NO, lower than that')
        print('is Done')		
else:
        print('while is done')


#for
for i in range(1,5):
        print(i)
else:
        print('The for loop is over')

#def
def sayHello():
        print('hello world!')

#func_param .. func_doc
def printMax(a, b):
        '''Print the test of max.

        if is integers.'''
        if a > b:
                print(a,'is maximum')
        else:
                print(b,'is maximum')
printMax(3, 4)
print(printMax.__doc__)

#default_param
def say(message='hi', times = 2):
        print(message * times)
say()

#using_sys
from sys import argv
from sys import path

print('The command line arguments are:')
for i in argv:
        print(i)
print('\n\nThe PYTHONPATH is', path, '\n')


#using module
from mymodule import sayhi, version

sayhi()
print('Version', version)







                
