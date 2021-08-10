#   list can contain; strings, floats, integers, booleans
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]

print(friends)
friends.sort()  #    sorts list in ascending order
print(friends)
friends.sort(reverse=True)   #   sorts in descending order
print(friends)
friends.reverse()   #   reverses order of original string
print(friends)

print(min(cars))
print(max(cars))
print(sum(cars))    #   can only be done with float + integer

print(min(friends)) #   provides lowest value (first letter)
print(max(friends)) #   does opposit

#   .append = adds things onto list

friends.append('TerryG')
print(friends)

#   .insert(#, variable) = places thing into specific locaiton on list
friends.insert(4,'JohnF')
print(friends)

#   variable[#] = replaces thing with new var/float/string
friends[2]='TerryG'
print(friends)

#  .extend = combine lists
friends.extend(cars)
print(friends)

#   remove = removes thing
friends.remove(Terry)
print(friends)

#   pop() = grab or remove (last variable by default) segmants form list
friends.pop()   #   try differnt numbers to experiment
print(friends)

#  .clear() = empties lists
friends.clear()
print(friends)

# del variable = delts list, be carful when using.
# del variable [#] = removes specifive var from list
del friends [2]
print(friends)

#   how to create new lists
new_friends = friends[:]
#   OR
new_friends = friends.copy()
# OR
new_friends = list(friends)

print(friends)
print(new_friends)
