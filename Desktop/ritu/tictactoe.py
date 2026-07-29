# Tic-Tac-Toe Game

board = [" " for _ in range(9)]

def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals5
        ]
   

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def board_full():
    return " " not in board

current_player = "X"

while True:
    display_board()

    try:
        choice = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

        if choice < 0 or choice > 8:
            print("Invalid position! Choose between 1 and 9.")
            continue

        if board[choice] != " ":
            print("Position already taken! Try again.")
            continue

        board[choice] = current_player

        if check_winner(current_player):
            display_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if board_full():
            display_board()
            print("🤝 It's a Draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    except ValueError:
        print("Please enter a valid number!")