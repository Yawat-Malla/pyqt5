import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class SignUpPage(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create widgets for signup page
        self.signup_label = QLabel('Sign Up')
        self.username_label = QLabel('Username:')
        self.username_entry = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.signup_button = QPushButton('Sign Up')
        self.signup_button.clicked.connect(self.signup)

        # Set layout for signup page
        layout = QVBoxLayout()
        layout.addWidget(self.signup_label)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('Sign Up Page')

    def signup(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        # You can implement your signup logic here
        # For simplicity, let's just print the credentials
        print(f'New User: {username}, Password: {password}')
        self.close()