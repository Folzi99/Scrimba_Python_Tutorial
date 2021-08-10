friends = ['John', 'Michael', 'Sarah', 'Eric', 'Graham', 'Eric']

#   will print select names form list in order
print(friends[1], friends[4])
print(friends[1])

#   negative indices will print from last to first
print(friends[-1], friends[-4])

#   slicing syntax using ':'
print(friends[2:4]) #   will not print numbers stated
print(friends[:])    #   will print whole list

#   count number of elements in list
print(len(friends))

#   identify position of item in list
print(friends.index('Eric'))

#   count occurnece in list
print(friends.count('Eric'))
