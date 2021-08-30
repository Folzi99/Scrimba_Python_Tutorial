def greeting(name, age=28, color="red"):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print('Hello '  +  name.capitalize() + ', you will be ' + str(age + 1) +' next birthday!')
    print(f'Hello {name.capitalize()}, you will be {int(age) + 1} years old next birthday!')
    print(f'We hear you like the color {color.lower()}! {color.lower()} is a string with color')

name = input('Enter your name: ')
age = input('Enter your age: ')
color = input('Favourite color: ')
greeting(name, int(age), color)
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color - DONE
# 2. extend the function with another  input parameter 'color', that defaults to 'red' - DONE
# 3. Capture the color via an input box as variable:color - DONE
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
#  adding 1 to the age - DONE
# 5. Capitalize first letter of the 'name', and rest are small caps - DONE
# 6. Favorite color should be in lowercase
