import random

def display_board(board):

print()

print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])

print('---+---+---')

print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])

print('---+---+---')

print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

print()

def player_choice():

    symbol = ''

    while symbol not in ['X', 'O']:

            symbol = input("Do you want to be 'X' or 'O'? ").upper()

            return ('X', 'O') if symbol == 'X' else ('O', 'X')

def player_move(board, symbol):

    move = -1

    while move not in range(1, 10) or not board[move - 1].isdigit():

        try:

            move = int(input("Enter your move (1-9): "))

        except ValueError:

            print("Please enter a number between 1 and 9")

            board[move - 1] = symbol

def ai_move(board, ai_symbol, player_symbol):

    for i in range(9):

        if board[i].isdigit():

            copy = board.copy()

            copy[i] = ai_symbol

        if check_win(copy, ai_symbol):

            board[i] = ai_symbol

            return

    for i in range(9):

        if board[i].isdigit():

        copy = board.copy()

        copy[i] = player_symbol

        if check_win(copy, player_symbol):

            board[i] = ai_symbol

            return

    moves = [i for i in range(9) if board[i].isdigit()]

    board[random.choice(moves)] = ai_symbol

def check_win(board, symbol):

    wins = [

    (0,1,2),(3,4,5),(6,7,8),

    (0,3,6),(1,4,7),(2,5,8),

    (0,4,8),(2,4,6)

]

    return any(board[a] == board[b] == board[c] == symbol for a,b,c in wins)

def check_full(board):

     return all(not cell.isdigit() for cell in board)
def tic_tac_toe():

    print("Welcome to Tic Tac Toe")

    name = input("Enter your name: ")

    board = ['1','2','3','4','5','6','7','8','9']

    player_symbol, ai_symbol = player_choice()

    turn = 'Player'

    while True:

        display_board(board)

        if turn == 'Player':

            player_move(board, player_symbol)

            if check_win(board, player_symbol):

                display_board(board)

                 
                print(f"Congratulations {name}! You won!")

                break

            turn = 'AI'

            else:

                ai_move(board, ai_symbol, player_symbol)

        if check_win(board, ai_symbol):

            display_board(board)

            print("AI has won!")

            break

        turn = 'Player'

if check_full(board):

    display_board(board)

    print("It's a tie!")

    break

if __name__ == "__main__":

    tic_tac_toe()