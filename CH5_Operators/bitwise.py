#!/usr/bin/env python3

x = 0x0a
y = 0x02
z = x & y
print("Bitwise AND (&) operator")
print("------------------------")
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print(f'(Dec) x is {x:02}, y is {y:02}, z is {z:02}\n')


x = 0x0a
y = 0x02
z = x | y
print("Bitwise OR (|) operator")
print("------------------------")
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print(f'(Dec) x is {x:02}, y is {y:02}, z is {z:02}\n')

x = 0x0a
y = 0x02
z = x ^ y
print("Bitwise XOR (|) operator")
print("------------------------")
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print(f'(Dec) x is {x:02}, y is {y:02}, z is {z:02}\n')

x = 0x0a
y = 0x02
z = x << y
print("Bitwise Shift Left (<<) operator")
print("------------------------")
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print(f'(Dec) x is {x:02}, y is {y:02}, z is {z:02}\n')

x = 0x0a
y = 0x02
z = x >> y
print("Bitwise Shift Right (>>) operator")
print("------------------------")
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print(f'(Dec) x is {x:02}, y is {y:02}, z is {z:02}\n')