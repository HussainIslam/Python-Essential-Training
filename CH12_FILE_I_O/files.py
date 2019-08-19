#!/usr/bin/env python3

def main():
  # Open the file and returns a file object
  f = open('lines.txt')
  for line in f:
    # The rstrip
    print(line.rstrip())

if __name__ == '__main__': main()