# Task from Python Institute (https://pythoninstitute.org/certification/)
# Scenario
# Your task is to write a simple program which pretends to play tic-tac-toe with the user.
# To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

# 1. the computer (i.e., your program) should play the game using 'X's;
# 2. the user (e.g., you) should play the game using 'O's;
# 3. the first move belongs to the computer - it always puts its first 'X' in the middle of the board;
# 4. all the squares are numbered row by row starting with 1 (see the example session below for reference)
# 5. the user inputs their move by entering the number of the square they choose - the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# 6. the program checks if the game is over - there are four possible verdicts: the game should continue, or the game ends with a tie, your win, or the computer's win;
# 7. the computer responds with its move and the check is repeated;
# 8. don't implement any form of artificial intelligence - a random field choice made by the computer is good enough for the game.

from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    free_board = make_list_of_free_fields(board)
    # print(free_board)
    print('Current free board number:',len(free_board))

    n = len(board)
    for j in range(n):
        print('+','+','+','+',sep='-'*7)
        print('|','|','|','|', sep=' '*7)
        print('|',board[j][0],'|',board[j][1],'|',board[j][2],'|', sep=' '*3)
        print('|','|','|','|', sep=' '*7)
    print('+','+','+','+', sep='-'*7)

    return 


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.

    print('Your Move...')

    opt = {
        '1':(0,0),
        '2':(0,1),
        '3':(0,2),
        '4':(1,0),
        '5':(1,1),
        '6':(1,2),
        '7':(2,0),
        '8':(2,1),
        '9':(2,2)
    }

    your_sign = 'O'
    your_input = str(input('Select a board number: '))

    your_row = opt[your_input][0]
    your_col = opt[your_input][1]
    board[your_row][your_col] = your_sign

    display_board(board)
    return


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    # print(board)

    free_board = []
    for i in range(len(board)):
        for j in range(len(board)):
            if ('X' == board[i][j]) or ('O' == board[i][j]):
                continue
            else:
                free_board.append(tuple([i,j]))

    return free_board


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game

    count_x = 0
    count_o = 0
    for i in range(9):
        if sign == 'X':
            count_x += 1
            draw_move(board)
            for j in range(len(board)):
                count_row = 0
                count_col = 0
                count_rdiag = 0
                count_ldiag = 0
                l = 2
                for k in range(len(board)):
                    if board[j][k] == sign:
                        count_row += 1
                    
                    if board[k][j] == sign:
                        count_col += 1
                    
                    if board[k][k] == sign:
                        count_rdiag += 1

                    if board[k][l] == sign:
                        count_ldiag += 1
                        l -= 1

                print('count_row X: ', count_row) 
                print('X:', count_x, 'O:', count_o) 
                if count_row == 3 or count_col == 3 or count_rdiag == 3 or count_ldiag == 3:
                    print('Computer Win !!!')
                    stop = True
                    break 
                else:
                    stop = False
                    continue
            
            if (count_x + count_o) == 9:
                    print('Draw !!!')
                    return
            else:
                if stop:
                    break
                else: 
                    sign = 'O'
        else:
            count_o += 1
            enter_move(board)
            for j in range(len(board)):
                count_row = 0
                count_col = 0
                count_rdiag = 0
                count_ldiag = 0
                l = 2
                for k in range(len(board)):
                    if board[j][k] == sign:
                        count_row += 1

                    if board[k][j] == sign:
                        count_col += 1

                    if board[k][k] == sign:
                        count_rdiag += 1

                    if board[k][l] == sign:
                        count_ldiag += 1
                        l -= 1

                print('count_row O: ', count_row)
                print('X:', count_x, 'O:', count_o)
                if count_row == 3 or count_col == 3 or count_rdiag == 3 or count_ldiag == 3:
                    print('You Win !!!')
                    stop = True 
                    break
                else:
                    stop = False 
                    continue

            if (count_x + count_o) == 9:
                print('Draw !!!')
                return
            else:
                if stop:
                    break
                else: 
                    sign = 'X'
    # return


def draw_move(board):
    # The function draws the computer's move and updates the board.

    print('Computer Move...')

    opt = {
        '1':(0,0),
        '2':(0,1),
        '3':(0,2),
        '4':(1,0),
        '5':(1,1),
        '6':(1,2),
        '7':(2,0),
        '8':(2,1),
        '9':(2,2)
    }

    comp_sign = 'X'
    n = 9

    if len(make_list_of_free_fields(board)) == 1:
        fb = make_list_of_free_fields(board)
        fb_row = fb[0][0]
        fb_col = fb[0][1]
        board[fb_row][fb_col] = comp_sign
        display_board(board)
        return
    else:
        comp_input = str(randrange(1,n))
    
    print('Computer Input: ',comp_input) 

    comp_row = opt[comp_input][0]
    comp_col = opt[comp_input][1]

    if board[comp_row][comp_col] == 'O':
        draw_move(board)
    elif  board[comp_row][comp_col] == 'X':
        draw_move(board)
    else:
        board[comp_row][comp_col] = comp_sign
    
    display_board(board)
    # return


# MAIN PROGRAM
board = [[1,2,3],[4,5,6],[7,8,9]]
display_board(board)
turn = 'O'
victory_for(board, turn)