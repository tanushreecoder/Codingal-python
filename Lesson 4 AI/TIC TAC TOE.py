import random
def display_board(board):
    print()
    print('  ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
    print('---+---+---')
    print('  ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' | ')
    print('---+---+---')
    print('  ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' | ')
    print()
def player_choise():
    symbol = ' '
    while symbol not in ['X', 'O']:
        symbol = input("Do yo want to be 'X' or ')'? ").upper()
    if symbol == 'X':
        return('X', 'O')
    else:
        return('O', 'X')
def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            print("Invalid move, please try again")
        except ValueError:
            print("Please enter a number between 1 to 9")
    board[move - 1] = symbol
def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = player_symbol
                return        
    possible_moves = [i for 1 in range(9) if board[i].isdigit()]
    moves = random.choice(possible_moves)
    board[moves] = ai_symbol
def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8)
        (0, 3, 6), (1, 4, 7), (2, 5, 8)
        (0, 4, 8), (2, 4, 6)
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[2]] == symbol:
            return True
    return False
def tic_tac_toe():
    print("Welcome to tic tac toe")
    player_name = input("Enter your name: ")
    turn = 'Player'
    game_on = True
    while game_on:
        display_board(board):
        if turn == 'Player':
            player_move(board, player_symbol)
            if check_win(board, player_symbol):
                display_board(board)
                print(f"Congradulations {player_name}! You won!")
                game_on = False
            elif check_full(board):
                display_board(board)
                print("It's a tie")
                break
            else:
                turn = "AI"
        else:

            ai_move(board, ai_symbol, player_symbol)

            if check_win(board, ai_symbol):

                display_board(board)

                print("AI has won the game!")

                game_on = False

            elif check_full(board):

                display_board(board)

                print("It's a tie!")

                break

            else:

                turn = 'Player'

play_again = input("Do you want to play again? (yes/no): ").lower()

if play_again != 'yes':

    print("Thank you for playing!")

   break

if __name__ == "__main__":

    tic_tac_toe()