#!/usr/bin/env python3

class Animal:
  def __init__(self, **kwargs):
    if 'type' in kwargs: self._type = kwargs['type']
    if 'name' in kwargs: self._name = kwargs['name']
    if 'sound' in kwargs: self._sound = kwargs['sound']
  
  def type(self, t = None):
    if t: self._type = t
    try: return self._type
    except AttributeError: return None
  
  def name(self, n = None):
    if n: self._name = n
    try: return self._name
    except AttributeError: return None

  def sound(self, s = None):
    if s: self._sound = s
    try: return self._sound
    except AttributeError: return None

  def __str__(self):
    return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}"'

# kitten class in inheriting from the Animal class
# that is why the Animal class is passed as paramter
# in the class declaration of the kitten class
# Inside the class declaration, we are defining the 
# constructor (__init__) method first. Here in the constructor
# first we are assigning the value of type to 'kitten
# then we are checking whether, the type is passed 
# in the kwargs; if it is passed, we delete what is passed
# and the call the constructor of the base class using the
# keyword 'super' followed by the constructor name __init__
class Kitten(Animal):
  def __init__(self, **kwargs):
    self._type = 'kitten'
    if 'type' in kwargs: del kwargs['type']
    super().__init__(**kwargs)

class Duck(Animal):
  def __init__(self, **kwargs):
    self._type = 'duck'
    if 'type' in kwargs: del kwargs['type']
    super().__init__(**kwargs)

def main():
  a0 = Kitten(name= 'fluffy', sound= 'rawr')
  a1 = Duck(name= 'donald', sound='quack')
  print(a0)
  print(a1)

if __name__ == '__main__': main()