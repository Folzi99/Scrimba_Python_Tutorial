# How to make this awesome?
print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")


#while condition:
#    code
#    iterator
# Three Loop Questions:
#1. What do I want to repeat?
#  -> message
#2. What do I want to change each time?
#  -> stars
#3. How long should we repeat?
#  -> 5 times

i = 0

while i < 5:
    i = i + 1 # short hand is i += 1N
    print(f"{i}."+"*"*i + "Loops are awesome"+"*"*i)
#    i = i + 1 >>> This method will start the iteraations after the first print statment, 'i' in print statment will be '0'
