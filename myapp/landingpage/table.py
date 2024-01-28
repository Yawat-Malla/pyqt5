import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton, QLineEdit, QMessageBox, QStackedWidget, QMainWindow
from PyQt5.uic import loadUi
from myapp.landingpage.upload_notes import ViewUpload

class UploadMain(QMainWindow):
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
        
        # connecting buttons using lambda functions
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
        
    def uploadNote(self, subject):
        view_upld = ViewUpload()
        widget.addWidget(view_upld)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def viewNote(self,subject):
        view_upld = ViewUpload()
        widget.addWidget(view_upld)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    MainWindow = UploadMain()
    widget.addWidget(MainWindow)
    widget.setFixedWidth(MainWindow.width())
    widget.setFixedHeight(MainWindow.height())
    widget.show()
    sys.exit(app.exec_())