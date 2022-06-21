# Assignment: Ponder and Prove 1
# Name: Christopher Larson

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    if is_a_draw(board) == True:
        print('\nThe game is a draw!')
    elif has_winner(board) == True:
        if next_player(player) == 'x':
            print('x\'s player has won!')
        elif next_player(player) == 'o':
            print('o\'s player has won!')

# Creates a board with 9 squares filled with numbers
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

# Prints the design of the board with the numbers and layout
def display_board(board):
    print(f"\n{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}\n")
    
    
# Checks if all squares are filled
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 
    
# Checks for possible winning combinations
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# Gets user input to fill a square on the board
def make_move(player, board):
    turn_over = False
    while turn_over == False:
        square = int(input(f"{player}'s turn to choose a square (1-9): "))
        if type(board[square-1]) == int:
            board[square - 1] = player
            turn_over = True
        else:
            print('You must choose an unoccupied square.')

# Determines whose turn it is
def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


if __name__ == "__main__":
    main()