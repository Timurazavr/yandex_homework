import sys
import sqlite3
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6 import QtWidgets, QtCore


class MyWidget(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(100, 90, 601, 461))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Изм/доб"))

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("data/coffee.sqlite")
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
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(666, 516)
        self.layoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 541, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Ignored
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line_id = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.line_id.setObjectName("line_id")
        self.verticalLayout_2.addWidget(self.line_id)
        self.line_name = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.line_name.setObjectName("line_name")
        self.verticalLayout_2.addWidget(self.line_name)
        self.line_roasting = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.line_roasting.setObjectName("line_roasting")
        self.verticalLayout_2.addWidget(self.line_roasting)
        self.line_ground = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_ground.sizePolicy().hasHeightForWidth())
        self.line_ground.setSizePolicy(sizePolicy)
        self.line_ground.setObjectName("line_ground")
        self.verticalLayout_2.addWidget(self.line_ground)
        self.line_taste = QtWidgets.QLineEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_taste.sizePolicy().hasHeightForWidth())
        self.line_taste.setSizePolicy(sizePolicy)
        self.line_taste.setObjectName("line_taste")
        self.verticalLayout_2.addWidget(self.line_taste)
        self.line_price = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.line_price.setObjectName("line_price")
        self.verticalLayout_2.addWidget(self.line_price)
        self.line_volume = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.line_volume.setObjectName("line_volume")
        self.verticalLayout_2.addWidget(self.line_volume)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(359, 434, 221, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "id"))
        self.label_2.setText(_translate("Dialog", "название"))
        self.label_3.setText(_translate("Dialog", "обжарка"))
        self.label_4.setText(_translate("Dialog", "молотый"))
        self.label_5.setText(_translate("Dialog", "вкус"))
        self.label_7.setText(_translate("Dialog", "Цена"))
        self.label_6.setText(_translate("Dialog", "объем"))
        self.pushButton.setText(_translate("Dialog", "Сохранить"))

    def __init__(self, patent=None):
        super().__init__(parent=patent)
        self.setupUi(self)
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
            con = sqlite3.connect("data/coffee.sqlite")
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
