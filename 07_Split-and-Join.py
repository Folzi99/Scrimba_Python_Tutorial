msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(list(msg)) # breaks message apart
print(msg.split()) # splits msg apart into list

msg ='Welcome     to     Python 101: Split     and Join'
print(msg.split(' ')) # will show spaces as empyt strings
# what class is this?

msg ='Welcome to Python 101: Split and Join'
print(msg.split(' '), type(msg.split(' ')))

# .split = converts to list

csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
#  results will be the same
print(csv.split(',')) #telling string to split on ','

# .join = converts to string
print(friends_list)
print('-'.join(friends_list)) # conversts list into string
print('-'.join(friends_list + friends_list)) # multiple lists can be turned into strings

# you can use .join + .split to create a list and convert back to string
print(''.join(msg.split())) # this exampls indicates the stripping of speces between strings

# .replace does the same thing as '.join + .split', its a more efficent alternative
print(msg.replace(' ', ''))
