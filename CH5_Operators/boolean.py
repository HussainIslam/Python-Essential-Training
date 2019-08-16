#!/usr/bin/env python3

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

# And Operator
print(f'AND operator')
if a and b:
  print('Expression is true')
else:
  print('Expression is false')

# OR Operator
print(f'OR Operator')
if a or b:
  print('Expression is true')
else:
  print('Expression is false')

# NOT Operator
print(f'NOT operator')
if not a:
  print('Expression is true')
else:
  print('Expression is false')

# IN Operator
print(f'IN Operator')
if y in x:
  print('Expression is true')
else:
  print('Expression is false')

# IS Operator
print('IS Operator')
if y is x[0]:
  print(f'expression is true')
else:
  print('Expression is false')