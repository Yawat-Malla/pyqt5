from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pygetwindow as gw
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import sqlite3
class Ui_MainWindow(object):
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
        self.pushButton_2.setText(_translate("MainWindow", "Item 1"))
        self.pushButton_3.setText(_translate("MainWindow", "Item 2"))
        self.pushButton_4.setText(_translate("MainWindow", "Item 3"))
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())