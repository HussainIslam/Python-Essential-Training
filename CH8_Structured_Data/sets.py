#!/usr/bin/env python

def main():
  a = set("We're gonna need a bigger boat.")
  b = set("I'm sorry, Dave. I'm afraid I can't do that.")
  
  # prints unordered set
  print_set(a)

  # prints sorted set
  print_set(sorted(a))

  # prints items that are part of a but b
  print_set(a - b)

  # prints items that are part of a or b
  print_set( a | b )

  # prints items that part of a or b but not both
  print_set( a ^ b )

  # prints items common to both a and b
  print_set( a & b )


def print_set(o):
  print('{', end='')
  for x in o:
    print(x, end='')
  print('}')

if __name__ == "__main__":
    main()