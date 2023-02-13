# import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def check():
    global X_score,Ties,O_score
    for i in range(3):
        if buttons[i][0].text()=="X" and buttons[i][1].text()=="X" and buttons[i][2].text()=="X":
            msg_box=QMessageBox(text="Player1 wins")
            msg_box.exec()
            X_score += 1
            main_window.btn_X_score.setText("'X' Score: " + str(X_score))
            return

        elif buttons[0][i].text()=="X" and buttons[1][i].text()=="X" and buttons[2][i].text()=="X":
            msg_box=QMessageBox(text="Player1 wins")
            msg_box.exec()
            X_score += 1
            main_window.btn_X_score.setText("'X' Score: " + str(X_score))
            return

        elif buttons[i][0].text()=="O" and buttons[i][1].text()=="O" and buttons[i][2].text()=="O":
            msg_box=QMessageBox(text="Player2 wins")
            msg_box.exec()
            O_score += 1
            main_window.btn_O_score.setText("'O' Score: " + str(O_score))
            return

        elif buttons[0][i].text()=="O" and buttons[1][i].text()=="O" and buttons[2][i].text()=="O":
            msg_box=QMessageBox(text="Player2 wins")
            msg_box.exec()
            O_score += 1
            main_window.btn_O_score.setText("'O' Score: " + str(O_score))
            return

    if buttons[0][0].text()=="X" and buttons[1][1].text()=="X" and buttons[2][2].text()=="X":
        msg_box=QMessageBox(text="Player1 wins")
        msg_box.exec()
        X_score += 1
        main_window.btn_X_score.setText("'X' Score: " + str(X_score))
        return

    if buttons[0][2].text()=="X" and buttons[1][1].text()=="X" and buttons[2][0].text()=="X":
        msg_box=QMessageBox(text="Player1 wins")
        msg_box.exec()
        X_score += 1
        main_window.btn_X_score.setText("'X' Score: " + str(X_score))
        return

    if buttons[0][0].text()=="O" and buttons[1][1].text()=="O" and buttons[2][2].text()=="O":
        msg_box=QMessageBox(text="Player2 wins")
        msg_box.exec()
        O_score += 1
        main_window.btn_O_score.setText("'O' Score: " + str(O_score))
        return

    if buttons[0][2].text()=="O" and buttons[1][1].text()=="O" and buttons[2][0].text()=="O":
        msg_box=QMessageBox(text="Player2 wins")
        msg_box.exec()
        O_score += 1
        main_window.btn_O_score.setText("'O' Score: " + str(O_score))
        return

    if buttons[0][0].text()!="" and buttons[0][1].text()!="" and buttons[0][2].text()!="" and buttons[1][0].text()!="" and buttons[1][1].text()!="" and buttons[1][2].text()!="" and buttons[2][0].text()!="" and buttons[2][1].text()!="" and buttons[2][2].text()!="":
        msg_box=QMessageBox(text="Tie!")
        msg_box.exec()
        Ties += 1
        main_window.btn_Ties.setText("Ties: " + str(Ties))
        return

def play(row, col):
    global player
    if player==1:
        if buttons[row][col].text()=="":
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color: red; background-color: pink")
            if cpu==False:
                check()
                player=2
            elif cpu==True:
                while True:
                    row=random.randint(0,2)
                    col=random.randint(0,2)
                    if buttons[row][col].text()=="":
                        buttons[row][col].setText("O")
                        buttons[row][col].setStyleSheet("color: blue; background-color: lightblue")
                        check()
                        player=1
                        break
        else:
            msg_box=QMessageBox(windowTitle="error",text="please choose empty box")
            msg_box.exec()

    elif player==2:
        if buttons[row][col].text()=="":
            buttons[row][col].setText("O")
            buttons[row][col].setStyleSheet("color: blue; background-color: lightblue")
            check()
            player=1
        else:
            msg_box=QMessageBox(windowTitle="error",text="please choose empty box")
            msg_box.exec()
    
def refresh():
    global player
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("color: gray; background-color: lightgray")
            player=1

def about():
    msg_box=QMessageBox(windowTitle="about",text="Tic-tac-toe is a game in which two players take turns in drawing either an ` O' or an ` X' in one square of a grid consisting of nine squares. The winner is the first player to get three of the same symbols in a row.")
    msg_box.exec()

def reset_scores():
    global X_score,Ties,O_score
    X_score=0
    Ties=0
    O_score=0
    main_window.btn_X_score.setText("'X' Score: 0")
    main_window.btn_Ties.setText("Ties: 0")
    main_window.btn_O_score.setText("'O' Score: 0")

def two_player():
    global cpu
    cpu=False
    refresh()
    reset_scores()

def one_player():
    global cpu
    cpu=True
    refresh()
    reset_scores()

# app==QApplication([sys.argv])
app=QApplication([])

loader=QUiLoader()
main_window=loader.load("tic\main.ui")
main_window.show()

player=1
cpu=False
reset_scores()

buttons=([[main_window.btn1,main_window.btn2,main_window.btn3],
        [main_window.btn4,main_window.btn5,main_window.btn6],
        [main_window.btn7,main_window.btn8,main_window.btn9]])

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

main_window.btn_refresh.clicked.connect(refresh)
main_window.btn_about.clicked.connect(about)
main_window.btn_2player.clicked.connect(two_player)
main_window.btn_1player.clicked.connect(one_player)

app.exec()