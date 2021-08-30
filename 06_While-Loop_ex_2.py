# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)

num = 53
guess_limit = 5
guess_number = 0

while guess_number < guess_limit:
    guess = int(input("guess a number [1-100]: "))
    if guess != num:
        guess_number = guess_number + 1
        if guess > num:
            print("too high! ")
        else:
            print("too low! ")
    if guess == num:
        print("correct!")
        break
if guess != num:
    print("nice try, the number is: ", num)