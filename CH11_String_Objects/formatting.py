#!/usr/bin/env python3

x = 42
y = 73
print('The number is {xx} {bb}'.format(xx=x, bb=y))
print('The number is {1} {0} {1}'.format(x, y))
print('The number is "{0:<+05}" "{1:+05}"'.format(x, y))
print('The number is {:,}'.format(x * y))
print('the number is (EU style) {:,}'.format(x * y).replace(',', '.'))
print('the number is {:f}'.format(x))
print('the number is {:.3f}'.format(x))
print('the number is (octal) {:o}'.format(x))
print('the number is (binary) {:b}'.format(x))
print('the number is (hexadecimal) {:x}'.format(x))
print(f'the number is {x}')
