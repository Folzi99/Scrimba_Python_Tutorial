# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

name = input('Name: ')
km = input('Km: ')
miles = round((float(km) / 1.609), 2)   #   variable not need with FORTMATING alternative

print('Hello ', name.capitalize(),'! You have entered ', km, 'km which is equal to ', miles, ' Miles', sep='')

print(f'Hello {name.capitalize()}! You have entered {km}km which is equal to  {round((float(km) / 1.609), 2)} Miles')

#   output for both print is same, just
