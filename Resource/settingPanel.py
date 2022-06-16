#!/usr/bin/python3
# -- coding: utf-8 --
# @Author : Long.Hou
# @Email : Long2.Hou@luxshare-ict.com
# @File : settingPanel.py
# @Project : SIP-Tester3_1
# @Time : 2022/6/13 08:47
# -------------------------------
import os
import sys, glob
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QHeaderView, QAbstractItemView, QTableWidgetItem, \
    QLabel, QComboBox, QLineEdit, QCheckBox, QPushButton
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QPropertyAnimation, QPoint, QTimer
from Resource.UI.setting import Ui_Form
from Tools.utils import CommonHelper


class SettingPanel(QWidget, Ui_Form):
    setup_start_signal = pyqtSignal(str)

    def __init__(self, config_data):
        super(SettingPanel, self).__init__()
        self.config = config_data
        self.cob_list = []
        self.line_list = []
        self.btn_list = []
        self.slot_search_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.slot_search_stop_list = [False, False, False, False, False, False, False, False, False, False, False,
                                      False, False, False]
        self.search_path_list = [':/log/search2-48.png', ':/log/search4-48.png', ':/log/search6-48.png',
                                 ':/log/search8-48.png']
        self.setupUi(self)
        self.setup()

    def setup(self):
        self.tabel_widget_init()

    def tabel_widget_init(self):
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        header = ['Slot', 'SerialPorts', 'VirtualPorts', 'Enabled', 'Setup']
        for i, text in enumerate(header):
            Qitem = QTableWidgetItem(text)
            Qitem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            Qitem.setFont(QFont('Arial', 17))
            self.tableWidget.setHorizontalHeaderItem(i, Qitem)
        self.tableWidget.setColumnWidth(1, 350)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)
        ports = glob.glob('/dev/cu.usbserial*')
        for y in range(14):
            self.tableWidget.setRowHeight(y, 45)
            for x in range(5):
                if x == 0:
                    Qitem = QTableWidgetItem("Slot%s" % (y + 1))
                    Qitem.setFont(QFont('Arial', 12))
                    Qitem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(y, x, Qitem)
                elif x == 1:
                    comb = QComboBox(self)
                    self.cob_list.append(comb)
                    comb.setStyleSheet("margin:5px 10px 5px 10px;text-align:center;font:'Arial 11")
                    for port in ports:
                        comb.addItem(port)
                    comb.addItem(self.config['SerialPorts'][y])
                    # print(self.config['SerialPorts'][y])
                    comb.setCurrentText(self.config['SerialPorts'][y])
                    self.tableWidget.setCellWidget(y, x, comb)
                elif x == 2:
                    line = QLineEdit(self)
                    self.line_list.append(line)
                    line.setReadOnly(True)
                    line.setText(self.config['VirtualPorts'][y])
                    line.setStyleSheet("margin:5px 10px 5px 10px ;height:20px;text-align:center;")
                    self.tableWidget.setCellWidget(y, x, line)
                elif x == 3:
                    ckb = QCheckBox(self)
                    # print(self.config["SlotEnable"][y])
                    ckb.setChecked(True) if self.config["SlotEnable"][y] else ckb.setEnabled(False)
                    ckb.setText('Enabled')
                    ckb.setStyleSheet("margin:5px 20px 5px 40px")
                    ckb.setProperty("slot", y)
                    self.tableWidget.setCellWidget(y, x, ckb)
                    ckb.clicked.connect(self.response_ckb_state)
                elif x == 4:
                    btn = QPushButton(self)
                    self.btn_list.append(btn)
                    btn.setText("Setup")
                    btn.setProperty('slot', y)
                    btn.setStyleSheet("margin:6px;height:50px;")
                    # icon1 = QtGui.QIcon()
                    # icon1.addPixmap(QtGui.QPixmap(":/log/search2-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    # btn.setIconSize(QtCore.QSize(30, 30))
                    # btn.setIcon(icon1)
                    btn.clicked.connect(self.response_btn_clicked)
                    self.tableWidget.setCellWidget(y, x, btn)

    def response_ckb_state(slef, click):
        slef.config['SlotEnable'][slef.sender().property('slot')] = click

    def response_btn_clicked(self):
        """
        响应设置串口按钮按下事件，调用定时器更新背景图片
        :return:
        """
        slot = self.sender().property('slot')
        self.sender().setText('')
        self.sender().setEnabled(False)
        self.setup_start_signal.emit(self.cob_list[slot].currentText())
        time1 = QTimer(self)
        time1.setProperty('slot', slot)
        time1.timeout.connect(self.timer_timeout)
        time1.start(150)

    def timer_timeout(self):
        """
        定时器响应事件
        :return:
        """
        slot = self.sender().property('slot')
        self.btn_list[slot].setStyleSheet("margin:6px;height:50px;image:url({});".format(
            self.search_path_list[self.slot_search_list[slot]]
        ))
        self.slot_search_list[slot] += 1
        if self.slot_search_list[slot] == 4:
            self.slot_search_list[slot] = 0
        if self.slot_search_stop_list[slot]:
            self.btn_list[slot].setEnable(True)
            self.btn_list[slot].setText("Setup")
            self.btn_list.setStyleSheet("margin:6px;height:50px;")
        else:
            self.sender().start()

    def set_create_port_finished(self,slot,virtual_port):
        """
        串口配置完成出发方法
        :param virtual_port: 虚拟串口号
        :param slot: 通道号
        :return:
        """
        self.slot_search_stop_list[slot]=True
        self.line_list[slot].setText(virtual_port)
        self.config['VirtualPorts'][slot] = virtual_port


if __name__ == '__main__':
    configBaseDir = os.path.expanduser("~/SIP_Tester3")
    config_json_path = os.path.join(configBaseDir, "config.json")
    helper = CommonHelper()
    config_json = helper.read_json(config_json_path)
    app = QApplication(sys.argv)
    main = SettingPanel(config_json)
    main.show()
    sys.exit(app.exec_())
