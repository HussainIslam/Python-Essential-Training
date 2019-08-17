#!/env/bin/usr python3

def main():
    x = 5
    kitten(x)
    print(f'in main: x is {x}, with id {id(x)}\n')
    kittenChange(x)
    print(f'in main: x is {x}, with id {id(x)}\n')
    y = [5]
    kittenRef(y)
    print(f'in main: y is {y}, with id {id(y)}\n')


def kitten(a):
    print('Pass-by-value (no change)')
    print(f'in kitten: a is {a}, with id {id(a)}')

def kittenChange(a):
    a = 3
    print('Pass-by-value (value change)')
    print(f'in kittenChange: a is {a}, with id {id(a)}')

def kittenRef(a):
    print('Pass-by-Reference')
    print(f'in kittenRef: a is {a}, with id {id(a)}')


if __name__ == '__main__': main()