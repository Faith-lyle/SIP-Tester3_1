#!/usr/bin/python3
# -- coding: utf-8 --
# @Author : Long.Hou
# @Email : Long2.Hou@luxshare-ict.com
# @File : longinpanel.py
# @Project : SIP-Tester3_1
# @Time : 2022/6/11 10:17
# -------------------------------
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QAbstractItemView, QTableWidgetItem, \
    QLabel
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QPropertyAnimation, QPoint
from Resource.UI.Login_UI import Ui_Form


class LoginPanel(QMainWindow, Ui_Form):
    passWorld_ture_siganl = pyqtSignal()
    cancel_signal = pyqtSignal()

    def __init__(self,key):
        self.key = key
        super(LoginPanel, self).__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_Bt_OK_clicked(self):
        user_name = self.Cbb_Username.currentText()
        if self.Edt_Password.text() == self.key:
            self.passWorld_ture_siganl.emit()
        else:
            for i in range(1000):
                animation = QPropertyAnimation(self)
                animation.setTargetObject(self)
                animation.setPropertyName(b'pos')
                # 2.设置属性值
                animation.setStartValue(QPoint(784,379))
                animation.setEndValue(QPoint(790,385))

                # 3.设置时长
                animation.setDuration(100)

                # 4.启动动画

                animation.start()

    @pyqtSlot()
    def on_Btn_Cancel_clicked(self):
        self.cancel_signal.emit()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.cancel_signal.emit()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LoginPanel('admin')
    main.show()
    sys.exit(app.exec_())
