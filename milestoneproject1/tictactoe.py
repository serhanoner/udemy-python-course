from IPython.display import clear_output

def display_board(board):
    clear_output()
    print (board[7] + "|" + board[8] + "|" + board[9])
    print (board[4] + "|" + board[5] + "|" + board[6])
    print (board[1] + "|" + board[2] + "|" + board[3])
    


def player_input():

    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    
    if marker == "X":
        return ("X","O")
    else:
        return ("O","X")
    
    player1_marker , player2_marker = player_input()
    
def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,marker):
#rows
    if marker == board[1] and marker == board[2] and marker == board[3]:
        return True
    elif marker == board[4] and marker == board[5] and marker == board[6]:
        return True
    elif marker == board[7] and marker == board[8] and marker == board[9]:
        return True
#diagonals
    elif marker == board[1] and marker == board[5] and marker == board[9]:
        return True
    elif marker == board[3] and marker == board[5] and marker == board[7]:
        return True

#columns
    elif marker == board[1] and marker == board[4] and marker == board[7]:
        return True
    elif marker == board[2] and marker == board[5] and marker == board[8]:
        return True
    elif marker == board[3] and marker == board[6] and marker == board[9]:
        return True
    
    


import random

def choose_first():
    if random.randint(0,1) == 1:
        return "Player 2"
    else:
        return "Player 1"
    

def space_check(board,position):

    return board[position] == " "
    

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')




print('Welcome to Tic Tac Toe!')

while True:
    the_board = [" "]*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n: ")

    if play_game == "y":
        game_on = True
    else:
        game_on = False 
    
    while game_on:

        if turn == "Player 1":
            display_board(the_board)
            
            position = player_choice(the_board)

            place_marker(the_board, player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie.")
                    game_on = False
                else:
                    turn = "Player 2"
        else:
            display_board(the_board)
            
            position = player_choice(the_board)

            place_marker(the_board, player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 2 has won!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie.")
                    game_on = False
                else:
                    turn = "Player 1"


    if not replay():
        break

