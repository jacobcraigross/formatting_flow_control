__author__ = 'dev'

# flow control, voting age verifier
name = input ('please enter your name: ')
age = int(input('hello {0} please enter your age: '.format(name)))

if age >= 18:
    print('you are old enough to vote')
    print('vote X for candidate Y. this is not a choice')
else:
    print('please come back and cast the party vote in {0} years'.format(18 - age))
    print('when you are old enough, vote X for candidate Y. this is not a choice')

# more flow control, number guessing game
print ('please guess a number between 1 and 10... enter it here: ')
guess = int(input())

if guess != 4:
    if guess < 4:
        print('guess higher dumbass')
    else:
        print('guess lower shit for brains')

    guess = int(input())
    if guess == 4:
        print('great job loser, even a broken clock is right twice a day')
    else:
        print('go lay down')

else:
    print('wow... you guessed the number but you are still one ugly motherfucker')

