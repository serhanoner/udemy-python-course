import random
def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
 
 
test_board = ['# ','X','O','X','O','X','O','X','O','X']
 
 
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
 
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    player1_marker , player2_marker = player_input()
 
def place_marker(board, marker, position):
    board[position] = marker
 
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
 
def choose_first():
    flip = random.randint(0,1)
    if flip ==0:
        return 'Player 1'
    else:
        return 'Player 2'
 
def space_check(board, position):
    
    return board[position] == ' '
 
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False #board not full
    return True #board is full if return true 
def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your next position(1-9): '))
        
    return position
 
def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
 
print('Welcome to Tic Tac Toe')
 
while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + 'Will go first!')
    play_game = input('Ready to play? y or n? ')
    if play_game =='y':
        game_on = True
    else:
        game_on = False
 
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has Won!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has Won!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 1'
 
             
    if not replay():
        break