# import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def check():
    if buttons[0][0].text()=="X" and buttons[0][1].text()=="X" and buttons[0][2].text()=="X":
        # print("player1 wins")
        msg_box=QMessageBox(text="Player1 wins")
        msg_box.exec()

def play(row, col):
    global player
    if player==1:
        buttons[row][col].setText("X")
        buttons[row][col].setStyleSheet("color: red; background-color: pink")
        player=2
    
    elif player==2:
        buttons[row][col].setText("O")
        buttons[row][col].setStyleSheet("color: blue; background-color: lightblue")
        player=1

    check()

# app==QApplication([sys.argv])
app=QApplication([])

player=1

loader=QUiLoader()
main_window=loader.load("tic\main.ui")
main_window.show()
# main_window.btn1.clicked.connect(partial(play, 0, 0))
# main_window.btn2.clicked.connect(partial(play, 0, 1))
# main_window.btn3.clicked.connect(partial(play, 0, 2))
# main_window.btn4.clicked.connect(partial(play, 1, 0))
# main_window.btn5.clicked.connect(partial(play, 1, 1))
# main_window.btn6.clicked.connect(partial(play, 1, 2))
# main_window.btn7.clicked.connect(partial(play, 2, 0))
# main_window.btn8.clicked.connect(partial(play, 2, 1))
# main_window.btn9.clicked.connect(partial(play, 2, 2))

buttons=([[main_window.btn1,main_window.btn2,main_window.btn3],
        [main_window.btn4,main_window.btn5,main_window.btn6],
        [main_window.btn7,main_window.btn8,main_window.btn9]])

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

app.exec()