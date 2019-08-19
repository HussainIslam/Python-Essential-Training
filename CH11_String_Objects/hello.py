#!/usr/bin/env python3

class MyString(str):
  def __str__(self):
    return self[::-1]

print('String Format {}'.format(2 * 3))
s = MyString('Reverse String')
print(s)

print('Upper method'.upper())
print('Lower Method'.lower())
print('capitalize method'.capitalize())
print('title method'.title())
print('Swap Case'.swapcase())
print('CASE FOLD'.casefold())

s1 = 'Hello, World!'
s2 = 's1'.upper()
print(id(s1))
print(id(s2))

s3 = 'This is another string'
print(s1 + ' ' +s3)
