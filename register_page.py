from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *


class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.phone_no_label = QLabel('Phone Number')
        self.dob_label = QLabel('Date of Birth')
        self.address_label = QLabel('Address')
        self.balance_label = QLabel('Balance')
        self.password_label = QLabel('Password')

        self.phone_no_edit = QLineEdit()
        self.phone_no_edit.setMaxLength(10)
        self.dob_edit = QDateEdit()
        self.dob_edit.setDisplayFormat('dd-MM-yyyy')
        self.address_edit = QTextEdit()
        self.balance_edit = QLineEdit()
        self.int_validator = QIntValidator()
        self.balance_edit.setValidator(self.int_validator)
        self.password_edit = QLineEdit()
        self.password_edit.setMaxLength(32)
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.grid_layout.addWidget(self.phone_no_label, 0, 0)
        self.grid_layout.addWidget(self.phone_no_edit, 0, 1)
        self.grid_layout.addWidget(self.dob_label, 1, 0)
        self.grid_layout.addWidget(self.dob_edit, 1, 1)
        self.grid_layout.addWidget(self.address_label, 2, 0)
        self.grid_layout.addWidget(self.address_edit, 2, 1)
        self.grid_layout.addWidget(self.balance_label, 3, 0)
        self.grid_layout.addWidget(self.balance_edit, 3, 1)
        self.grid_layout.addWidget(self.password_label, 4, 0)
        self.grid_layout.addWidget(self.password_edit, 4, 1)

        self.title_label = QLabel('Customer Registration')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addLayout(self.grid_layout)

        self.submit_button = QPushButton('Submit')
        self.main_layout.addWidget(self.submit_button)

        self.setLayout(self.main_layout)
