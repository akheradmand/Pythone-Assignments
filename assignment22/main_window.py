# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(229, 310)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gl_tasks = QGridLayout()
        self.gl_tasks.setObjectName(u"gl_tasks")

        self.verticalLayout.addLayout(self.gl_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tb_new_task_title = QLineEdit(self.centralwidget)
        self.tb_new_task_title.setObjectName(u"tb_new_task_title")
        font = QFont()
        font.setPointSize(20)
        self.tb_new_task_title.setFont(font)

        self.horizontalLayout.addWidget(self.tb_new_task_title)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        self.btn_new_task.setFont(font)

        self.horizontalLayout.addWidget(self.btn_new_task)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.time_box = QTimeEdit(self.centralwidget)
        self.time_box.setObjectName(u"time_box")

        self.verticalLayout.addWidget(self.time_box)

        self.date_box = QDateEdit(self.centralwidget)
        self.date_box.setObjectName(u"date_box")

        self.verticalLayout.addWidget(self.date_box)

        self.tb_new_task_description = QTextEdit(self.centralwidget)
        self.tb_new_task_description.setObjectName(u"tb_new_task_description")

        self.verticalLayout.addWidget(self.tb_new_task_description)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 229, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi
