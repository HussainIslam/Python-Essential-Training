#!/usr/bin/env python

#Lists
x = [ 1, 2, 3, 4, 5]
print('Lists')
print('-----')

for i in x:
  print('i is {}'.format(i))

#Tuples
x = ( 1, 2, 3, 4, 5 )
print('Tuples')
print('------')
for i in x:
  print('i is {}'.format(i))

#Range, Overload with single parameter
x = range(5)
print('Range Overload 1')
print('----------------')
for i in x:
  print('i is {}'.format(i))

#Range, Overload with two parameters
x = range(5, 10)
print('Range, Overload 2')
print('-----------------')
for i in x:
  print('i is {}'.format(i))

#Range, Overload with three parameters
x = range(5)
print('Range, Overload 3')
print('-----------------')
for i in x:
  print('i is {}'.format(i))

#Dictionary
x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
print('Dictionary')
print('----------')
for k, v in x.items():
  print('k: {}, v: {}'.format(k, v))

print()
print('Value changed')

x['three'] = 42
for k, v in x.items():
  print('k: {}, v: {}'.format(k, v))