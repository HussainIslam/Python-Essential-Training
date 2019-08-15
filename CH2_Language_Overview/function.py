#!/usr/bin/env python3

def function(n = 1):
  print(n)

function(20)
function()

x = function(42)
print('Return from function is: {}'.format(x))