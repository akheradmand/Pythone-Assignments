import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.db=Database()

        self.read_from_database()

        self.ui.btn_new_task.clicked.connect(self.new_task)

    def new_task(self):
        new_title=self.ui.tb_new_task_title.text()
        new_description=self.ui.tb_new_task_description.toPlainText()
        feedback=self.db.add_new_task(new_title,new_description)
        if feedback==True:
            for i in reversed(range(self.ui.gl_tasks.count())): 
                self.ui.gl_tasks.itemAt(i).widget().setParent(None)
            self.read_from_database()
        else:
            msg_box= QMessageBox
            msg_box.setText("مشکلی رخ داده است")
            msg_box.exec_()

        self.ui.tb_new_task_title.setText("")
        self.ui.tb_new_task_description.setText("")

    def remove(self,id):
        feedback=self.db.remove_task(id)
        if feedback==True:
            for i in reversed(range(self.ui.gl_tasks.count())): 
                self.ui.gl_tasks.itemAt(i).widget().setParent(None)
            self.read_from_database()
        else:
            msg_box= QMessageBox
            msg_box.setText("مشکلی رخ داده است")
            msg_box.exec_()

    def read_from_database(self):
        tasks=self.db.get_tasks()
        # print(tasks)
        for i in range(len(tasks)):
            new_checkbox=QCheckBox()
            new_label=QLabel()
            new_label2=QLabel()
            new_btn=QPushButton()
            
            if tasks[i][3]==1:
                new_checkbox.setChecked(True)
            else:
                new_checkbox.setChecked(False)

            new_label.setText(tasks[i][1])
            if tasks[i][4]==1:
                new_label.setStyleSheet("background-color:red")
            elif tasks[i][4]==0:
                new_label.setStyleSheet("background-color:pink")

            new_label2.setText(tasks[i][2])
            new_btn.setText("❌")

            self.ui.gl_tasks.addWidget(new_checkbox, i, 0)
            self.ui.gl_tasks.addWidget(new_label, i, 1)
            self.ui.gl_tasks.addWidget(new_label2, i, 2)
            self.ui.gl_tasks.addWidget(new_btn, i, 3)

            new_checkbox.clicked.connect(partial(self.db.task_done,tasks[i][0]))
            new_btn.clicked.connect(partial(self.remove,tasks[i][0]))

if __name__ == "__main__":
    app=QApplication(sys.argv)

    main_window=MainWindow()
    main_window.show()

    app.exec_()