# main.py
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from myapp.login.login_window import Ui_MainWindow

class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Connect buttons to methods
        self.Login.clicked.connect(self.login_clicked)
        self.signup.clicked.connect(self.signup_clicked)
        self.Login_button.clicked.connect(self.login_button_clicked)
        # Initialize SignupWindow but don't show it initially
        

    

if __name__ == "__main__":
    app = QApplication([])
    main_application = MainApplication()
    main_application.show()
    ui = Ui_MainWindow()
    ui.setupUi(main_application)
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(main_application)
    main_application.show()
    
    