import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget

class TodoListApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)


        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.add_button = QPushButton('Add Task', self)
        self.add_button.clicked.connect(self.add_task)

        self.task_list = QListWidget(self)
        self.load_tasks()

        layout.addWidget(self.task_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_list)

        self.central_widget.setLayout(layout)

        self.setWindowTitle('To-Do List')

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.db_handler.execute('INSERT INTO tasks (task) VALUES (%s)', (task,))
            self.task_input.clear()
            self.load_tasks()


    def load_tasks(self):
        self.task_list.clear()
        tasks = self.db_handler.fetch_all('SELECT task FROM tasks')
        for task in tasks:
            self.task_list.addItem(task[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = TodoListApp()
    todo_app.show()
    sys.exit(app.exec_())
