from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.id_label = QLabel('ID')
        self.password_label = QLabel('Password')

        self.id_edit = QLineEdit()
        self.id_edit.setMaxLength(32)

        self.password_edit = QLineEdit()
        self.password_edit.setMaxLength(32)
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.grid_layout.addWidget(self.id_label, 0, 0)
        self.grid_layout.addWidget(self.id_edit, 0, 1)
        self.grid_layout.addWidget(self.password_label, 1, 0)
        self.grid_layout.addWidget(self.password_edit, 1, 1)

        self.title_label = QLabel('Customer Login')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addLayout(self.grid_layout)

        self.submit_button = QPushButton('Submit')
        self.main_layout.addWidget(self.submit_button)

        self.setLayout(self.main_layout)
