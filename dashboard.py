from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()

        self.title_label = QLabel('Customer Dashboard')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        self.transaction_container = QHBoxLayout()
        self.balance_button = QPushButton('Check Balance')
        self.transaction_container.addWidget(self.balance_button)
        self.withdraw_container = QVBoxLayout()
        self.transaction_container.addLayout(self.withdraw_container)
        self.deposit_container = QVBoxLayout()
        self.transaction_container.addLayout(self.deposit_container)

        self.withdraw_label = QLabel('Withdraw')
        self.withdraw_label.setAlignment(Qt.AlignCenter)
        self.withdraw_container.addWidget(self.withdraw_label)
        self.withdraw_edit = QLineEdit()
        self.int_validator = QIntValidator()
        self.withdraw_edit.setValidator(self.int_validator)
        self.withdraw_container.addWidget(self.withdraw_edit)
        self.withdraw_button = QPushButton('Withdraw')
        self.withdraw_container.addWidget(self.withdraw_button)

        self.deposit_label = QLabel('Deposit')
        self.deposit_label.setAlignment(Qt.AlignCenter)
        self.deposit_container.addWidget(self.deposit_label)
        self.deposit_edit = QLineEdit()
        self.deposit_edit.setValidator(self.int_validator)
        self.deposit_container.addWidget(self.deposit_edit)
        self.deposit_button = QPushButton('Deposit')
        self.deposit_container.addWidget(self.deposit_button)

        self.main_layout.addLayout(self.transaction_container)

        self.transfer_label = QLabel('Transfer')
        self.transfer_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.transfer_label)

        self.transfer_container = QHBoxLayout()
        self.transfer_input_container = QGridLayout()

        self.account_label = QLabel('Account ID')
        self.account_edit = QLineEdit()
        self.account_edit.setMaxLength(32)
        self.amount_label = QLabel('Amount')
        self.amount_edit = QLineEdit()
        self.amount_edit.setValidator(self.int_validator)

        self.transfer_input_container.addWidget(self.account_label, 0, 0)
        self.transfer_input_container.addWidget(self.account_edit, 0, 1)
        self.transfer_input_container.addWidget(self.amount_label, 1, 0)
        self.transfer_input_container.addWidget(self.amount_edit, 1, 1)

        self.transfer_button = QPushButton('Transfer')
        self.transfer_container.addLayout(self.transfer_input_container)

        self.transfer_container.addWidget(self.transfer_button)
        self.main_layout.addLayout(self.transfer_container)

        self.setLayout(self.main_layout)
