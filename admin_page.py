from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import database


class AdminPage(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.title_label = QLabel('Admin Dashboard')
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        data = database.retrieve_customers()
        len_data = len(data)

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(len_data + 1)
        self.table_widget.setColumnCount(6)

        column_labels = ["Customer ID", "Password", "Balance", "Date of Birth", "Phone Number", "Address"]
        self.table_widget.setHorizontalHeaderLabels(column_labels)

        for i in range(0, len_data):
            current_data = data[i]
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(current_data[0])))
            self.table_widget.setItem(i, 1, QTableWidgetItem(str(current_data[1])))
            self.table_widget.setItem(i, 2, QTableWidgetItem(str(current_data[2])))
            self.table_widget.setItem(i, 3, QTableWidgetItem(str(current_data[5])))
            self.table_widget.setItem(i, 4, QTableWidgetItem(str(current_data[3])))
            self.table_widget.setItem(i, 5, QTableWidgetItem(str(current_data[4])))

        self.main_layout.addWidget(self.table_widget)

        self.setLayout(self.main_layout)
