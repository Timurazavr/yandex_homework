import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6 import QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("coffee.sqlite")
        self.db.open()
        self.upp()
        self.pushButton.clicked.connect(self.run)

    def upp(self):
        model = QSqlTableModel(self, self.db)
        model.setTable("coffee")
        model.select()
        self.tableView.setModel(model)

    def run(self):
        Dialog(self)


class Dialog(QtWidgets.QDialog):
    def __init__(self, patent=None):
        super().__init__(parent=patent)
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.pushButton.clicked.connect(self.run)
        self.show()

    def run(self):
        try:
            idd, name, roasting, ground, taste, price, volume = (
                int(self.line_id.text()),
                self.line_name.text(),
                self.line_roasting.text(),
                self.line_ground.text(),
                self.line_taste.text(),
                int(self.line_price.text()),
                int(self.line_volume.text()),
            )
        except Exception:
            self.destroy()
            return
        if idd and name and roasting and ground and taste and price and volume:
            con = sqlite3.connect("coffee.sqlite")
            cur = con.cursor()
            result = cur.execute("""SELECT id FROM coffee""").fetchall()
            if (idd,) in result:
                cur = con.cursor()
                cur.execute(
                    f"""UPDATE coffee
                        SET name = '{name}',
                            roasting = '{roasting}',
                            ground = '{ground}',
                            taste = '{taste}',
                            price = {price},
                            volume = {volume}
                        WHERE id = {idd}"""
                )
            else:
                cur = con.cursor()
                cur.execute(
                    f"""INSERT INTO coffee(id, name, roasting, ground, taste, price, volume)
                VALUES({idd}, '{name}', '{roasting}', '{ground}', '{taste}', {price}, {volume})"""
                )
            con.commit()
            con.close()
            self.parent().upp()
            self.destroy()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
