import sys
import sqlite3
from random import sample, shuffle
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import (
    QApplication, QPushButton, QFrame, QLineEdit,
    QMessageBox, QStackedWidget, QMainWindow,
    QDialog, QWidget, QFileDialog, QTextEdit,
    QListWidgetItem, QCalendarWidget, QVBoxLayout, QLabel
)
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal, QTimer, Qt
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pygetwindow as gw
import matplotlib.pyplot as plt
from PyQt5.uic import loadUi
import os
import shutil

# Add your resources
import stripes_rc
import icons_rc
import wellbeing_rc

class Ui_MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):  
        loadUi("myapp/Resources/loginui.ui", self)
        self.signup_tab = self.findChild(QPushButton, "signup")
        self.login_button = self.findChild(QPushButton, "Login_button")
        self.login_username = self.findChild(QLineEdit, "username")
        self.login_password = self.findChild(QLineEdit, "username_2")

        # Connect the signal after loading the UI
        self.login_button.clicked.connect(self.login_button_clicked)
        self.signup_tab.clicked.connect(self.signup_clicked)
        
        # Add the following line to set the layout for the main window
        self.setLayout(self.layout())

    def login_button_clicked(self):
        username = self.login_username.text()
        password = self.login_password.text()

        # Add your login validation logic here
        if self.check_credentials(username, password):
                # self.show_message("Login Successful")
                landing = LandingPage(parent = widget)
                widget.addWidget(landing)
                widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            self.show_message("Login Failed")

    def check_credentials(self, username, password):
        connection = sqlite3.connect("studentapp.db")
        cursor = connection.cursor()

        # Check if the username and password match a record in the database
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        connection.close()

        return user is not None

    def signup_clicked(self):
        signupwin = SignupWindow()
        widget.addWidget(signupwin)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def show_message(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Info")
        msg.exec_()

class SignupWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loadUi("myapp/Resources/signupui.ui", self)
        self.signup_button = self.findChild(QPushButton, "Login_button")
        self.logintab_button = self.findChild(QPushButton, "Login")
        self.username_signup = self.findChild(QLineEdit, "username")
        self.line_password = self.findChild(QLineEdit, "username_2")
        self.line_email = self.findChild(QLineEdit, "username_3")
        self.line_contact = self.findChild(QLineEdit, "username_4")

        # Connect the signal after loading the UI
        self.signup_button.clicked.connect(self.on_signup)
        self.logintab_button.clicked.connect(self.login_clicked)
        
    def login_clicked(self):
        loginwin = Ui_MainWindow()
        widget.addWidget(loginwin)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def on_signup(self):
        username = self.username_signup.text()
        password = self.line_password.text()
        email = self.line_email.text()
        contact = self.line_contact.text()

        connection = sqlite3.connect('studentapp.db')
        cursor = connection.cursor()

        # Check if the user already exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            QMessageBox.warning(self, 'Signup Error', 'Username already exists. Please choose a different one.')
        else:
            # Insert the new user
            cursor.execute('INSERT INTO users (username, password,email,contact) VALUES (?, ?, ?, ?)',
                           (username, password, email, contact))
            connection.commit()
            connection.close()

            QMessageBox.information(self, 'Signup Successful', 'Account created for {}'.format(username))

    def login_window_closed(self):
        # Re-enable the signup window when the login window is closed
        self.setDisabled(False)

    def reset_ui(self):
        # Reset UI components as needed
        self.username_signup.clear()
        self.line_password.clear()
        self.line_email.clear()
        self.line_contact.clear()

class LandingPage(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 644)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"  border: none;\n"
"  background-color: transparent;\n"
"  color: #FFF; /* Specify a default color */\n"
"}\n"
"\n"
"#centralwidget {\n"
"  background-color: white\n"
";\n"
"}\n"
"\n"
"#side_menu {\n"
"  background-color: #071e26;\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  padding: 10px;\n"
"  background-color: #071e26;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"#main_body {\n"
"  background-color: #071e26;\n"
"  border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons_folder/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.frame_2)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.side_menu)
        self.frame_4.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons_folder/airplay.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons_folder/camera.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons_folder/github.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons_folder/coffee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons_folder/music.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.gridLayout = QtWidgets.QGridLayout(self.main_body)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_11 = QtWidgets.QFrame(self.main_body)
        self.frame_11.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Welcome = QtWidgets.QLabel(self.frame_11)
        self.Welcome.setStyleSheet("position: absolute;\n"
"width: 310px;\n"
"height: 80px;\n"
"\n"
"\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 34px;\n"
"line-height: 92px;\n"
"\n"
"color: #7A999C;\n"
"background : transparent;")
        self.Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome.setObjectName("Welcome")
        self.verticalLayout_10.addWidget(self.Welcome)
        self.Welcome_2 = QtWidgets.QLabel(self.frame_11)
        self.Welcome_2.setStyleSheet("position: absolute;\n"
"width: 310px;\n"
"height: 80px;\n"
"\n"
"\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size: 20px;\n"
"line-height: 92px;\n"
"\n"
"color: #7A999C;\n"
"background : transparent;")
        self.Welcome_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Welcome_2.setObjectName("Welcome_2")
        self.verticalLayout_10.addWidget(self.Welcome_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_10)
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6.addWidget(self.frame_12)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_8 = QtWidgets.QFrame(self.main_body)
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame_8)
        self.label_2.setStyleSheet("image: url(:/wel/welbeing_1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.frame_8)
        self.label_4.setStyleSheet("color:black;\n"
"font-size:20px;\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 600;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.horizontalLayout_4.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.main_body)
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setStyleSheet("image: url(:/wel/welbeing_2.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_9)
        self.label_5.setStyleSheet("color:black;\n"
"font-size:20px;\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 600;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.main_body)
        self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame_10)
        self.label_6.setStyleSheet("image: url(:/wel/welbeing_3.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        self.label_7.setStyleSheet("color:black;\n"
"font-size:20px;\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 600;")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_10)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.frame_7 = QtWidgets.QFrame(self.main_body)
        self.frame_7.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_9.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_13.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_9.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_14.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_9.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_15.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_9.addWidget(self.pushButton_15)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.bar_graph_frame = QtWidgets.QFrame(self.main_body)
        self.bar_graph_frame.setMinimumSize(QtCore.QSize(0, 400))
        self.bar_graph_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bar_graph_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bar_graph_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bar_graph_frame.setObjectName("bar_graph_frame")
        
        self.bar_graph_layout = QVBoxLayout(self.bar_graph_frame)
        self.bar_graph_frame.setLayout(self.bar_graph_layout)
        self.conn = sqlite3.connect('app_screen_time.db')
        self.create_table()
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.update_data_and_plot)
        self.timer.start(1000)  # Update every second

    
        
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.bar_graph_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6.addWidget(self.bar_graph_frame)
        self.frame_6 = QtWidgets.QFrame(self.main_body)
        self.frame_6.setStyleSheet("background-color: transparent;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_6.setMinimumHeight(420)
        self.frame_6.setMaximumWidth(720)
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_6)
        self.calendarWidget.setStyleSheet("color: rgb(85, 255, 255);\n"
        "font-weight:700;\n"
        "font-family: \'Istok Web\';"
        "alternate-background-color: black;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_4.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.main_body)
        self.main_body.raise_()
        self.side_menu.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menu_expanded = False

        # Connect the button click event to the toggle_menu function
        self.pushButton.clicked.connect(self.toggle_menu)

        # Set up the animation for the side menu
        self.side_menu_animation = QtCore.QPropertyAnimation(self.side_menu, b"maximumWidth")
        self.side_menu_animation.setDuration(300)

        # Set up the central widget animation for overlay effect
        self.central_widget_animation = QtCore.QPropertyAnimation(self.centralwidget, b"geometry")
        self.central_widget_animation.setDuration(300)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton_2.clicked.connect(self.FirstButtonClicked)
        self.pushButton_3.clicked.connect(self.SecondButtonClicked)
        self.pushButton_4.clicked.connect(self.ThirdButtonClicked)
        self.pushButton_5.clicked.connect(self.FourthButtonClicked)
        # self.pushButton_6.clicked.connect(self.FifthButtonClicked)
        
    def toggle_menu(self):
        # Toggle the menu state
        self.menu_expanded = not self.menu_expanded

        # Define the target width for the side menu
        target_width = 200 if self.menu_expanded else 0

        # Update the side menu animation
        self.side_menu_animation.setEndValue(target_width)
        self.side_menu_animation.start()

        # Update the central widget animation for overlay effect
        if self.menu_expanded:
            self.central_widget_animation.setEndValue(QtCore.QRect(200, 0, 586, 370))
        else:
            self.central_widget_animation.setEndValue(QtCore.QRect(0, 0, 586, 370))
        self.central_widget_animation.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "Samadhan App"))
        self.pushButton_2.setText(_translate("MainWindow", "Notes"))
        self.pushButton_3.setText(_translate("MainWindow", "Calendar"))
        self.pushButton_4.setText(_translate("MainWindow", "Quiz"))
        self.pushButton_5.setText(_translate("MainWindow", "Item 4"))
        self.pushButton_6.setText(_translate("MainWindow", "Item 5"))
        self.Welcome.setText(_translate("MainWindow", "Welcome"))
        self.Welcome_2.setText(_translate("MainWindow", "Username"))
        self.label_4.setText(_translate("MainWindow", "Academic Supervison"))
        self.label_5.setText(_translate("MainWindow", "Academic Anaysis"))
        self.label_7.setText(_translate("MainWindow", "     Time Effecient"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS screen_time (
                            app_name TEXT PRIMARY KEY,
                            total_screen_time REAL
                        )''')
        self.conn.commit()

    def track_and_store_screen_time(self):
        active_window = gw.getActiveWindow()
        if active_window is not None:
            app_name = active_window.title

            if app_name != 'Main Window':  # Exclude details about the PyQt window
                if "Google Chrome" in app_name or "Firefox" in app_name or "Edge" in app_name:
                    tab_name = self.get_browser_tab_name(active_window)
                elif "Visual" in app_name:
                        tab_name="Visual Studio"        
                else:
                    tab_name = app_name

                cursor = self.conn.cursor()
                cursor.execute("SELECT total_screen_time FROM screen_time WHERE app_name=?", (tab_name,))
                row = cursor.fetchone()

                if row:
                    total_time = row[0] + 1  # Update every second
                    cursor.execute("UPDATE screen_time SET total_screen_time=? WHERE app_name=?", (total_time, tab_name))
                else:
                    cursor.execute("INSERT INTO screen_time (app_name, total_screen_time) VALUES (?, ?)", (tab_name, 1))

                self.conn.commit()

    def get_browser_tab_name(self, window):
        title = window.title
        if " - Google Chrome" in title:
            tab_name = title.split(" - Google Chrome")[0]
            if "- YouTube" in tab_name:
                tab_name = "YouTube" 
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram" 
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"    
            return tab_name
        elif " - Mozilla Firefox" in title:
            tab_name = title.split(" - Mozilla Firefox")[0]
            if "- YouTube" in tab_name:
                tab_name = "YouTube" 
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram" 
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"      
            return tab_name
        elif " - Microsoft Edge" in title:
            tab_name = title.split(" - Microsoft Edge")[0]
            if "- YouTube" in tab_name:
                tab_name = "YouTube" 
            elif "Chats" in tab_name or "Instagram" in tab_name:
                tab_name = "Instagram" 
            elif "Messenger" in tab_name or "Facebook" in tab_name:
                tab_name = "Facebook"       
            return tab_name
        elif "- Visual Studio Code" in title:
                title="Visual Studio Code"
                return title
        else:
            return title    

    def format_time(self, seconds):
        if seconds >= 3600:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{hours}h {minutes}m"
        elif seconds >= 60:
            minutes = seconds // 60
            return f"{minutes}m"
        else:
            return f"{seconds}s"

    def update_data_and_plot(self):
        self.track_and_store_screen_time()
        self.plot_graph()

    def plot_graph(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM screen_time WHERE app_name != 'Application Monitor' ORDER BY total_screen_time DESC LIMIT 5")
        data = cursor.fetchall()

        apps = [row[0] for row in data]
        times = [row[1] for row in data]

        formatted_times = [self.format_time(time) for time in times]

        fig, ax = plt.subplots(figsize=(8, 5))  # Larger figure size
        bars = ax.bar(apps, times, color='skyblue')
        ax.set_xlabel('Tabs/Applications', fontsize=10)
        ax.set_ylabel('Total Screen Time', fontsize=10)  # Adjusted font size for y-label
        ax.set_title('Top Tabs/Applications by Total Screen Time', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=10)  # Adjusted font size for x-ticks
        plt.yticks(fontsize=10)  # Adjusted font size for y-ticks

        # Annotate bars with total time spent
        for bar, time in zip(bars, formatted_times):
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{time}', ha='center', va='bottom', fontsize=12)

        plt.tight_layout()
        
        # Clear the previous layout
        for i in reversed(range(self.bar_graph_layout.count())):
                self.bar_graph_layout.itemAt(i).widget().setParent(None)

        # Embed the Matplotlib figure into the PyQt5 application
        canvas = FigureCanvas(fig)
        self.bar_graph_layout.addWidget(canvas)
        canvas.draw()
    
    def FirstButtonClicked(self):
        notes = NoteTable()
        widget.addWidget(notes)
        widget.setCurrentIndex(widget.currentIndex() + 1)
         
    def SecondButtonClicked(self):
        calendar = Calendar()
        widget.addWidget(calendar)
        widget.setCurrentIndex(widget.currentIndex() + 1) 
        
    def ThirdButtonClicked(self):
        quiz = Quiz()
        widget.addWidget(quiz)
        widget.setCurrentIndex(widget.currentIndex() + 1) 
    
    def FourthButtonClicked(self):
        quiz = Subject()
        widget.addWidget(quiz)
        widget.setCurrentIndex(widget.currentIndex() + 1) 
    
class NoteTable(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):  
        loadUi("myapp/Resources/table.ui", self)
        self.menu = self.findChild(QWidget, "side_menu")
        self.physics_upld = self.findChild(QPushButton, "upload_physics")
        self.chemistry_upld = self.findChild(QPushButton, "upload_chemistry")
        self.maths_upld = self.findChild(QPushButton, "upload_maths")
        self.java_upld = self.findChild(QPushButton, "upload_java")
        self.python_upld = self.findChild(QPushButton, "upload_python")
        
        self.physics_view = self.findChild(QPushButton, "view_physics")
        self.chemistry_view = self.findChild(QPushButton, "view_physics")
        self.maths_view = self.findChild(QPushButton, "view_maths")
        self.java_view = self.findChild(QPushButton, "view_java")
        self.python_view = self.findChild(QPushButton, "view_python")
        
        self.physics_upld.clicked.connect(lambda: self.uploadNote("physics"))
        self.chemistry_upld.clicked.connect(lambda: self.uploadNote("chemistry")) 
        self.maths_upld.clicked.connect(lambda: self.uploadNote("maths"))
        self.java_upld.clicked.connect(lambda: self.uploadNote("java"))
        self.python_upld.clicked.connect(lambda: self.uploadNote("python"))
        
        self.physics_view.clicked.connect(lambda: self.viewNote("physics"))
        self.chemistry_view.clicked.connect(lambda: self.viewNote("chemistry")) 
        self.maths_view.clicked.connect(lambda: self.viewNote("maths"))
        self.java_view.clicked.connect(lambda: self.viewNote("java"))
        self.python_view.clicked.connect(lambda: self.viewNote("python"))
        
        self.pushButton_2 = self.findChild(QPushButton, "pushButton_2")
        self.pushButton_3 = self.findChild(QPushButton, "pushButton_3")
        self.pushButton_4 = self.findChild(QPushButton, "pushButton_4")
        self.pushButton_2.clicked.connect(LandingPage.FirstButtonClicked)
        self.pushButton_3.clicked.connect(LandingPage.SecondButtonClicked)
        self.pushButton_4.clicked.connect(LandingPage.ThirdButtonClicked)
        
    def uploadNote(self, subject):
        view_upld = ViewUpload()
        widget.addWidget(view_upld)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def viewNote(self,subject):
        view_upld = ViewNoteTable()
        widget.addWidget(view_upld)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
class ViewUpload(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loadUi("myapp/Resources/upload_view_page.ui", self)
        self.chapter_num = self.findChild(QLineEdit, "Chapter_form")
        self.select_bttn = self.findChild(QPushButton, "select_button")
        self.chapter_title = self.findChild(QLineEdit, "title_form")
        self.chapter_description = self.findChild(QTextEdit, "Description_form")
        self.upload_bttn = self.findChild(QPushButton, "upload_button")

        self.upload_bttn.clicked.connect(self.uploadClicked)
        self.select_bttn.clicked.connect(self.selectFiles)

        # Construct the path to the SQLite database file
        script_directory = os.path.dirname(os.path.abspath(__file__))
        database_directory = os.path.join(script_directory, '..', '..')  # Go two levels up
        database_path = os.path.join(database_directory, 'studentapp.db')

        # Connect to the SQLite database
        self.connection = sqlite3.connect(database_path)
        self.cursor = self.connection.cursor()
        
        self.pushButton_2 = self.findChild(QPushButton, "pushButton_2")
        self.pushButton_3 = self.findChild(QPushButton, "pushButton_3")
        self.pushButton_4 = self.findChild(QPushButton, "pushButton_4")
        self.pushButton_5 = self.findChild(QPushButton, "pushButton_5")
        
        self.pushButton_2.clicked.connect(LandingPage.FirstButtonClicked)
        self.pushButton_3.clicked.connect(LandingPage.SecondButtonClicked)
        self.pushButton_4.clicked.connect(LandingPage.ThirdButtonClicked)
        self.pushButton_5.clicked.connect(LandingPage.FourthButtonClicked)

    def selectFiles(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 'Documents', '*.png *.jpg *.pdf')
        self.select_bttn.setText(fname)
        self.selected_file_path = fname


    def uploadClicked(self):
        title = self.chapter_title.text()
        chapter_num = self.chapter_num.text()
        description = self.chapter_description.toPlainText()

        if title and chapter_num and description:
            
            # Insert user-entered information and file path into the database
            self.cursor.execute("INSERT INTO notes (FileName, FilePath, Description, chapternum) VALUES (?, ?, ?, ?)",
                                (title,  self.selected_file_path,  description, chapter_num))
            self.connection.commit()

            # Move the selected file to a specified directory
            if hasattr(self, 'selected_file_path') and os.path.exists(self.selected_file_path):
                destination_directory = 'C:\pyqt5\myapp\storage'
                shutil.copy(self.selected_file_path, destination_directory)

                QMessageBox.information(self, 'Success', 'Upload successful!')

        else:
            QMessageBox.warning(self, 'Fields Empty', 'Please fill all fields')
                    
class ViewNoteTable(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.populate_data()
        self.tableWidget.itemClicked.connect(self.download_file)

    def load_ui(self):
        loadUi("myapp/Resources/view_notes_table.ui", self)
        self.pushButton_2 = self.findChild(QPushButton, "pushButton_2")
        self.pushButton_3 = self.findChild(QPushButton, "pushButton_3")
        self.pushButton_4 = self.findChild(QPushButton, "pushButton_4")
        self.pushButton_2.clicked.connect(LandingPage.FirstButtonClicked)
        self.pushButton_3.clicked.connect(LandingPage.SecondButtonClicked)
        self.pushButton_4.clicked.connect(LandingPage.ThirdButtonClicked)
    
    def populate_data(self):
        # Connect to the SQLite database
        connection = sqlite3.connect("studentapp.db")
        cursor = connection.cursor()

        # Fetch data from the 'notes' table
        cursor.execute("SELECT FileName, chapternum, Description, FilePath FROM notes")
        data = cursor.fetchall()

        # Close the database connection
        connection.close()

        # Populate the data into the table widget
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 350)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setColumnWidth(3, 0)
        
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)

    def download_file(self, item):
        # Assuming FilePath is in the fourth column (index 3)
        full_file_path = self.tableWidget.item(item.row(), 3).text()
        # Extract only the filename from the path
        file_name = os.path.basename(full_file_path)

        # Specify the path to the "storage" folder
        storage_folder = "C:\pyqt5\myapp\storage"  # Replace with the actual path to your "storage" folder

        # Construct the full file path in the storage folder
        file_path_in_storage = os.path.join(storage_folder, file_name)
        print(full_file_path,file_name, file_path_in_storage)

        # Check if the file exists
        if os.path.exists(file_path_in_storage):
            # Open a file dialog to choose the download location
            save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*)")

            # Check if the user canceled the file dialog
            if save_path:
                try:
                    # Copy the file to the chosen location
                    shutil.copy(file_path_in_storage, save_path)
                    QtWidgets.QMessageBox.information(self, "Download Complete", "File downloaded successfully.")
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self, "Error", f"Error downloading file: {str(e)}")
        else:
            QtWidgets.QMessageBox.warning(self, "File Not Found", "The selected file does not exist.")
           
class Calendar(LandingPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 401)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"  border: none;\n"
"  background-color: transparent;\n"
"  color: #FFF; /* Specify a default color */\n"
"}\n"
"\n"
"#centralwidget {\n"
"  background-color: white\n"
";\n"
"}\n"
"\n"
"#side_menu {\n"
"  background-color: #071e26;\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  padding: 10px;\n"
"  background-color: #071e26;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"#main_body {\n"
"  background-color: #071e26;\n"
"  border-radius: 10px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons_folder/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.frame_2)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.side_menu)
        self.frame_4.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons_folder/airplay.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons_folder/award.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons_folder/bar-chart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons_folder/cloud-drizzle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons_folder/crosshair.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.gridLayout = QtWidgets.QGridLayout(self.main_body)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(self.main_body)
        self.frame_6.setStyleSheet("background-color:transprent;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_6)
        self.calendarWidget.setStyleSheet("color: rgb(85, 255, 255);\n"
"font-size:20px;\n"
"font-weight:700;\n"
"font-family: \'Istok Web\';\n"
"alternate-background-color: rgb(0, 0, 0);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_6.addWidget(self.calendarWidget)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.main_body)
        self.frame_5.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.addButton = QtWidgets.QPushButton(self.frame_5)
        self.addButton.setMinimumSize(QtCore.QSize(10, 0))
        self.addButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.addButton.setBaseSize(QtCore.QSize(0, 0))
        self.addButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size:12 px;\n"
"color:#071e26;\n"
"border-radius:5px\n"
"\n"
"\n"
"")
        self.addButton.setAutoDefault(False)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_5.addWidget(self.addButton)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"font-family: \'Istok Web\';\n"
"border-radius:5px;\n"
"letter-spacing:1px;\n"
"font-size:6px;\n"
"padding-left:4px")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.tasksListWidget = QtWidgets.QListWidget(self.frame_5)
        self.tasksListWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black;")
        self.tasksListWidget.setObjectName("tasksListWidget")
        item = QtWidgets.QListWidgetItem()
        self.tasksListWidget.addItem(item)
        self.verticalLayout_5.addWidget(self.tasksListWidget)
        self.saveButton = QtWidgets.QPushButton(self.frame_5)
        self.taskLineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.verticalLayout_5.addWidget(self.taskLineEdit)
        self.saveButton.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"font-family: \'Istok Web\';\n"
"font-style: normal;\n"
"font-weight: 700;\n"
"font-size:12 px;\n"
"color:#071e26;\n"
"\n"
"\n"
"\n"
"")
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_5.addWidget(self.saveButton)
        self.gridLayout.addWidget(self.frame_5, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.main_body)
        self.main_body.raise_()
        self.side_menu.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.menu_expanded = False

        # Connect the button click event to the toggle_menu function
        self.pushButton.clicked.connect(self.toggle_menu)

        # Set up the animation for the side menu
        self.side_menu_animation = QtCore.QPropertyAnimation(self.side_menu, b"maximumWidth")
        self.side_menu_animation.setDuration(300)

        # Set up the central widget animation for overlay effect
        self.central_widget_animation = QtCore.QPropertyAnimation(self.centralwidget, b"geometry")
        self.central_widget_animation.setDuration(300)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.conn = sqlite3.connect('studentapp.db')
        self.cursor = self.conn.cursor()
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        
        self.pushButton_2.clicked.connect(LandingPage.FirstButtonClicked)
        self.pushButton_3.clicked.connect(LandingPage.SecondButtonClicked)
        self.pushButton_4.clicked.connect(LandingPage.ThirdButtonClicked)
        self.pushButton_5.clicked.connect(LandingPage.FourthButtonClicked)
        
    def calendarDateChanged(self):
            print("The calendar date was changed.")
            dateSelected = self.calendarWidget.selectedDate().toPyDate()
            print("Date selected:", dateSelected)
            self.updateTaskList(dateSelected)

    def updateTaskList(self, date):
        self.tasksListWidget.clear()

        query = "SELECT task, completed FROM tasks WHERE date = ?"
        row = (date,)
        results = self.cursor.execute(query, row).fetchall()
        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            if result[1] == "YES":
                item.setCheckState(Qt.Checked)
            elif result[1] == "NO":
                item.setCheckState(Qt.Unchecked)
            self.tasksListWidget.addItem(item)

    def saveChanges(self):
        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.tasksListWidget.count()):
            item = self.tasksListWidget.item(i)
            task = item.text()
            if item.checkState() == Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)
            self.cursor.execute(query, row)
        self.conn.commit()

        messageBox = QMessageBox()
        messageBox.setText("Changes saved.")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

    def addNewTask(self):
        newTask = str(self.lineEdit.text())  # Use self.lineEdit.text() instead of self.taskLineEdit.text()
        date = self.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?,?,?)"
        row = (newTask, "NO", date,)

        try:
            self.cursor.execute(query, row)
            self.conn.commit()
            self.updateTaskList(date)
            self.lineEdit.clear()  # Clear the lineEdit widget
        except Exception as e:
            print(f"An error occurred: {e}")


    def closeEvent(self, event):
        self.conn.close()
        event.accept()
    def toggle_menu(self):
        # Toggle the menu state
        self.menu_expanded = not self.menu_expanded

        # Define the target width for the side menu
        target_width = 200 if self.menu_expanded else 0

        # Update the side menu animation
        self.side_menu_animation.setEndValue(target_width)
        self.side_menu_animation.start()

        # Update the central widget animation for overlay effect
        if self.menu_expanded:
            self.central_widget_animation.setEndValue(QtCore.QRect(200, 0, 586, 370))
        else:
            self.central_widget_animation.setEndValue(QtCore.QRect(0, 0, 586, 370))
        self.central_widget_animation.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "Samadhan App"))
        self.pushButton_2.setText(_translate("MainWindow", "Notes"))
        self.pushButton_3.setText(_translate("MainWindow", "Calendar"))
        self.pushButton_4.setText(_translate("MainWindow", "Quiz"))
        self.pushButton_5.setText(_translate("MainWindow", "Item 4"))
        self.pushButton_6.setText(_translate("MainWindow", "Item 5"))
        self.pushButton_17.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_18.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "Academic Supervison"))
        self.label_5.setText(_translate("MainWindow", "Academic Anaysis"))
        self.label_7.setText(_translate("MainWindow", "     Time Effecient"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_7.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_8.setText(_translate("MainWindow", "PushButton"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "My app"))
        self.pushButton_2.setText(_translate("MainWindow", "Notes"))
        self.pushButton_3.setText(_translate("MainWindow", "Calendar"))
        self.pushButton_4.setText(_translate("MainWindow", "Quiz"))
        self.pushButton_5.setText(_translate("MainWindow", "Item 4"))
        self.pushButton_6.setText(_translate("MainWindow", "Item 5"))
        self.addButton.setText(_translate("MainWindow", "Add New"))
        __sortingEnabled = self.tasksListWidget.isSortingEnabled()
        self.tasksListWidget.setSortingEnabled(False)
        item = self.tasksListWidget.item(0)
        item.setText(_translate("MainWindow", "hello"))
        self.tasksListWidget.setSortingEnabled(__sortingEnabled)
        self.saveButton.setText(_translate("MainWindow", "Save Changes"))

class Subject(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loadUi("myapp/Resources/subject.ui", self)
        
        self.physics_bttn = self.findChild(QFrame, 'phys_frame')
        self.chemistry_bttn = self.findChild(QFrame, 'Chem_frame')
        self.maths_bttn = self.findChild(QFrame, 'maths_frame')
        self.coding_bttn = self.findChild(QFrame, 'coding_frame')
        
        self.pushButton_2 = self.findChild(QPushButton, "pushButton_2")
        self.pushButton_3 = self.findChild(QPushButton, "pushButton_3")
        self.pushButton_4 = self.findChild(QPushButton, "pushButton_4")
        self.pushButton_5 = self.findChild(QPushButton, "pushButton_5")

        self.pushButton_2.clicked.connect(LandingPage.FirstButtonClicked)
        self.pushButton_3.clicked.connect(LandingPage.SecondButtonClicked)
        self.pushButton_4.clicked.connect(LandingPage.ThirdButtonClicked)
        self.pushButton_5.clicked.connect(LandingPage.FourthButtonClicked)
        
        # Use the ClickableFrame class for each button
        self.physics_bttn.mousePressEvent = self.onFrameClicked('')
        self.chemistry_bttn.mousePressEvent = self.onFrameClicked('')
        self.maths_bttn.mousePressEvent = self.onFrameClicked('')
        self.coding_bttn.mousePressEvent = self.onFrameClicked('')
               
    def onFrameClicked(self , n):
        print("Physics Quiz clicked")
        ques = Quiz()
        widget.addWidget(ques)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
class QuizWrapper(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 375)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"  border: none;\n"
"  background-color: transparent;\n"
"  color: #FFF; /* Specify a default color */\n"
"}\n"
"\n"
"#centralwidget {\n"
"  background-color: white\n"
";\n"
"}\n"
"\n"
"#side_menu {\n"
"  background-color: #071e26;\n"
"  border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton {\n"
"  padding: 10px;\n"
"  background-color: #071e26;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"#main_body {\n"
"  background-color: #071e26;\n"
"  border-radius: 10px;\n"
"}\n"
"")     
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMinimumSize(QtCore.QSize(0, 50))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons_folder/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(24, 24))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu = QtWidgets.QWidget(self.frame_2)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.side_menu)
        self.frame_4.setMinimumSize(QtCore.QSize(150, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/New folder/airplay.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/New folder/award.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/New folder/coffee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/New folder/music.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_4)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/New folder/wifi.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout_2.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.side_menu)
        self.main_body = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.timer_label = QtWidgets.QLabel(self.main_body)
        self.timer_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.timer_label.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:600;\n"
"font-size:28px;")
        self.timer_label.setObjectName("timer_label")
        self.verticalLayout_6.addWidget(self.timer_label)
        self.question_label = QtWidgets.QLabel(self.main_body)
        self.question_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.question_label.setStyleSheet(" font-family: \'Istok Web\';\n"
"\n"
"font-weight:600;\n"
"font-size:34px;")
        self.question_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_label.setObjectName("question_label")
        self.verticalLayout_6.addWidget(self.question_label)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.option_1 = QtWidgets.QRadioButton(self.main_body)
        self.option_1.setMinimumSize(QtCore.QSize(0, 80))
        self.option_1.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:500;\n"
"font-size:26px;\n"
"margin-left:20px;")
        self.option_1.setObjectName("option_1")
        self.verticalLayout_5.addWidget(self.option_1)
        self.option_2 = QtWidgets.QRadioButton(self.main_body)
        self.option_2.setMinimumSize(QtCore.QSize(0, 80))
        self.option_2.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:500;\n"
"font-size:26px;\n"
"margin-left:20px;")
        self.option_2.setObjectName("option_2")
        self.verticalLayout_5.addWidget(self.option_2)
        self.option_3 = QtWidgets.QRadioButton(self.main_body)
        self.option_3.setMinimumSize(QtCore.QSize(0, 80))
        self.option_3.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:500;\n"
"font-size:26px;\n"
"margin-left:20px;")
        self.option_3.setObjectName("option_3")
        self.verticalLayout_5.addWidget(self.option_3)
        self.option_4 = QtWidgets.QRadioButton(self.main_body)
        self.option_4.setMinimumSize(QtCore.QSize(0, 80))
        self.option_4.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:500;\n"
"font-size:26px;\n"
"margin-left:20px;")
        self.option_4.setObjectName("option_4")
        self.verticalLayout_5.addWidget(self.option_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.next_button = QtWidgets.QPushButton(self.main_body)
        self.next_button.setMinimumSize(QtCore.QSize(0, 80))
        self.next_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_button.setMouseTracking(False)
        self.next_button.setStyleSheet(" font-family: \'Istok Web\';\n"
"font-weight:600;\n"
"font-size:18px;\n"
"background-color: rgb(27, 239, 52);\n"
"border-radius:7px;")
        
        self.timer = QTimer(MainWindow)
        self.timer.timeout.connect(self.timer_timeout)
        self.time_left = 15  # Initial time (seconds)
        self.timer.start(1000) 
        self.next_button.setObjectName("next_button")
        self.verticalLayout_6.addWidget(self.next_button)
        self.horizontalLayout.addWidget(self.main_body)
        self.main_body.raise_()
        self.side_menu.raise_()
        self.verticalLayout.addWidget(self.frame_2)
        # MainWindow.setCentralWidget(self.centralwidget)
        self.next_button.clicked.connect(self.next_question)
        self.questions = [
            [
                "Which planet is known as the \"Red Planet\"?", "a) Venus", "b) Mars", "c) Jupiter", "d) Saturn", "b"
            ],
            [
                "Who painted the famous artwork \"The Mona Lisa\"?", "a) Pablo Picasso", "b) Leonardo da Vinci",
                "c) Vincent van Gogh", "d) Claude Monet", "b"
            ],
            [
                "What is the chemical symbol for gold?", "a) Go", "b) Gd", "c) Au", "d) Ag", "c"
            ],
            [
                "What is the 2nd tallest mountain in the world?", "a) Mount Everest", "b) K2",
                "c) Mount Kilimanjaro", "d) Mount McKinley", "b"
            ],
            [
                "What is the chemical symbol for Scandium?", "a) Sn", "b) Scan", "c) Sd", "d) Sc", "d"
            ],
            [
                "What is the capital of France?", "a) London", "b) Paris", "c) Berlin", "d) Rome", "b"
            ],  
                [
                "Who wrote \"Romeo and Juliet\"?", "a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen", "d) Mark Twain", "b"
            ],
            [
                "What is the largest mammal in the world?", "a) Elephant", "b) Giraffe", "c) Blue Whale", "d) Lion", "c"
            ],
            [
                "In which year did Christopher Columbus discover America?", "a) 1492", "b) 1588", "c) 1776", "d) 1620", "a"
            ],
            [
                "What is the chemical symbol for water?", "a) W", "b) O", "c) H2O", "d) Wa", "c"
            ],
            [
                "Who is known as the \"Father of Computers\"?", "a) Bill Gates", "b) Alan Turing", "c) Steve Jobs", "d) Charles Babbage", "d"
            ],
            [
                "What is the currency of Japan?", "a) Won", "b) Ringgit", "c) Yen", "d) Baht", "c"
            ],
            [
                "What is the square root of 64?", "a) 6", "b) 7", "c) 8", "d) 9", "c"
            ],
            [
                "Who painted the Mona Lisa?", "a) Vincent van Gogh", "b) Pablo Picasso", "c) Leonardo da Vinci", "d) Claude Monet", "c"
            ]
]

        self.selected_questions = sample(self.questions, 7)
        self.current_question = 0
        self.user_answers = []

        self.show_question()        
        self.pushButton_2.clicked.connect(LandingPage.FirstButtonClicked)
        self.pushButton_3.clicked.connect(LandingPage.SecondButtonClicked)
        self.pushButton_4.clicked.connect(LandingPage.ThirdButtonClicked)
        self.pushButton_5.clicked.connect(LandingPage.FourthButtonClicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def show_question(self):
        if self.current_question < len(self.selected_questions):
            question_data = self.selected_questions[self.current_question]
            self.question_label.setText(question_data[0])

            options = question_data[1:5]
            

            for i in range(4):
                getattr(self, f"option_{i+1}").setText(options[i])

            self.timer_label.setText(f'Time remaining: {self.time_left} seconds')

            self.timer.start()

        else:
            self.evaluate_answers()
    
    def next_question(self):
        self.timer.stop()
        selected_option = None

        for i in range(4):
            if getattr(self, f"option_{i+1}").isChecked():
                selected_option = chr(ord('a') + i)

        if selected_option is not None:
            self.user_answers.append(selected_option)
        else:
            self.user_answers.append('')  # Mark unanswered question

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.time_left = 15  # Reset timer for each new question
            self.show_question()
            self.timer.start()
        else:
            self.evaluate_answers()
        
    def evaluate_answers(self):
        correct_answers = sum(user_ans == question[-1] for user_ans, question in zip(self.user_answers, self.selected_questions))
        total_questions = len(self.selected_questions)

        QMessageBox.information(MainWindow, 'Results', f'You answered {correct_answers} out of {total_questions} questions correctly.')
        MainWindow.close()  
            
    def timer_timeout(self):
        self.time_left -= 1
        self.timer_label.setText(f'Time remaining: {self.time_left} seconds')

        if self.time_left == 0:
            self.timer.stop()
            current_question_index = self.current_question
            self.user_answers.append('')  # Mark unanswered question
            QMessageBox.warning(MainWindow, "Time's Up!", 'You did not respond in time. Moving to the next question.')

            # Mark the previous unanswered question as incorrect
            if current_question_index < len(self.questions):
                self.user_answers[current_question_index] = 'incorrect'

            self.current_question += 1
            if self.current_question < len(self.questions):
                self.time_left = 15  # Reset timer for each new question
                self.show_question()
                self.timer.start()
            else:
                self.evaluate_answers()
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "My app"))
        self.pushButton_2.setText(_translate("MainWindow", "Notes"))
        self.pushButton_3.setText(_translate("MainWindow", "Calendar"))
        self.pushButton_4.setText(_translate("MainWindow", "Quiz"))
        self.pushButton_5.setText(_translate("MainWindow", "Item 4"))
        self.pushButton_6.setText(_translate("MainWindow", "Item 5"))
        self.timer_label.setText(_translate("MainWindow", "Timer Count down here"))
        self.next_button.setText(_translate("MainWindow", "Next"))

class Quiz(QuizWrapper):
    def __init__(self, parent=None):
        super().__init__(parent)
                   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    MainWindow = Ui_MainWindow()
    widget.addWidget(MainWindow)

    # Set the size of the QStackedWidget to match the default size of the UI
    widget.setFixedWidth(MainWindow.width())
    widget.setFixedHeight(MainWindow.height())

    widget.show()
    sys.exit(app.exec_())
