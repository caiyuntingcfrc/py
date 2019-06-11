#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:34:01 2019

@author: leotsai0119
"""
# =============================================================================
# if, elif, else
# =============================================================================

x = 1
if x > 2:
    print("It is true.")
elif x == 1:
    print("x is 1")
else:
    print("It is not true.")

# strings    
name = "Sammy"
if name == "Frankie":
    print("Frankie")
elif name == "Sammy":
    print("Hi! " + name)
    
# =============================================================================
# for loop
# =============================================================================
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    print(num)
# the variable name can be anything
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in mylist:
    print(i)

for hello in mylist:
    print("Hello")
    print("This is a for loop")

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    # check for even
    if num % 2 == 0:
        # print(num)
        # print(f'Even number: {num}')
        print(f'{num} is even.')
    else:
        print(f'Odd Number: {num}')
        
# indentation
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    # with indentation
    print(list_sum)
    
for num in mylist:
    list_sum = list_sum + num
# without indentation (outside the for loop)
print(list_sum)

# strings
for letter in "Hello World":
    print(letter)

# use underscore (don't have to specify the variable)
for _ in "Hello World":
    print("A")

# tuple
tup = (1, 2, 3)
for item in tup:
    print(item)

# tuple unpacking
mylist = [(1, 2), (3, 4), (5, 6)]
for i in mylist:
    print(i)

for a, b in mylist:
    # you get 1, 3, 5
    print(a)
    # you get 2, 4, 6
    print(b)

# dictionary
d = {"k1":1, "k2":2, "k3":3}
for item in d:
    # you get k1, k2, k3
    print(item)
# print key and value in pair
for item in d.items():
    print(item)
# print keys and values with .itmes method
for key, value in d.items():
    print(key)
    print(value)
# print values with .value mathod
for value in d.values():
    print(value)

# =============================================================================
# while loop: do sth untill condition is not satisfied.
# =============================================================================
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    # x = x + 1
    x += 1
else:
    print("x is not less than 5")

# =============================================================================
# pass: do nothing at all.
# =============================================================================
x = [1, 2, 3]
for i in x:
    # some comment
    pass
print("End of my script")

# =============================================================================
# continue: goes to the top of the closest enclosing loop
# =============================================================================
my_string = "Sammy"
for letter in my_string:
    if letter == "a":
        continue
    # it goes to the top of the loop and print "m"
    print(letter)
# =============================================================================
# break: breaks out of the current closest enclosing loop
# =============================================================================
my_string = "Sammy"
for letter in my_string:
    if letter == "a":
        break
    # it will print only "S"
    print(letter)
# break in while loop
x = 0
while x < 50:
    if x == 30:
        break
    print(x)
    x += 2