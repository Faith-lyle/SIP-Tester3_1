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
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QHeaderView, QAbstractItemView, QTableWidgetItem, \
    QLabel
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QPropertyAnimation, QPoint
from Resource.UI.help import Ui_Help


class HelpPanel(QWidget, Ui_Help):

    def __init__(self):
        super(HelpPanel, self).__init__()
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = HelpPanel()
    main.show()
    sys.exit(app.exec_())
