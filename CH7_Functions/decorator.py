#!/usr/bin/env python3

# This is the wrapper function, that wraps around the
# function 'f' any fuction can be wrapper around using
# this wrapper function.
def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2

# f3 is a function that was wrapped around by the 
# wrapper function 'f1'. So, now ONLY f3 can't be
# called. Whenever we call f3, the wrapper function
# is executed along with the f3.
@f1
def f3():
    print('this is f3')

@f1
def f4():
    print('this is f4')

f3()
f4()