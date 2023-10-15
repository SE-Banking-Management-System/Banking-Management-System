from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()

        self.logo = QPixmap('logo.png').scaled(320, 240)
        self.image_label = QLabel()
        self.image_label.setPixmap(self.logo)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.image_label)

        self.button_layout = QHBoxLayout()

        self.customer_login_button = QPushButton('Customer Login')
        self.customer_registration_button = QPushButton('Customer Registration')
        self.admin_button = QPushButton('Admin')

        self.button_layout.addWidget(self.customer_login_button)
        self.button_layout.addWidget(self.customer_registration_button)
        self.button_layout.addWidget(self.admin_button)

        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)
