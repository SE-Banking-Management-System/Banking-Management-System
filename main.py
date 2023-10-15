import sys

from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow, QMessageBox

import database
from admin_login import AdminLogin
from admin_page import AdminPage
from dashboard import Dashboard
from home_page import HomePage
from login_page import LoginPage
from register_page import RegisterPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        database.init_db()

        self.home_page = HomePage()
        self.login_page = LoginPage()
        self.admin_login = AdminLogin()
        self.register_page = RegisterPage()
        self.dashboard = Dashboard()
        self.admin_page = AdminPage()

        self.setWindowTitle('Bank')
        self.setGeometry(100, 100, 640, 480)

        self.stacked_widget = QStackedWidget()

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.admin_login)
        self.stacked_widget.addWidget(self.register_page)
        self.stacked_widget.addWidget(self.dashboard)
        self.stacked_widget.addWidget(self.admin_page)

        self.stacked_widget.setCurrentWidget(self.home_page)

        self.setCentralWidget(self.stacked_widget)

        self.home_page.customer_login_button.clicked.connect(self.on_login)
        self.home_page.customer_registration_button.clicked.connect(self.on_register)
        self.home_page.admin_button.clicked.connect(self.on_admin)

        self.login_page.submit_button.clicked.connect(self.login_submit)

        self.dashboard.balance_button.clicked.connect(self.on_balance)
        self.dashboard.withdraw_button.clicked.connect(self.on_withdraw)
        self.dashboard.deposit_button.clicked.connect(self.on_deposit)
        self.dashboard.transfer_button.clicked.connect(self.on_transfer)

        self.register_page.submit_button.clicked.connect(self.register_submit)

        self.admin_login.submit_button.clicked.connect(self.admin_submit)

    def on_login(self):
        self.stacked_widget.setCurrentWidget(self.login_page)

    def login_submit(self):
        customer_id = self.login_page.id_edit.text()
        password = self.login_page.password_edit.text()
        flag = database.validate_customer(customer_id, password)

        if flag:
            database.current_login = customer_id
            self.stacked_widget.setCurrentWidget(self.dashboard)
        else:
            self.show_invalid_popup()

    def on_register(self):
        self.stacked_widget.setCurrentWidget(self.register_page)

    def register_submit(self):
        customer_id = database.get_next_customer_id()
        phone_no = self.register_page.phone_no_edit.text()
        dob = self.register_page.dob_edit.date().toString('yyyy-MM-dd')
        address = self.register_page.address_edit.toPlainText()
        balance = int(self.register_page.balance_edit.text())
        password = self.register_page.password_edit.text()

        database.register_customer(customer_id, password, balance, phone_no, address, dob)
        self.show_id_popup(customer_id)

        self.stacked_widget.setCurrentWidget(self.home_page)

    def on_admin(self):
        self.stacked_widget.setCurrentWidget(self.admin_login)

    def admin_submit(self):
        admin_id = self.admin_login.id_edit.text()
        password = self.admin_login.password_edit.text()
        flag = database.validate_admin(admin_id, password)

        if flag:
            self.stacked_widget.setCurrentWidget(self.admin_page)
        else:
            self.show_invalid_popup()

    def on_balance(self):
        balance = database.get_balance(database.current_login)
        self.show_balance_popup(balance)

    def on_withdraw(self):
        amount = int(self.dashboard.withdraw_edit.text())

        if database.withdraw(amount):
            self.dashboard.withdraw_edit.clear()
            balance = database.get_balance(database.current_login)
            self.show_balance_popup(balance)
        else:
            self.show_insufficient_balance_popup()

    def on_deposit(self):
        amount = int(self.dashboard.deposit_edit.text())
        database.deposit(amount)
        self.dashboard.deposit_edit.clear()
        balance = database.get_balance(database.current_login)
        self.show_balance_popup(balance)

    def on_transfer(self):
        account = self.dashboard.account_edit.text()
        amount = int(self.dashboard.amount_edit.text())

        if database.transfer(account, amount):
            self.dashboard.account_edit.clear()
            self.dashboard.amount_edit.clear()
            balance = database.get_balance(database.current_login)
            self.show_balance_popup(balance)
        else:
            self.show_insufficient_balance_popup()

    def show_invalid_popup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Invalid.")
        msg.setWindowTitle("Error")
        msg.exec_()

    def show_id_popup(self, customer_id):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.NoIcon)
        msg.setText(f"Your ID is {customer_id}.")
        msg.setWindowTitle("Successful")
        msg.exec_()

    def show_balance_popup(self, balance):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.NoIcon)
        msg.setText(f"Balance: {balance}")
        msg.setWindowTitle("Account Balance")
        msg.exec_()

    def show_insufficient_balance_popup(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Insufficient balance.")
        msg.setWindowTitle("Error")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
