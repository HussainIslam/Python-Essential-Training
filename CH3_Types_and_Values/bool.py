#!/usr/bin/env python3

big = 9
small = 5

#Straight assignment
x = True
print(f'x has a value: {x} with type: {type(x)}')

#Logical test
x = 9 < 5
print(f'x has a value: {x} with type: {type(x)}')

#zero as false
x = 0
if x:
  print('true')
else:
  print('false`')