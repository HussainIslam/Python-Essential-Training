#!/usr/bin/env python3

import sys
import os
import random
import datetime

def main():
  v = sys.version_info
  print('Python version {}.{}.{}'.format(*v))
  print('Platform: {}'.format(sys.platform))
  print('Operating System: {}'.format(os.name))
  print(os.getenv('PATH'))
  print(os.getcwd())
  print(os.urandom(25).hex())

  print(random.randint(1, 1000))
  
  x = list(range(25))
  print(x)
  random.shuffle(x)
  print(x)

  now = datetime.datetime.now()
  print(f'Current Time: {now}')
  print(f'Current Year: {now.year}')
  print(f'Current Month: {now.month}')
  print(f'Current Day: {now.day}')
  print(f'Current Hour: {now.hour}')
  print(f'Current Minute: {now.minute}')
  print(f'Current Second: {now.second}')
  print(f'Current Microsecond: {now.microsecond}')
  

if __name__ == "__main__":
    main()