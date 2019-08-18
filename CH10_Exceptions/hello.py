#!/usr/bin/env python3

import sys

def main():
  try:
    x = 5/0
  except ValueError:
    print('I caught a ValueError')
  except:
    print(f'Unknown error: {sys.exc_info()}')
  else:
    print('good job')

if __name__=='__main__': main()
