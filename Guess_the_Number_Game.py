# Import randint function from the random library to generate a random number
from random import randint

# Import the os module to hide Pygame's welcome message
import os

# Set an environment variable to hide Pygame's welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
# Import pygame to play sound effects
import pygame

# Set the range of numbers to guess from
min_num = 0    # The minimum of the random number
max_num = 100    # The maximum of the random number

# Initialize Pygame
pygame.init()

# get the sound effects files
game_start_sound = pygame.mixer.Sound('game_start.mp3')
try_again_sound = pygame.mixer.Sound('try_again.mp3')
level_passed_sound = pygame.mixer.Sound('level_passed.mp3')
kun_sound = pygame.mixer.Sound('kun.mp3')

# Set the path for the file to store the high score
high_score_file = 'high_score.txt'
# Check if the file exists
if os.path.exists(high_score_file):
    # If the file exists, read the high score from the file
    with open(high_score_file, "r") as f:
        high_score = int(f.read())
else:
    # If the file does not exist, set the high score to 0
    high_score = 0

# Print the welcome message and the range of numbers the user can guess from
equals = '='
plus = '+'
print(f'\n{equals*20} Welcome to Guess the Number Game {equals*20}')
print(f'{equals*15} You can guess the number between {min_num} and {max_num} {equals*15}')

limit_of_guesses = 10   # Initialize the limit of guesses to 10
num_of_guesses = 0    # Initialize the number of guesses to 0
activ = True    # Initialize the activ variable to True, which controls the loop
set_random = True   # If it is True, generate random number in the while loop

while activ:
    # Start the game loop
    if set_random:
        # Print the current high score and how many chances have user
        print(f"\n{plus*26} Current high score:{high_score} {plus*26}")
        print(f'{plus*22} You have {limit_of_guesses} chances to guess {plus*22}')
        #play game start sound effect
        game_start_sound.play()
        # Generate a random number between min_num and max_num, inclusive
        random_num = randint(min_num, max_num+1)
        set_random = False
    # Ask the user to input a number or quit the game
    user_input = input(f'\nGuess the Number(enter "q" or "quit" to quit): ')
    if user_input.lower() in ('q', 'quit'):
        # If the user enters 'q' or 'quit', end the game
        print('\nGame over. Thanks for playing! ')
        break
    try:
        user_guess = int(user_input)    # Convert the user's input to an integer
        num_of_guesses += 1             # Increment the number of guesses
        limit_of_guesses -= 1           # chances - 1
        if user_guess < random_num:
            # Provides feedback on their guess was too low
            print('Your guess is too low, please try again. ')
            print(f'Number of guesses: {num_of_guesses}')
            try_again_sound.play()
            if limit_of_guesses == 0:
                print('You have used up your chances.')
                play_again = input('\nDo you want to play again?(y for yes)')
                if play_again.lower() in ('y', 'yes'):
                    set_random = True
                    limit_of_guesses = 10
                    num_of_guesses = 0
                else:
                    activ = False   # Set activ to False to end the loop
        elif user_guess > random_num:
            # Provides feedback on their guess was too high
            print('Your guess is too high, please try again. ')
            print(f'Number of guesses: {num_of_guesses}')
            try_again_sound.play()
            if limit_of_guesses == 0:
                print('You have used up your chances.')
                play_again = input('\nDo you want to play again?(y for yes)')
                if play_again.lower() in ('y', 'yes'):
                    set_random = True
                    limit_of_guesses = 10
                    num_of_guesses = 0
                else:
                    activ = False   # Set activ to False to end the loop
        else:
            # If the guess is correct, congratulate the user and end the game
            print('Congratulations!')
            print(f'You guessed the number in {num_of_guesses} tries.')
            ''' Check if the new score(11-nubmer of guesses) 
                is bigger than the high score'''
            if 11-num_of_guesses > high_score or high_score == 0:
                ''' If the number of guesses is less than the high score 
                    or there is no high score, 
                    update the high score and save it to the file.'''
                high_score = 11-num_of_guesses
                with open(high_score_file, "w") as f:
                    f.write(str(high_score))
                print(f"\nNew high score: {high_score}")
            else:
                print(f'Your score in this round: {11-num_of_guesses}')
            level_passed_sound.play()
            pygame.time.wait(2000)
            kun_sound.play()
            pygame.time.wait(8000)
            play_again = input('\nDo you want to play again?(y for yes)')
            if play_again.lower() in ('y', 'yes'):
                set_random = True
                limit_of_guesses = 10
                num_of_guesses = 0
            else:
                activ = False   # Set activ to False to end the loop
    except ValueError:
        # If the user inputs something that can't be converted to an integer, 
        # prompt them to input again
        print('Please enter an integer.')
        # Continue the loop without incrementing the number of guesses
        continue