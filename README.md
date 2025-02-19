# Tic Tac Toe Game in Python

This is a simple implementation of the **Tic Tac Toe** game developed using the Python programming language. It allows two players to take turns and play a game of Tic Tac Toe in the terminal/command line.

## Features

- Two-player gameplay.
- Board displayed after every move.
- Input validation to ensure valid moves.
- Check for winner or draw after each move.

## Requirements

- Python 3.x

## Installation

To run the Tic Tac Toe game, you need to have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

## Steps:
1. Clone this repository or download the source code to your local machine.
   ```bash
   git clone https://github.com/Saivivek04/manage.git
2. Navigate to the project directory:

   cd manage.py
3. Run the game:

   python manage.py

## Game Instructions

The game is played on a 3x3 grid. Players will take turns to mark their symbol ('X' or 'O') on the grid.
Player 1 is assigned the 'X' symbol, and Player 2 is assigned the 'O' symbol.
The first player to align three of their symbols in a row, column, or diagonal wins the game.
If all spots are filled and no player has won, the game results in a draw.

## How It Works

The board is represented as a list of strings, and the players input the number (1-9) corresponding to the grid positions to place their symbol.
After each move, the board is updated and displayed.
The game checks after every move whether a player has won or if there is a draw.

## Example of the Game Board:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9


Players input a number (1-9) to place their mark in the corresponding position.

## Example Gameplay

Player 1: X


Player 2: O

Initial Board:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9


Player X, enter a number (1-9) to place your mark: 1

X | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9


Player O, enter a number (1-9) to place your mark: 5 

X | 2 | 3
---------
4 | O | 6
---------
7 | 8 | 9


...

## Code Explanation
- display_board(): This function prints the current state of the game board to the console after each move.
- player_move(player): This function allows the current player to make a move by selecting a number between 1-9 that corresponds to a spot on the board.
- check_winner(player): This function checks if the current player has won the game.
- play_game(): This is the main function that drives the entire game.

## Contact Information
- **Email**: saiuppala2003@gmail.com
- **LinkedIn**: [Sai Vivek](https://www.linkedin.com/in/saivivek04/)
- **GitHub**: [Sai Vivek](https://github.com/Saivivek04)

## Acknowledgments
Special thanks to the open-source libraries and tools used in this project to enhance its functionality and design.
