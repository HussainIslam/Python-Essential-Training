#!/usr/bin/env python3

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff', 'lion': 'grrr',
                'giraffe': 'I am giraffe', 'dragon': 'rawr'}
    animalsAlt = dict(kitten='meow', puppy='ruff', lion='grrr',
                    giraffe='I am giraffe', dragon='rawr')

    # Printing key value pairs
    print('Print key-value pairs')
    for k, v in animals.items():
        print(f'{k}: {v}')
    print()

    # Printing only the values
    print('Print only values')
    for v in animals.values():
        print(v)
    print()

    # working with individual values
    print('Working with one value')
    animals['lion'] = 'I am a lion'
    print(animals['lion'])

    # additing new items
    print('Additing new items')
    animals['monkey'] = 'haha'
    for v in animals.values(): print(v)

    # GET method of Dictionary, this returns
    # None if key not found rather than
    # throwing an error
    print()
    print('Get method of Dictionary')
    print(animals.get('godzilla'))

if __name__ == "__main__":
    main()