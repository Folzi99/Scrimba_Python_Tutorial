# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Three Loop Questions:
# 1. What do I want to repeat?
#  -> guesses
# 2. What do I want to change each time?
#  -> guess number and number of guesses
# 3. How long should we repeat?
#  -> until user loses, runs out of guesses, or wins

num = 12
guess = 0
guess_limit = 3
guess_number = 0

while guess_number < guess_limit:
    guess = int(input("guess a number: "))
    if guess == num:
        print("correct")
        break
    else:
        print("try again")
    guess_number = guess_number + 1
if guess != num:
    print("nice try, the number is: ", num)

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

num = 53
guess = 0
guess_limit = 5
guess_number = 0

while guess_number < guess_limit:
    guess = int(input("guess a number: "))
    if guess == num:
        print("correct")
        break
    elif guess < num:
        print("too low!\ntry again")
    elif guess > num:
        print("too high!\ntry again")
    guess_number = guess_number + 1
if guess != num:
    print("nice try, the number is: ", num)
