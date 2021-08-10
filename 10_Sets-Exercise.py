friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']

#1. Check if ‘Eric’ and ‘John’ exist in friends
print('Eric' in friends and 'John' in friends)

#2. combine or add the two sets
print(friends.union(my_friends))
### print(friends | my_friends) # same result as ^

#3. Find names that are in both sets
print(friends.intersection(my_friends))
### print(friends & my_friends)  # same result as ^

#4. find names that are only in friends
print(friends.difference(my_friends))
### print(friends - my_friends) # same result as ^

#5. Show only the names who only appear in one of the lists
print(my_friends.symmetric_difference(friends))
### print(my_friends ^ friends) # same result as ^

#6. Create a new cars-list without duplicates
cars_no_dup = set(cars)
# cars_no_dup = list(set(cars))
# ^ converts back into list
print(cars_no_dup)
