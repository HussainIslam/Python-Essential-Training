#!/usr/bin/env python3

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(game[1: 5: 2])

    i = game.index('Paper')
    print(game[i])
    print_list(game)
    print()

    # add item at the end of the list
    game.append('Computer')

    # insert item at a particular index of list
    game.insert(0, 'Mouse')

    # remove an item from any index of the list
    game.remove('Paper')

    # remove an item from the end of the list
    # it also returns the item removed
    item = game.pop() 
    print(item)

    # remove an item from a particular index of list
    item2 = game.pop(3)
    print(item2)

    # delete statement to remove an item
    # we can also use the slicer format [start: end: step]
    # to remove items using the delete command
    del game[0]

    # join list
    print('- '.join(game))
    print_list(game)

def print_list(o):
    for i in o:
        print(i, end=' ', flush = True)
    print()

if __name__ == "__main__": main()