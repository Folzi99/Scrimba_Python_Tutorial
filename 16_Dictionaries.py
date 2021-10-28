movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
print(movie)
print(movie['title'])
# 'budget' doesn't exist in dictionary
# print(movie['budget'])
print(movie.get('budget'))

# 'not found' becomes default value
print(movie.get('budget', 'not found'))

# how to update dictionary
movie['title'] = 'The Holy Grail'

print(movie.get('title'))

# you can use same process to add new entry to dictionary
movie['budget'] = 250000
print(movie.get('budget'))
print(movie)

movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
print(movie)

# how to delete an entry
# del movie['year']
print(movie)

# how to remove an entry and save as a new variable
year = movie.pop('year')
print(year)

# finding legth of entries
print(len(movie))
# find the keys
print(movie.keys())
# find the values
print(movie.values())
# fine the items, results will be tupels
print(movie.items())

# if you want to loop through all items in the list
for key, value in movie.items():
    print(key, value)