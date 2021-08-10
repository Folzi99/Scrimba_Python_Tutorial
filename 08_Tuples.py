#Tuples - faster Lists you can't change
## less complex
## faster to work with, iterations/searches are faster
## can use some functions as list but has limitations
## if you have data you dont want to change; can be more better suited than lists
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham') # parentheses makes it tuple

# results will be the same
print(friends)
print(friends_tuple)
print(friends[2:4])
print(friends_tuple[2:4])
