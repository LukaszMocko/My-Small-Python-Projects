import os
import random

board = [' ']*10

# '_____________________________________________________________________________________________________'

def clear_output(board):
    os.system('cls' if os.name == 'nt' else 'clear')

# '_____________________________________________________________________________________________________'

def display_example_board(board):

    print('||', board[7], '7' + '  ' + '|' + board[8], '8' + '  ' + '|' + board[9], '9' + '  ', '||')
    print('||', board[4], '4' + '  ' + '|' + board[5], '5' + '  ' + '|' + board[6], '6' + '  ', '||')
    print('||', board[1], '1' + '  ' + '|' + board[2], '2' + '  ' + '|' + board[3], '3' + '  ', '||')

# '_____________________________________________________________________________________________________'

print('You Have come across the game under the name TIC TAC TOE. \n'
      'Below You can notice the board layout showing the arrangement of the squares on the board. \n'
      'To place your mark on the board, use the numbers according to the attached diagram below:')


display_example_board(board)

# '_____________________________________________________________________________________________________'

def display_board(board):

    print('||', board[7] + '   ' + '|' + board[8] + '  ' + '|' + board[9] + '  ', '||')
    print('||', board[4] + '   ' + '|' + board[5] + '  ' + '|' + board[6] + '  ', '||')
    print('||', board[1] + '   ' + '|' + board[2] + '  ' + '|' + board[3] + '  ', '||')

# '_____________________________________________________________________________________________________'

marker1 = 'x'
marker2 = 'o'

def player_input():
    pInput = ''


    while pInput != marker1 or pInput != marker2:
        pInput = input(' Choose your marker Player 1: "X" or "O"')

        if pInput == marker1 or pInput == marker2:
            player1_marker = pInput

            if player1_marker == marker1:
                # player2_marker = marker2
                return ('X', 'O')

            else:
                # player2_marker = marker1
                return ('O', 'X')

        else:
            continue

    return marker1, marker2

# '_____________________________________________________________________________________________________'

def place_marker(board, marker, position):

    board[position] = marker

# '_____________________________________________________________________________________________________'

def win_check(board, mark):

    ''' we need to check if the same mark is in all 3 dimensions:'''
    return ((board[7] == board[8] == board[9]) == mark or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

# '_____________________________________________________________________________________________________')

def player_display():

    if player1_marker == marker1 or marker2:
        return 'Player 1'

# '_____________________________________________________________________________________________________'

def space_check(board, position):
# checks if the position you wanna put your marker is empty.
    return board[position] == ' '

# '_____________________________________________________________________________________________________')

moves_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def player2_input(board, moves_list):

    possible_moves = []

    for i in moves_list:
        if space_check(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        win_check(the_board, player2_marker)

# '_____________________________________________________________________________________________________')

def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    """ if the board is full it will return TRUE. If not it will check and return False"""
    return True

# '_____________________________________________________________________________________________________')

def player_choice(board):

    position = ''

    while position not in range(1,10) or not space_check(board, position) or not int:
        try:
            position = int(input('Choose an empty space to put your marker (1-9):'))
        except ValueError:
            print('Sorry, this is not a number.')

    return position

# '_____________________________________________________________________________________________________')

def play():

    play_game = ''
    while play_game not in ['Y', 'N']:
        play_game = input('Are you ready? Y or N ')
        play_game = play_game.upper()
        if play_game not in ['Y', 'N']:
            print('Invalid typo. Type Y or N.')

    if play_game.upper() == 'Y':
        return True
    else:
        return False

# '_____________________________________________________________________________________________________')

def replay():

    choice = ''

    while choice not in ['Y', 'N']:
        choice = input('Do You want to keep playing? (Y or N)')
        choice = choice.upper()
        if choice not in ['Y', 'N']:
            print('Invalid typo. Type Y or N')

    if choice.upper() == 'Y':
        return True
    else:
        return False

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                   STARTING THE GAME                                                                                #

while True:

    # Preparation

    the_board = board                                                   # board

    # START

    game_on = True
    player1_marker, player2_marker = player_input()  # markers. It shows the question from the function in console
    turn = player_display()
    print(turn + ' goes first with -> ' + '', player1_marker, '', 'Player 2 goes with -> ' + '', player2_marker)

    if not play():
        print('Thanks for.... nothing. Bye')
        break

    # Gameplay:

    while game_on:

        if turn == 'Player 1':
            print('\n Player 1 turn.')
            # SHOW THE BOARD
            display_board(the_board)
            # CHOOSE A POSITION FOR THE PLAYERS' MARK ON THE BOARD
            position = player_choice(the_board)
            # PLACE THE MARKER ON THE SELECTED POSITION
            place_marker(the_board, player1_marker, position)
            # CHECK IF THE PLAYER WON WITH HIS RECENT MOVE
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False                 # THIS BREAK THE ENTIRE WHILE LOOP AND THE GAME IS OVER
            # CHECK IF THERE IS A TIE RESULTED BY THE RECENT MOVE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('That my friend is called a TIE')
                    game_on = False
                else:
            # NO TIE OR WIN? GAME_ON -> PLAYER 2 TURN
                    turn = 'Player 2'
                    print('\n Player 2 turn.')

        else:
            # SHOW THE BOARD
            display_board(the_board)
            # CHOOSE A POSITION FOR THE PLAYERS' MARK ON THE BOARD
            position = player2_input(the_board, moves_list)
            # PLACE THE MARKER ON THE SELECTED POSITION
            place_marker(the_board, player2_marker, position)
            # CHECK IF THE PLAYER WON WITH HIS RECENT MOVE
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON')
                game_on = False  # THIS BREAK THE ENTIRE WHILE LOOP AND THE GAME IS OVER
            # CHECK IF THERE IS A TIE RESULTED BY THE RECENT MOVE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('That my friend is called a TIE')
                    game_on = False
                else:
                    # NO TIE OR WIN? GAME_ON -> PLAYER 1 TURN
                    turn = 'Player 1'


    if not replay():
        print('Thanks for the game')
        break
    else:
        board = [' ']*10

# '_____________________________________________________________________________________________________')
