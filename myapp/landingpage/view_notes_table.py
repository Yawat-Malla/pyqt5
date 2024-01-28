import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.uic import loadUi
import sqlite3
import shutil
import os
import sys
import icons_rc
import welbeings_rc
import pygetwindow as gw
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import sqlite3
class ViewNoteTable(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.populate_data()
        self.tableWidget.itemClicked.connect(self.download_file)

    def load_ui(self):
        loadUi("myapp/Resources/view_notes_table.ui", self)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = ViewNotes()
    MainWindow.show()
    sys.exit(app.exec_())
