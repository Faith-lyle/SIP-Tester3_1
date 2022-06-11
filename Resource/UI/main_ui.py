# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 668)
        MainWindow.setMinimumSize(QtCore.QSize(1366, 668))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 668))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 230, 100))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lb_site1_pass = QtWidgets.QLabel(self.widget)
        self.lb_site1_pass.setGeometry(QtCore.QRect(75, 10, 60, 16))
        self.lb_site1_pass.setObjectName("lb_site1_pass")
        self.lb_site1_fail = QtWidgets.QLabel(self.widget)
        self.lb_site1_fail.setGeometry(QtCore.QRect(75, 40, 60, 16))
        self.lb_site1_fail.setObjectName("lb_site1_fail")
        self.lb_site1_yield = QtWidgets.QLabel(self.widget)
        self.lb_site1_yield.setGeometry(QtCore.QRect(75, 70, 60, 16))
        self.lb_site1_yield.setObjectName("lb_site1_yield")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(160, 20, 60, 16))
        self.label_7.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(140, 50, 80, 40))
        self.pushButton.setObjectName("pushButton")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(280, 10, 230, 100))
        self.widget_2.setObjectName("widget_2")
        self.label_8 = QtWidgets.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 60, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 60, 16))
        self.label_10.setObjectName("label_10")
        self.lb_site2_pass = QtWidgets.QLabel(self.widget_2)
        self.lb_site2_pass.setGeometry(QtCore.QRect(75, 10, 60, 16))
        self.lb_site2_pass.setObjectName("lb_site2_pass")
        self.lb_site2_fail = QtWidgets.QLabel(self.widget_2)
        self.lb_site2_fail.setGeometry(QtCore.QRect(75, 40, 60, 16))
        self.lb_site2_fail.setObjectName("lb_site2_fail")
        self.lb_site1_yield_2 = QtWidgets.QLabel(self.widget_2)
        self.lb_site1_yield_2.setGeometry(QtCore.QRect(75, 70, 60, 16))
        self.lb_site1_yield_2.setObjectName("lb_site1_yield_2")
        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(160, 20, 60, 16))
        self.label_14.setStyleSheet("font: 75 16pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 50, 80, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(700, 10, 71, 31))
        self.label_15.setStyleSheet("font: 75 28pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.lb_ct = QtWidgets.QLabel(self.centralwidget)
        self.lb_ct.setGeometry(QtCore.QRect(770, 13, 60, 21))
        self.lb_ct.setStyleSheet("font: 75 24pt \"Arial\";")
        self.lb_ct.setObjectName("lb_ct")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(560, 60, 160, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(550, 80, 300, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(870, 10, 231, 100))
        self.widget_3.setObjectName("widget_3")
        self.label_18 = QtWidgets.QLabel(self.widget_3)
        self.label_18.setGeometry(QtCore.QRect(10, 30, 201, 61))
        self.label_18.setStyleSheet("font: 75 18pt \"Arial\";")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.widget_3)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_19.setObjectName("label_19")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(420, 115, 931, 31))
        self.widget_4.setObjectName("widget_4")
        self.lb_1 = QtWidgets.QLabel(self.widget_4)
        self.lb_1.setGeometry(QtCore.QRect(10, 6, 55, 20))
        self.lb_1.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_1.setObjectName("lb_1")
        self.lb_2 = QtWidgets.QLabel(self.widget_4)
        self.lb_2.setGeometry(QtCore.QRect(70, 6, 55, 20))
        self.lb_2.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_2.setObjectName("lb_2")
        self.lb_4 = QtWidgets.QLabel(self.widget_4)
        self.lb_4.setGeometry(QtCore.QRect(210, 6, 55, 20))
        self.lb_4.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_4.setObjectName("lb_4")
        self.lb_3 = QtWidgets.QLabel(self.widget_4)
        self.lb_3.setGeometry(QtCore.QRect(140, 6, 55, 20))
        self.lb_3.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_3.setObjectName("lb_3")
        self.lb_7 = QtWidgets.QLabel(self.widget_4)
        self.lb_7.setGeometry(QtCore.QRect(420, 6, 55, 20))
        self.lb_7.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_7.setObjectName("lb_7")
        self.lb_6 = QtWidgets.QLabel(self.widget_4)
        self.lb_6.setGeometry(QtCore.QRect(350, 6, 55, 20))
        self.lb_6.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_6.setObjectName("lb_6")
        self.lb_5 = QtWidgets.QLabel(self.widget_4)
        self.lb_5.setGeometry(QtCore.QRect(280, 6, 55, 20))
        self.lb_5.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_5.setObjectName("lb_5")
        self.lb_8 = QtWidgets.QLabel(self.widget_4)
        self.lb_8.setGeometry(QtCore.QRect(490, 6, 55, 20))
        self.lb_8.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_8.setObjectName("lb_8")
        self.lb_11 = QtWidgets.QLabel(self.widget_4)
        self.lb_11.setGeometry(QtCore.QRect(700, 6, 55, 20))
        self.lb_11.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_11.setObjectName("lb_11")
        self.lb_10 = QtWidgets.QLabel(self.widget_4)
        self.lb_10.setGeometry(QtCore.QRect(630, 6, 55, 20))
        self.lb_10.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_10.setObjectName("lb_10")
        self.lb_9 = QtWidgets.QLabel(self.widget_4)
        self.lb_9.setGeometry(QtCore.QRect(560, 6, 55, 20))
        self.lb_9.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_9.setObjectName("lb_9")
        self.lb_12 = QtWidgets.QLabel(self.widget_4)
        self.lb_12.setGeometry(QtCore.QRect(770, 6, 55, 20))
        self.lb_12.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_12.setObjectName("lb_12")
        self.lb_13 = QtWidgets.QLabel(self.widget_4)
        self.lb_13.setGeometry(QtCore.QRect(830, 6, 55, 20))
        self.lb_13.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_13.setObjectName("lb_13")
        self.lb_14 = QtWidgets.QLabel(self.widget_4)
        self.lb_14.setGeometry(QtCore.QRect(890, 6, 55, 20))
        self.lb_14.setStyleSheet("background-color: rgb(69, 207, 255);")
        self.lb_14.setObjectName("lb_14")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1120, 10, 211, 81))
        self.label_20.setStyleSheet("image: url(:/log/luxshare2.png);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 151, 1341, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.lb_Pdca = QtWidgets.QLabel(self.centralwidget)
        self.lb_Pdca.setGeometry(QtCore.QRect(540, 20, 60, 16))
        self.lb_Pdca.setStyleSheet("font: 75 22pt \"Arial\";\n"
"color: rgb(255, 211, 17);")
        self.lb_Pdca.setObjectName("lb_Pdca")
        self.widget_3.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.label_15.raise_()
        self.lb_ct.raise_()
        self.label_17.raise_()
        self.lineEdit.raise_()
        self.widget_4.raise_()
        self.label_20.raise_()
        self.tableWidget.raise_()
        self.lb_Pdca.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.actionPDCA = QtWidgets.QAction(MainWindow)
        self.actionPDCA.setObjectName("actionPDCA")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menu.addAction(self.action)
        self.menu.addAction(self.actionPDCA)
        self.menu.addAction(self.action_2)
        self.menu_2.addAction(self.actionHelp)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.action_2.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TestPanel"))
        self.label.setText(_translate("MainWindow", "PASS Qty:"))
        self.label_2.setText(_translate("MainWindow", "FAIL Qty:"))
        self.label_3.setText(_translate("MainWindow", "Yield:"))
        self.lb_site1_pass.setText(_translate("MainWindow", "0"))
        self.lb_site1_fail.setText(_translate("MainWindow", "0"))
        self.lb_site1_yield.setText(_translate("MainWindow", "100%"))
        self.label_7.setText(_translate("MainWindow", "工位1"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))
        self.label_8.setText(_translate("MainWindow", "PASS Qty:"))
        self.label_9.setText(_translate("MainWindow", "FAIL Qty:"))
        self.label_10.setText(_translate("MainWindow", "Yield:"))
        self.lb_site2_pass.setText(_translate("MainWindow", "0"))
        self.lb_site2_fail.setText(_translate("MainWindow", "0"))
        self.lb_site1_yield_2.setText(_translate("MainWindow", "100%"))
        self.label_14.setText(_translate("MainWindow", "工位2"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.label_15.setText(_translate("MainWindow", "CT："))
        self.lb_ct.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Serial_Number"))
        self.label_18.setText(_translate("MainWindow", "A5-2F-S12_\n"
"SIP_Measurement_L_1"))
        self.label_19.setText(_translate("MainWindow", "站点名称："))
        self.lb_1.setText(_translate("MainWindow", "Slot1"))
        self.lb_2.setText(_translate("MainWindow", "Slot1"))
        self.lb_4.setText(_translate("MainWindow", "Slot1"))
        self.lb_3.setText(_translate("MainWindow", "Slot1"))
        self.lb_7.setText(_translate("MainWindow", "Slot1"))
        self.lb_6.setText(_translate("MainWindow", "Slot1"))
        self.lb_5.setText(_translate("MainWindow", "Slot1"))
        self.lb_8.setText(_translate("MainWindow", "Slot1"))
        self.lb_11.setText(_translate("MainWindow", "Slot1"))
        self.lb_10.setText(_translate("MainWindow", "Slot1"))
        self.lb_9.setText(_translate("MainWindow", "Slot1"))
        self.lb_12.setText(_translate("MainWindow", "Slot1"))
        self.lb_13.setText(_translate("MainWindow", "Slot1"))
        self.lb_14.setText(_translate("MainWindow", "Slot1"))
        self.lb_Pdca.setText(_translate("MainWindow", "PDCA"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "设置"))
        self.action.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_2.setText(_translate("MainWindow", "退出"))
        self.action_2.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPDCA.setText(_translate("MainWindow", "PDCA"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
from Resource.Img import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
