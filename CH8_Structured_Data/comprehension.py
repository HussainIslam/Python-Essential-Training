#!/usr/bin/env python3

def main():
  seq = range(11)
  
  # list from sequence
  seq2 = [ x for x in seq if x % 3 != 0 ]

  #creating tuple
  seq3 = [ (x, x**2) for x in seq]

  # create another list
  from math import pi
  seq4 = [round(pi, i) for i in seq]

  # create a dictionary
  seq5 = { x: x**2 for x in seq }

  # create a set
  seq6 = { x for x in 'superduper' if x not in 'pd'}

  print_list(seq)
  print_list(seq2)
  print_list(seq3)
  print_list(seq4)
  print(seq5)
  print_list(seq6)

def print_list(o):
  for x in o: print(x, end=' ')
  print()

if __name__ == "__main__":
    main()