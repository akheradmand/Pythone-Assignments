import pyfiglet
import numpy as np
import colorama
from colorama import Fore
import time

def show():
    for r in game_board:
        for c in r:
            if c=="-":
                print(Fore.WHITE,c,end=' ')
            elif c=="x":
                print(Fore.RED,c,end=' ')
            elif c=="o":
                print(Fore.BLUE,c,end=' ')
        print(Fore.WHITE,"")

def check_game():
    # global elapsed_time
    # global start_time
    # global end_time

    tr_game_board=np.array(game_board).T.tolist() #transpose game_board
    for i in range(3):
        # print(set(game_board[i]))
        if len(set(game_board[i]))==1 and list(set(game_board[i]))==["x"]:
            print("player 1 wins!")
            exit()
        elif len(set(tr_game_board[i]))==1 and list(set(tr_game_board[i]))==["x"]:
            print("player 1 wins!")
            exit()
        elif len(set(game_board[i]))==1 and list(set(game_board[i]))==["o"]:
            print("player 2 wins!")
            exit()
        elif len(set(tr_game_board[i]))==1 and list(set(tr_game_board[i]))==["o"]:
            print("player 2 wins!")
            exit()
    
    if game_board[0][0]=="x" and game_board[1][1]=="x" and game_board[2][2]=="x":
        print("player 1 wins!")
        exit()
    elif game_board[0][0]=="o" and game_board[1][1]=="o" and game_board[2][2]=="o":
        print("player 2 wins!")
        exit()
    elif game_board[0][2]=="x" and game_board[1][1]=="x" and game_board[2][0]=="x":
        print("player 1 wins!")
        exit()
    elif game_board[0][2]=="o" and game_board[1][1]=="o" and game_board[2][0]=="o":
        print("player 2 wins!")
        exit()

    # for i in range(3):
    #     for j in range(3):
    #         if game_board[i][j]=="-":
    #             break
    #     else:
    #         continue
    # print("no winer")
    # exit()

    # end_time=time.time()
    # elapsed_time= end_time-start_time

def player1():
    ...

def player2():

    ...

title = pyfiglet.figlet_format("Tic Tac Toe",font="slant")

print(title)

player=input("enter '1' for play with computer or '2' for two-players= ")

if player==1:
    ...
elif player==2:
    ...

game_board= [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]
show()

# start_time=time.time()
# end_time=0
# elapsed_time=0

while True:
    
    print("player1")
    while True:
        row= int(input("row: "))
        col= int(input("col: "))

        if 0<=row<=2 and 0<=col<=2:

            if game_board[row][col]=="-":
                game_board[row][col]="x"
                break
            else:
                print("jer nazan :/")
        else:
            print("mese adam vared kon :|")

    show()
    check_game()

    print("player2")
    while True:
        row= int(input("row: "))
        col= int(input("col: "))

        if 0<=row<=2 and 0<=col<=2:

            if game_board[row][col]=="-":
                game_board[row][col]="o"
                break
            else:
                print("jer nazan :/")
        else:
            print("mese adam vared kon :|")

    show()
    check_game()

# print("elapsed_time= ", elapsed_time)
