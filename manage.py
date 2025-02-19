# Initialize the Tic Tac Toe board
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Function to display the board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to get user input and place their symbol on the board
def player_move(player):
    while True:
        move = input(f"Player {player}, enter a number (1-9) to place your mark: ")
        if move in board:
            board[int(move) - 1] = player
            break
        else:
            print("Invalid move! Try again.")

# Function to check for a win
def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical wins
        [0, 4, 8], [2, 4, 6]              # Diagonal wins
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Main function to run the game
def play_game():
    display_board()
    current_player = "X"
    
    for _ in range(9):
        player_move(current_player)
        display_board()
        
        if check_winner(current_player):
            print(f"Congratulations! Player {current_player} wins!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("It’s a tie!")
# Start the game
play_game()