# Dictionaries CANNOT contain duplicate keys BUT there can be multiple values
python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}

# Membership Test
# Result will be False
print('arthur' in holy_grail)

# Keys are case sensitive
# Result will be True
print('Arthur' in holy_grail)

if 'Arthur' not in python:
    print('He\'s not here!')
   
# Dictionaries are inherently not sorted
# Concatenating multiple dictionaries
people = {}
people1 = {}
people2 = {}
# Method 1 update
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(people)
print(sorted(people.items()))

# Method 2 comprehension
for groups in (python, holy_grail, life_of_brian) : people1.update(groups)
print(people1)
print(sorted(people1.items()))

# Method 3 unpacking (Python 3.5 >)
people2 = {**python, **holy_grail, **life_of_brian}
print(people2)
print(sorted(people2.items()))

# Finding the sum of all values
# If values are strings it will result in Error
print('The sum of the ages: ', sum(people.values()))