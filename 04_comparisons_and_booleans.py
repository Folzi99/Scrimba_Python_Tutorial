a=7
b=3
print('a == b is', a == b)
print('a != b is', a != b)
print('a > b is', a > b)
print('a < b is', a < b)
print('a >= b is', a >= b)
print('a <= b is', a <= b)
print('o in John is ','o' in 'John') #membership
print('o in John is ','o' not in 'John') #non membership
print('John is John ','John' is 'John') #identity
print('John is not John is ','John' is not 'John') # negative identity

# referes to occupying memory space in computer
a = [3,7,42]
b = a
print(a == b)
print(a is b)
print(id(a), id(b)) # results will be the same

a = [3,7,42]
b = [3,7,42]
print(a == b)
print(a is b)
print(id(a), id(b)) # results will different becuase they occupy different space

# Boolean Properties:
print(int(True)) # evaluates to 1
print(int(False)) # evaluates to 0

# Converting strings to booleans:
print(bool('Parrot')) # evaluates to True
print(bool(' ')) # evaluates to True
print(bool('')) # evaluates to False

# Converting numbers to booleans:
print(bool(1)) # evaluates to True
print(bool(43)) # evaluates to True
print(bool(0)) # evaluates to False

# This means that empty/trival objects will equal 0
