# You're having a party and want to invite your friends.
# You want the print out invitations for each friend using for loops
# The names are in two lists, 'names' and 'names1'
# You also need to add two extra names to the list using and 'input' box, when you run the code
# Printout on invitation to each friend per line
# Names should be properly capitalized
# Example of printout
#   John Cleese! You are invited to the party on saturday.
#   Eric Idle! You are invited to the party on saturday.
#   names = ['john ClEEse','Eric IDLE','michael']
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
msg = "! You are invited to the aprty on saturday."
names.extend(names1)
# names += names1 >same result as^
for index in range(2):
    names.append(input("enter a name: "))
for name in names:
    msg1 = f'{name.title()} {msg}'
    print(msg1)
