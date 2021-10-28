print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

# How do you add a number to each item to count the list?
for friend in friends:
    print(friend)

i = 0
for friend in friends:
    i += 1 #before print statment means 'i' outside loop wont be counted
    print(i, friend, sep=" ")

i = 0
for friend in friends:
    print(i, friend, sep=" ")
    i += 1 #after print statement means 'i' outside loop will be counted

print("---Enumerate----")
for num, friend in enumerate(friends,51): #adding number changeds where numbers start counting from
    print(num, friend)

for friend in enumerate(enumerate(friends,51),-100):
    print(friend)
for num, letter in enumerate('python',start = 5):
    print(num, letter)

print(type(enumerate(friends)))
print(list(enumerate(friends)))