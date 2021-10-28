print('Guessing game') 
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game. 
# Give user input box: 1. To capture guesses, 
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

#Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

# Three Loop Questions:
#1. What do I want to repeat?
#  -> guesses
#2. What do I want to change each time?
#  -> guess number and number of guesses
#3. How long should we repeat?
#  -> until user loses, runs out of guesses, or wins++

num = 12
guess = 0
g_limit = 3
g_number = 0

while g_number < g_limit:
    guess = int(input('Guess a number 1-20: '))

    if guess == num:
        print(f"you win! you guess it: {guess}")
    else:
        print(f'No, not {guess}')
        g_number += 1
if guess != num:
    print(f"you loose! it was {num}")