import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit, QTextEdit, QFileDialog, QMessageBox
from PyQt5.uic import loadUi
import sqlite3
import shutil

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = ViewUpload()
    MainWindow.show()
    sys.exit(app.exec_())
