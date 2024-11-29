import sys

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("coffee.sqlite")
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable("coffee")
        model.select()
        self.tableView.setModel(model)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
