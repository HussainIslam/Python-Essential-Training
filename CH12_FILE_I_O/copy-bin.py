#!/usr/bin/env python3

def main():
  infile = open('excellent_solutions.jpg', 'rb')
  outfile = open('exs.jpg', 'wb')
  while True:
    buf = infile.read(10)
    if buf:
      outfile.write(buf)
      print('.', end='', flush=True)
    else: break
  outfile.close()
  print('\nDone Copying')

if __name__=='__main__': main()
