#!/usr/bin/env python3

def main():
  infile = open('lines.txt','rt')
  outfile = open('lines_copy.txt', 'wt')
  for line in infile:
    print(line.rstrip(), file=outfile)
    # outfile.writelines(line)
    print('.', end='', flush=True)
  outfile.close()
  print('\nDone Copying')

if __name__ == '__main__': main()