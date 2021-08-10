# print  "1 Welcome Ring To Tyler"
# ever 1st letter == capitalised
# reverse the printed line
msg = "welcome to Python 101: Strings"
msg1 = "welcome to Python 101: Strings" [:: -1]
print(msg[18], msg.capitalize()[:7], msg.upper()[25] + msg[26:29], msg.title()[8:10], "Tyler")
print(msg1)

# Scimbe answers
msg1 = msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title())
print(msg1[::-1].title())
