#!/usr/bin/env python3

y = ( 1, 'two', 3.0, 4, 5 )
print(id(y))

if isinstance(y, tuple):
  print('Tuple')
else:
  print('Not tuple')