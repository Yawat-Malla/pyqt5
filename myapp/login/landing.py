from PyQt5 import QtWidgets ,QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QMessageBox, QStackedWidget, QMainWindow
from PyQt5.uic import loadUi
import os
import sys
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from myapp.landingpage.view_notes_table import ViewUpload

class LandingPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        MainWindow = QtWidgets.QMainWindow()
        self.load_ui(MainWindow)
        
    def load_ui(self, MainWindow):
        loadUi("myapp/Resources/landing.ui", self)
        self.menu_button = self.findChild(QPushButton, "pushButton")
        self.side_menu = self.findChild(QPushButton, "side_menu")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.firstoption = self.findChild(QPushButton,'pushButton_2')
        self.secondoption = self.findChild(QPushButton,'pushButton_3')
        self.thirdoption = self.findChild(QPushButton,'pushButton_4')
        self.fourthoption = self.findChild(QPushButton,'pushButton_5')

        self.firstoption.clicked.connect(self.FirstButtonClicked)
        # Connect the signal after loading the UI
        # self.signup_button.clicked.connect(self.on_signup)
        # self.logintab_button.clicked.connect(self.login_clicked)
        
        # Connect the button click event to the toggle_menu function
        self.menu_button.clicked.connect(self.toggle_menu)

        # Set up the animation for the side menu
        self.side_menu_animation = QtCore.QPropertyAnimation(self.side_menu, b"maximumWidth")
        self.side_menu_animation.setDuration(300)

        # Set up the central widget animation for overlay effect
        self.central_widget_animation = QtCore.QPropertyAnimation(self.centralwidget, b"geometry")
        self.central_widget_animation.setDuration(300)

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

    def FirstButtonClicked(self):
        notes = ViewUpload()
        widget.addWidget(notes)
        widget.setCurrentIndex(widget.currentIndex() + 1)   
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    MainWindow = LandingPage()
    widget.addWidget(MainWindow)

    # Set the size of the QStackedWidget to match the default size of the UI
    widget.setFixedWidth(MainWindow.width())
    widget.setFixedHeight(MainWindow.height())

    widget.show()
    sys.exit(app.exec_())