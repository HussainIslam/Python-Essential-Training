#!/usr/bin/env python3

# Multiline String

multi = """This is the first line
This is the second line
This is the third line
"""
print(multi)

# String methods
################

#upper case method
x = 'This line is uppercase'.upper()
print(x)

#capitalize case method
x = 'this line is capitalized'.capitalize()
print(x)

#lower case method
x = 'THIS MAKES LOWERCASE'.lower()
print(x)

#string format method
x = 'seven "{1:< 9}" "{0:> 9}"'.format(8,9)
print(x)

