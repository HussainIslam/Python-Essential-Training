#!/usr/bin/env python3

def isPrime(n):
  if n <= 1:
    return False
  for x in range(2, n):
    if n % x == 0:
      return False
  else:
    return True


def listPrime():
  for n in range(100):
    if isPrime(n):
      print(n, end=' ', flush = True)
  print()

n = 20

if isPrime(n):
  print(f'{n} is a Prime number')
else:
  print(f'{n} is not a prime number')

listPrime()