# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
def new_game(mode):
    global secret_number
    global count_guesses
    global max_guesses
    
    secret_number = random.randrange(0, mode)
    count_guesses = 0
    max_guesses = math.ceil(math.log(mode, 2))
    max_guesses = int(max_guesses)
    print
    print 'New game. Range is from 0 to ' + str(mode)
    print 'Number of remaining guesses is ', str(max_guesses)

# define event handlers for control panel
def range100():
    global mode
    
    mode = 100   
    new_game(mode)

def range1000():
    global mode   
  
    mode = 1000
    new_game(mode)


def input_guess(guess):
    global count_guesses
    global max_guesses
    global mode
    
    guess = int(guess)
    max_guesses -= 1
    print
    print 'Guess was', guess
    print 'Number of remaining guesses is', str(max_guesses)
    if guess == secret_number:
        print 'Correct!'
        print
        new_game(mode)
    elif guess > secret_number and max_guesses > 0:
        print 'Lower!'
    elif guess < secret_number and max_guesses > 0:
        print 'Higher!'
    elif max_guesses == 0:
        print 'You ran out of guesses. The number was', str(secret_number)
        print
        new_game(mode)
    else:
        print 'Unexpected condition in function: unput_guess'
    
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)
frame.add_button('Range is [0,100)', range100, 150)
frame.add_button('Range is [0,1000)', range1000, 150)
frame.add_input('Enter your guess:', input_guess, 50)

# register event handlers for control elements and start frame
frame.start()

# call new_game
mode = 100
new_game(mode)


# always remember to check your completed program against the grading rubric
