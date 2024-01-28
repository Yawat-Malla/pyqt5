import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QTextEdit, QFileDialog, QMessageBox, QFrame, QLabel
from PyQt5.uic import loadUi
import sqlite3
import shutil

class ViewDetails(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()

    def load_ui(self):
        loadUi("myapp/Resources/view_notes_details.ui", self)
        
        
    # def titleClicked(self):
    
    
    # def downloadClicked(self):
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = ViewDetails()
    MainWindow.show()
    sys.exit(app.exec_())
