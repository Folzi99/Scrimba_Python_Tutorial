csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

# MY WAY - [The long way lol]
csv_1 = csv.split(',')
csv_2 = ' '.join(csv_1)
csv_3 = csv_2.split(':')
csv_4 = ' '.join(csv_3)
csv_5 = csv_4.split(';')
csv_6 = ' '.join(csv_5)
friends_list = csv_6.split(' ')
print(friends_list)

# Scimba Solution!!!! Seems to obvious haha
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

# using .joing and .split
## print(','.join(csv.split(';'))) # <class 'str'>
## print(','.join(csv.split(';')).split(':')) # <class 'list'>
## print(','.join(','.join(csv.split(';')).split(':'))) # <class 'str'>
## print(','.join(','.join(csv.split(';')).split(':')).split(',')) # <class 'list'>
friends_list = (','.join(','.join(csv.split(';')).split(':')).split(','))
print(friends_list)

# other way using replace
print('replace', csv.replace(';',',').replace(':',',').split(','))
