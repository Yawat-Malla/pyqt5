from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSignal
import sys

class ClickableFrame(QFrame):
    clicked = pyqtSignal()  # Custom signal

    def __init__(self, parent=None):
        super(ClickableFrame, self).__init__(parent)

    def mousePressEvent(self, event):
        # This method is called when the mouse button is pressed over the frame
        print(f"Frame {self.objectName()} Clicked!")
        self.clicked.emit()  # Emit the custom signal

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
        
        # Use the ClickableFrame class for each button
        self.physics_bttn = ClickableFrame(self.physics_bttn)
        self.chemistry_bttn = ClickableFrame(self.chemistry_bttn)
        self.maths_bttn = ClickableFrame(self.maths_bttn)
        self.coding_bttn = ClickableFrame(self.coding_bttn)

        # Connect the custom clicked signal of each button to the corresponding method
        self.physics_bttn.clicked.connect(self.PhysQuiz)
        self.chemistry_bttn.clicked.connect(self.ChemQuiz)
        self.maths_bttn.clicked.connect(self.MathsQuiz)
        self.coding_bttn.clicked.connect(self.CodingQuiz)

    def PhysQuiz(self):
        print("Physics Quiz clicked")
        # Perform actions related to Physics Quiz

    def ChemQuiz(self):
        print("Chemistry Quiz clicked")
        # Perform actions related to Chemistry Quiz

    def MathsQuiz(self):
        print("Maths Quiz clicked")
        # Perform actions related to Maths Quiz

    def CodingQuiz(self):
        print("Coding Quiz clicked")
        # Perform actions related to Coding Quiz

if __name__ == "__main__":
    app = QApplication([])
    widget = QStackedWidget()
    MainWindow = Subject()
    widget.addWidget(MainWindow)

    # Set the size of the QStackedWidget to match the default size of the UI
    widget.setFixedWidth(MainWindow.width())
    widget.setFixedHeight(MainWindow.height())

    widget.show()
    sys.exit(app.exec_())
