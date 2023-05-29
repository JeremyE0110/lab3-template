#!/usr/bin/env python3

'''
#Part1 Function: No argument no return value
def hello():
    print('Hello World')
    print('Inside a Funtion')
    return

my_stuff = hello()
print('Stuff return from hello(): ',my_stuff)
print('the object my_stuff is of type:',type(my_stuff))
'''
#############
'''
#Part2 Function: No argument but returns a string
def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

text = return_text_value()
print(text)
'''
###########
"""
#Part3 Function: no argument but returns a number
def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3
'''
number = return_number_value()
print(number)
print(number + 5)
print(return_number_value() + 10)
'''
number = return_number_value()
print('my number is', number)
print('my number is ' + str(number))
print('my number is ' + str(return_number_value()))
"""
