#Sets - blazingly fast unordered Lists
### Sets CANNOT contain dupplicates
## use curly brackets
## much fast at finding members than lists
## results will be unordered in some python interpeters
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends)
print(friends_tuple)
print(friends_set)

my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
print(friends_set.intersection(my_friends_set)) # finds members that match both sets
print(friends_set.difference(my_friends_set)) # finds members that are not in both sets
print(friends_set.union(my_friends_set)) # command shows all memembers with NO duplicates

#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()
