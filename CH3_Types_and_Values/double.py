#!/usr/bin/env python3

from decimal import *

a = Decimal('.01')
b = Decimal('.03')
x = a + a + a - b
print(x)
print(type(x))