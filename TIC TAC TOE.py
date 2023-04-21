import os


def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')


board = [' ']*10


def display_example_board(board):

    print('||', board[7], '7' + '  ' + '|' + board[8], '8' + '  ' + '|' + board[9], '9' + '  ', '||')
    print('||', board[4], '4' + '  ' + '|' + board[5], '5' + '  ' + '|' + board[6], '6' + '  ', '||')
    print('||', board[1], '1' + '  ' + '|' + board[2], '2' + '  ' + '|' + board[3], '3' + '  ', '||')


print('You Have come across the game under the name TIC TAC TOE. \n'
      'Below You can notice the board layout showing the arrangement of the squares on the board. \n'
      'To place your mark on the board, use the numbers according to the attached diagram below:')


display_example_board(board)


def display_board(board):

    print('||', board[7] + '  ' + '|' + board[8] + '  ' + '|' + board[9] + '  ', '||')
    print('||', board[4] + '  ' + '|' + board[5] + '  ' + '|' + board[6] + '  ', '||')
    print('||', board[1] + '  ' + '|' + board[2] + '  ' + '|' + board[3] + '  ', '||')


def player_input():
    pInput = ''
    marker1 = 'x'
    marker2 = 'o'
    player1_marker = 'None'
    player2_marker = 'None'

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
            # break

        else:
            continue

    # return (player1_marker, player2_marker)


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


import random

def choose_first():
#this flips a 'coin' to determine which player starts first

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# '_____________________________________________________________________________________________________')


def space_check(board, position):
# checks if the position you wanna put your marker is empty.
    return board[position] == ' '


# '_____________________________________________________________________________________________________')


def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False
    """ if the board is full it will return TRUE. If not i will check and return False"""
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


def replay():

    choice = ''

    while choice not in ['Y', 'N', 'y', 'n']:
        choice = input('Do You want to keep playing? (Y or N)')

        if choice not in ['Y', 'N', 'y', 'n']:
            print('Invalid typo. Type Y or N')

    if choice in ['Y', 'y']:
        return True
    else:
        return False

#-----------------------------------------------------------------------------------------------------------------#
#                                                STARTING THE GAME                                                #


while True:

    # Preparation
    '''set up: board -> choose markers -> who's first'''

    the_board = board                                   #board
    player1_marker, player2_marker = player_input()     #markers. It shows the question from the function in console
    turn = choose_first()                               #whos turn is now
    mark_selected_for_P1 = player1_marker
    mark_selected_for_P2 = player2_marker

    print(turn + ' goes first with -> ' + '', mark_selected_for_P1, '', 'Player 2 goes with -> ' + '', mark_selected_for_P2)

    play_game = input('Are you ready? Y or N ')         #START

    if play_game == 'y' or 'Y':
        game_on = True
    else:
        game_on = False


    ## Gameplay:
    '''player 1 turn -> player 2 turn'''

    while game_on:

        if turn == 'Player 1':
            #SHOW THE BOARD
            clear_output()
            print('\n')
            display_board(the_board)
            #CHOOSE A POSITION FOR THE PLAYERS' MARK ON THE BOARD
            position = player_choice(the_board)
            #PLACE THE MARKER ON THE SELECTED POSITION
            place_marker(the_board, player1_marker, position)
            #CHECK IF THE PLAYER WON WITH HIS RECENT MOVE
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON')
                game_on = False                 # THIS BREAK THE ENTIRE WHILE LOOP AND THE GAME IS OVER
            #CHECK IF THERE IS A TIE RESULTED BY THE RECENT MOVE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('That my friend is called a TIE')
                    game_on = False
                else:
            # NO TIE OR WIN? GAME_ON -> PLAYER 2 TURN
                    turn = 'Player 2'

        else:
            # SHOW THE BOARD
            display_board(the_board)
            # CHOOSE A POSITION FOR THE PLAYERS' MARK ON THE BOARD
            position = player_choice(the_board)
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

# '_____________________________________________________________________________________________________')
