#   Will print multiple lines
msg="""Dear Terry,,
You must cut down the mightiest
tree in the forest with…
a herring! <3"""
print(msg)

#   REPLACE
msg='Welcome to Python 101: Strings'
print(msg.replace('Python','Java'))
#   Strings are imutable, canonot be change once rate, need to creat new variable
#   will have same result but varible has changed
msg=msg.replace('Python','C')
print(msg)

#  Membership
msg='Welcome to Python 101: Strings'
#   Will print True
print('Python' in msg)

#   Will print False
print('Python' not  in msg)

#   CONCATENATION = adding strings together
#   Use '+' to add variables together, concatetion can get messy with long strings

name = 'TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
print(msg)
#   more efficient way = same result
#   String FORTMATING add 'f' at start
msg1 = f'[{name}] loves the color {color.lower()}!'
print(msg1)
# How to capitalize name?
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg1)
