# This is GUI for TIC-TAC-TOE game
import tkinter as tk
from random import randrange
from tkinter.constants import DISABLED, NORMAL
from tkinter import PhotoImage, Toplevel, messagebox

# from typing_extensions import IntVar

window = tk.Tk()
window.geometry("330x330")
window.title("TIC TAC TOE GAME")
ip = PhotoImage(file='icon.png')
window.iconphoto(False,ip)

# game_title_label = tk.Label(window, text='TIC TAC TOE GAME')
# game_title_label.place(x=10, y=7)

# Write function here
update_board = [
        ['','',''],
        ['','',''],
        ['','','']
        ]

# check free board
def freeboard(board):
    free_board = []
    for i in range(len(board)):
        for j in range(len(board)):
            if ('X' == board[i][j]) or ('O' == board[i][j]):
                continue
            else:
                free_board.append(tuple([i,j]))
    return free_board

# check the winner
cx = 0
co = 0
def winner(sign,m,n):
    global update_board
    global cx 
    global co
    dimension = len(update_board)
    # sign = player_select()
    # cx = 0
    # co = 0
    if sign == 'X':
        cx += 1
        # computer_move()
        update_board[m][n] = board[m][n]['text']
        for i in range(dimension):
            cr,cc,cld,crd,l = 0,0,0,0,2
            for j in range(dimension):
                if update_board[i][j] == sign:
                    cr += 1 
                
                if update_board[j][i] == sign:
                    cc += 1 
                
                if update_board[j][j] == sign:
                    crd += 1
                
                if update_board[j][l] == sign:
                    cld += 1
                    l -= 1
                
            if cr == 3 or cc == 3 or crd == 3 or cld == 3:
                # print('Computer Win')
                messagebox.showinfo('Winner','Computer Win')
                return
        if (cx + co) == 9:
            # print('Draw')
            messagebox.showinfo('Winner','Draw')
    elif sign == 'O':
        co += 1
        # player_move(m,n)
        update_board[m][n] = board[m][n]['text']
        for i in range(dimension):
            cr,cc,cld,crd,l = 0,0,0,0,2
            for j in range(dimension):
                if update_board[i][j] == sign:
                    cr += 1 
                
                if update_board[j][i] == sign:
                    cc += 1 
                
                if update_board[j][j] == sign:
                    crd += 1
                
                if update_board[j][l] == sign:
                    cld += 1
                    l -= 1
                
            if cr == 3 or cc == 3 or crd == 3 or cld == 3:
                # print('You Win')
                messagebox.showinfo('Winner','You Win')
                return
        if (cx + co) == 9:
            print('Draw')
        else:
            computer_move()
    return 

# Button function
def computer_move():
    # Board game index
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

    n = 9
    if len(freeboard(update_board)) == 1:
        fb = freeboard(update_board)
        i = fb[0][0]
        j = fb[0][1]
    else:
        computer_input = str(randrange(1,n))
        i = opt[computer_input][0]
        j = opt[computer_input][1]

    sign = 'X'
    if board[i][j]['text'] == '':
        board[i][j].config(text=sign, bg='red',fg='white')
        winner(sign,i,j)
    elif board[i][j]['text'] == 'O':
        computer_move()
    elif board[i][j]['text'] == 'X':
        computer_move()
    return

# player movement
def player_move(i,j):
    sign = 'O'
    board[i][j].config(text=sign,bg='cyan',fg='black')
    winner(sign,i,j)
    return

# Player select function
def player_select():
    # radvar.set(0)
    if radvar.get() == 1:
        sign = 'X'
        computer_move()
        for i in range(3):
            for j in range(3):
                board[i][j]["state"] = NORMAL
    elif radvar.get() == 2:
        sign = 'O'
        for i in range(3):
            for j in range(3):
                board[i][j]["state"] = NORMAL
    else:
        sign = 'Please select player'
    return sign

# Reset game
def reset_game():
    # print('Reset Game')
    global update_board
    global co
    global cx
    radvar.set(0)
    co = 0
    cx = 0
    update_board = [
        ['','',''],
        ['','',''],
        ['','','']
        ]
    for i in range(3):
        for j in range(3):
            board[i][j].config(text='', bg='yellow')
            board[i][j]['state'] = DISABLED
    return

# board label
board = [
    ['','',''],
    ['','',''],
    ['','','']
]

# -------------------GUI-------------------#
# toplevel = Toplevel()
messagebox.showinfo('Info','Please select the first turn!')

# Select player Frame
frame_player = tk.Frame(
    window
    )
frame_player.place(
    x=20,
    y=5
)

radvar = tk.IntVar()
computer_first = tk.Radiobutton(
    frame_player,
    text='Computer First',
    value=1,
    variable=radvar,
    command=player_select
)
computer_first.grid(
    row=0,
    column=0
)
player_first = tk.Radiobutton(
    frame_player,
    text='Player First',
    variable=radvar,
    value=2,
    command=player_select   
)
player_first.grid(
    row=0,
    column=1
)

# button frame
frame_button = tk.Frame(
    window,
    background='white'
    )
frame_button.place(
    x=25,
    y=35)

dimension = 3
for i in range(dimension):
    for j in range(dimension):
        board[i][j] = tk.Button(
            frame_button,
            height=5,
            width=10,
            text=board[i][j],
            command=lambda i=i, j=j: player_move(i,j),
            state=DISABLED,
            bg='yellow'
            )
        board[i][j].grid(
            row=i,
            column=j,
            padx=5,
            pady=5
            )

# frame reset button
frame_reset = tk.Frame(
    window
)
frame_reset.place(
    x=230,
    y=5
)
reset_button = tk.Button(
    frame_reset,
    text='Play Again',
    command=reset_game
)
reset_button.grid(
    row=0,
    column=0
)
window.mainloop()