# Tic Tac Toe Game

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

current_player = "X"


def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    win_conditions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for condition in win_conditions:
        if (
            board[condition[0]] == player and
            board[condition[1]] == player and
            board[condition[2]] == player
        ):
            return True

    return False


for turn in range(9):

    print_board()

    position = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

    if board[position] == " ":
        board[position] = current_player
    else:
        print("Position already taken!")
        continue

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

else:
    print_board()
    print("Match Draw!")