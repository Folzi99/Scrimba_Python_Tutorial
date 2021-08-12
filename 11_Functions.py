# bundles together code you often use
# allows you to split-up code so it is easier to read
# use names you understand
# always declare functions before you use them
# everything under def function needs to be indented to be included
# peramators are a variable used inside function
# you need to specify an 'arrgument'
# sometimes you need to set a default falue for variable
def greeting(name, age="28"):
    print("Hello " + name + " you are " + age + "!")
    # formate print with stings; shorter and snapper, easier to read
    print(f"Hello {name} you are {age}!")

name = input("Enter you name: ")
greeting(name, "32")

#to use funtion you need to 'call' it
greeting("Brian", "32")
greeting("Judith")

# how to convert number to string?
def greeting(name, age= 28):
    print("Hello " + name + " you are " + str(age) + "!")
    # formate print with stings; shorter and snapper, easier to read
    print(f"Hello {name} you are {age}!")

name = input("Enter you name: ")
greeting(name, 33)
