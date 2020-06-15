import re
LoginDetails = {}
data = open('login users.txt')
subaru = data.readline()

for x in data:
    x = x.strip().split('|')
    LoginDetails[x[0]] = x[1]

def Login(username, password):
    for user in LoginDetails:
        if username == user and password == LoginDetails[user]:
            return True
    return False

print('Welcome to the guessing game!')
print('Please sign in!')
name = input('Username: ')
pwd = input('Password: ')

valid = False
counter = 0

while valid == False:
    valid = Login(name, pwd)
    if valid == True:
        print('Yay! You logged in!')
        print('Choose your difficulty')
    else:
        while counter < 4:
            counter += 1
            valid = False
            print("Oops! It seems you are incorrect")
            print("You have ", 5 - counter, "attempt(s) left." )
            name = input('Username: ')
            pwd = input('Password: ')

if counter == 4:
    signup = input('Uh oh, it seems you are wrong. Would you like to sign up? Y or N ')
    if signup.lower() == 'y':
            print("Ken's dad")
    elif signup.lower() == 'n':
        print('qwertyuiop')
    else:
        print('Stop. Just stop.')



















