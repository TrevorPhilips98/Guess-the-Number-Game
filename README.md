Guess the Number Game
This is a simple console-based game where the player has to guess a random number between a specified range. 
The game provides feedback on whether the guess is too high or too low, and the player has a limited number of chances to guess the correct number. 
The game ends when the player correctly guesses the number or runs out of chances.

Requirements
This game requires Python 3.x and the Pygame library. You can install Pygame using pip:
pip install pygame

How to Play
To start the game, run the script guess_the_number.py in your terminal:
python guess_the_number.py

The game will display a welcome message and provide instructions on how to play. 
The player has to guess a number between a specified range by inputting their guess into the console. 
The game will provide feedback on whether the guess is too high or too low, and the player has a limited number of chances to guess the correct number. 
The player can also choose to quit the game at any time by entering "q" or "quit" into the console.

If the player correctly guesses the number, the game will congratulate them and display their score, 
which is based on the number of guesses it took them to guess the correct number. 
If their score is better than the previous high score, it will update the high score and save it to a file called high_score.txt.

Files
The program consists of the following files:

guess_the_number.py: The main script that runs the game.
game_start.mp3, try_again.mp3, level_passed.mp3, and kun.mp3: Sound effects played during the game.
high_score.txt: A text file that stores the previous high score.
Guess_the_Number_Game.pap: The flow diagramm of the programm, install PapDesign to open it
Flow diagramm.JPG: Screenshot of flow diagramm
