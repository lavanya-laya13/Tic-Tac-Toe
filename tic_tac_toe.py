# tic_tac_toe.py

def print_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(cell != ' ' for cell in board)

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move >= 9 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
            board[move] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"🎉 Player {current_player} wins!")
                break
            elif is_draw(board):
                print("It's a draw! 🤝")
                break

            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Please enter a valid number (1-9).")

if __name__ == "__main__":
    tic_tac_toe()
