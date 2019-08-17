#!/usr/bin/env python3

def main():
    print('Call with Three args:')
    kitten('meow', 'grrr', 'purrr')
    print()

    x = ( '1', '2', '3')
    print('Call with Tuple as args')
    kitten(*x)
    print()
    
    print('Call with no args: ')
    kitten()

# It's a best practice to call the variable length
# parameter as 'args'
def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else:
        print('Empty args')

if __name__ == "__main__":
    main()