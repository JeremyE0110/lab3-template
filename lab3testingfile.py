#!/usr/bin/env python3

#Investigation2 Part1
"""
def square(number):
    return number ** 2
'''
print(square(5))
print(square(10))
print(square(12))
print(square(square(2)))
#print(square('2'))
'''
def sum_numbers(number1, number2):
    return int(number1) + int(number2)

print(sum_numbers(5, 10))
print(sum_numbers(50, 100))
print(square(sum_numbers(5, 10)))
"""

#Multiple Argument using Conditional statements
'''
def describe_temperature(temp):
    if temp > 30:
        return 'hot'
    elif temp < 0:
        return 'cold'
    elif temp == 20:
        return 'perfect'
    return 'ok'

print(describe_temperature(50))
print(describe_temperature(20))
print(describe_temperature(-50))
print(describe_temperature(25))
print(describe_temperature(10))
'''

#Investigation2 Part 2
'''
import os

ls_return = os.system('ls')
print('The contents of ls_return:', ls_return)

whoami_return = os.system('whoami')
print('The contents of whoami_return:', whoami_return)

ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:', ifconfig_return)

ipconfig_return = os.system('ipconfig')
print('The contents of ipconfig_return:', ipconfig_return)
'''

#popen()
'''
import os
ls_return = os.popen('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.popen('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.popen('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)

import os
whoami_return=os.popen('whoami')
whoami_contents = whoami_return.read()
print('whoami_contents:',whoami_contents)

#try
ifconfig_return = os.popen('ifconfig')
ifconfig_contents = ifconfig_return.read()
print('ifconfig_contents:')
print(ifconfig_contents)

ipconfig_return = os.popen('ipconfig')
ipconfig_contents = ipconfig_return.read()
print('The contents of ipconfig_return:',ipconfig_contents)
'''

#subprocess popen()
'''
import subprocess

p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

output = p.communicate()
print(output)
print(output[0])
stdout = output[0].decode('utf-8').strip()
print(stdout)
'''

#Investigation3: Part1
'''
list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
list2 = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]
list3 = [ 'uli101', 1, 'ops235', 2, 'ops335', 3, 'ops445', 4, 'ops535', 5, 'ops635', 6 ]

print(list1[0])
print(list2[1])
print(list3[-1])

print(list1[0:5])
print(list2[2:4])
print(list3[3:])
'''

#Part2 Manipulating Items
'''
courses = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]
print(courses[0])
courses[0] = 'eac150'
print(courses[0])
print(courses)

courses.append('ops235')
print(courses)

courses.insert(0, 'hwd101') 
print(courses)

courses.remove('ops335')
print(courses)

sorted_courses = courses.copy() 
sorted_courses.sort()           
print(courses)
print(sorted_courses)



list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
length_of_list = len(list_of_numbers)
smallest_in_list = min(list_of_numbers)
largest_in_list = max(list_of_numbers)

print("List length is " + str(length_of_list) + 
      ", smallest element in the list is " + str(smallest_in_list) +
      ", largest element in the list is " + str(largest_in_list))
'''

#Part3 Iterating over lists
'''
list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
for item in list_of_numbers:
    print(item)

#try1

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]

def square(num):
    return num * num

for value in list_of_numbers:
    print(square(value))

#try2
list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]

def square_list(number_list):
    new_list = []
    for number in number_list:
        new_list.append(number * number)
    return new_list

new_list_of_numbers = square_list(list_of_numbers)
print(list_of_numbers)
print(new_list_of_numbers)

#try3
list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
def delete_numbers(numbers):
    numbers.remove(5)
    numbers.remove(6)
    numbers.remove(8)
    numbers.remove(5)
delete_numbers(list_of_numbers)
print(list_of_numbers)
'''