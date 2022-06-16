#!/usr/bin/python3
# -- coding: utf-8 --
# @Author : Long.Hou
# @Email : Long2.Hou@luxshare-ict.com
# @File : mainPanel.py
# @Project : SIP-Tester3_1
# @Time : 2022/6/8 08:52
# -------------------------------
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QHeaderView, QAbstractItemView, QTableWidgetItem, \
    QLabel, QPushButton
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from Resource.UI.main_ui import Ui_MainWindow
from Resource.helpPanel import HelpPanel


class MainPanel(QMainWindow, Ui_MainWindow):
    setting_signal = pyqtSignal()
    edit_text_signal = pyqtSignal(str)
    pdca_signal = pyqtSignal(bool)
    close_signal = pyqtSignal()

    def __init__(self, items, config_dict):
        super(MainPanel, self).__init__()
        self.show_result_list = []
        self.items = items
        self.config_dict = config_dict
        self.user_slot_enable_flag = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.mes_slot_enable_flag = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.setupUi(self)
        self.init_ui()
        self.set_pdca_style()
        self.lineEdit.editingFinished.connect(lambda: self.edit_text_signal.emit(self.lineEdit.text()))

    def set_pdca_style(self):
        if self.config_dict['PdcaMode']:
            with open('./Resource/Style/PDCA.css', 'r') as f:
                self.setStyleSheet(f.read())
        else:
            with open('./Resource/Style/NOPDCA.css', 'r') as f:
                self.setStyleSheet(f.read())

    def init_ui(self):
        self.init_tabel_widget()
        self.update_data_to_tabel(self.items)
        self.test_slot_init()
        try:
            self.add_fail_qty(1, 0)
            self.add_pass_qty(1, 0)
            self.add_fail_qty(2, 0)
            self.add_pass_qty(2, 0)
        except ZeroDivisionError:
            self.lb_site1_yield_2.setText("100%")
            self.lb_site1_yield.setText("100%")

    def init_tabel_widget(self):
        self.tableWidget.setColumnCount(18)
        self.tableWidget.setRowCount(20)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        for i in range(18):
            if i == 0:
                self.tableWidget.setColumnWidth(i, 30)
            elif i == 1:
                self.tableWidget.setColumnWidth(i, 250)
            else:
                self.tableWidget.setColumnWidth(i, 65)

    def update_data_to_tabel(self, items):
        header = ['NO', "TestItem", "Upper", "Lower"]
        for i in range(14):
            header.append("Slot{}".format(i + 1))
        self.tableWidget.setHorizontalHeaderLabels(header)
        for x, item in enumerate(items):
            for y, text in enumerate(header):
                try:
                    Qitem = QTableWidgetItem(item[text])
                except:
                    Qitem = QTableWidgetItem('')
                Qitem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                if x % 2 == 0:
                    Qitem.setBackground(QColor("#D4D4D4"))
                self.tableWidget.setItem(x, y, Qitem)

    def clear_line_edit(self):
        """
        清除lineEdit的内容，准备下一次测试
        :return:
        """
        self.lineEdit.setText('')

    def add_value(self, row, column, value, color):
        """
        添加数据到表格中
        :param row: 行号
        :param column: 列号
        :param value: 显示值
        :param color:  字体颜色
        :return:
        """
        Qitem = QTableWidgetItem(str(value))
        Qitem.setForeground(QColor(color))
        Qitem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(row, column, Qitem)

    def tabel_select_row(self, row):
        """
        选择表格的某一行
        :param row: 行数
        :return: None
        """
        self.tableWidget.selectRow(row)

    def tabel_content_clear(self):
        """
        清除表格的测试数据，保留Item和upper、lower
        :return: None
        """
        self.tableWidget.clear()
        self.update_data_to_tabel(self.items)

    def test_slot_init(self):
        """
        测试结果显示label初始化，所有的测试结果显示label都在self.show_result_list里面
        :return:
        """
        i = 0
        for chi in self.widget_4.children():
            if type(chi) == QPushButton:
                self.show_result_list.append(chi)
                chi.setGeometry(7 + (i * 65), 3, 57, 25)
                chi.setText("Ready")
                chi.setProperty('slot', i + 1)
                chi.setProperty('Enable', True)
                chi.setStyleSheet('border:1px outset black;background-color:Cyan')
                chi.clicked.connect(self.link_clicked)
                i += 1

    def link_clicked(self):
        slot = self.sender().property('slot')
        enable = self.sender().property('Enable')
        self.sender().setProperty("Enable", False if enable else True)
        if not enable:
            self.sender().setStyleSheet('border:1px outset black;background-color:Cyan')
            self.sender().setText("Ready")
            self.user_slot_enable_flag[slot - 1] = 1
        else:
            self.sender().setStyleSheet('border:1px outset black;background-color:Gray')
            self.sender().setText("Skip")
            self.user_slot_enable_flag[slot - 1] = 0

        print(self.user_slot_enable_flag)

    def test_slot_show_result(self, result: str, slot: int):
        if result == 'PASS':
            self.show_result_list[slot].setStyleSheet("'border:1px outset black;background-color: green;")
            self.show_result_list[slot].setText("PASS")
        elif result == "FAIL":
            self.show_result_list[slot].setStyleSheet("'border:1px outset black;background-color: red;")
            self.show_result_list[slot].setText("FAIL")
        elif result == "TEST":
            self.show_result_list[slot].setStyleSheet("'border:1px outset black;background-color: yellow;")
            self.show_result_list[slot].setText("Testing")

    def test_slot_enable(self, enable, slot):
        """
        MES enable 测试通道
        :param enable: Ture or False
        :param slot:  通道号
        :return:
        """
        if enable:
            self.show_result_list[slot].setStyleSheet('border:1px outset black;background-color:Cyan')
            self.show_result_list[slot].setText("Ready")
            self.mes_slot_enable_flag[slot] = 1
        else:
            self.show_result_list[slot].setStyleSheet('border:1px outset black;background-color:Gray')
            self.show_result_list[slot].setText("Skip")
            self.mes_slot_enable_flag[slot] = 0

    def add_pass_qty(self, site, qty):
        if site == 1:
            self.config_dict['PASSQty1'] += qty
            self.lb_site1_pass.setText(str(self.config_dict['PASSQty1']))
            total = self.config_dict['PASSQty1'] + self.config_dict['FAILQty1']
            self.lb_site1_yield.setText("{:.2f}".format(self.config_dict['PASSQty1'] / total))
        elif site == 2:
            self.config_dict['PASSQty2'] += qty
            self.lb_site2_pass.setText(str(self.config_dict['PASSQty2']))
            total = self.config_dict['PASSQty2'] + self.config_dict['FAILQty2']
            self.lb_site1_yield_2.setText("{:.2f}".format(self.config_dict['PASSQty2'] / total))

    def add_fail_qty(self, site: int, qty: int):
        if site == 1:
            self.config_dict['FAILQty1'] += qty
            self.lb_site1_fail.setText(str(self.config_dict['FAILQty1']))
            total = self.config_dict['PASSQty1'] + self.config_dict['FAILQty1']
            self.lb_site1_yield.setText("{:.2f}".format(self.config_dict['PASSQty1'] / total))
        elif site == 2:
            self.config_dict['FAILQty2'] += qty
            self.lb_site2_fail.setText(str(self.config_dict['FAILQty2']))
            total = self.config_dict['PASSQty2'] + self.config_dict['FAILQty2']
            self.lb_site1_yield_2.setText("{:.2f}".format(self.config_dict['PASSQty2'] / total))

    def clear_count_qty(self, site):
        if site == 1:
            self.config_dict['FAILQty1'] = 0
            self.config_dict['PASSQty1'] = 0
            self.lb_site1_pass.setText("0")
            self.lb_site1_fail.setText("0")
            self.lb_site1_yield.setText("100%")
        elif site == 2:
            self.config_dict['FAILQty2'] = 0
            self.config_dict['PASSQty2'] = 0
            self.lb_site2_pass.setText("0")
            self.lb_site2_fail.setText("0")
            self.lb_site1_yield_2.setText("100%")

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.clear_count_qty(1)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.clear_count_qty(2)

    @pyqtSlot()
    def on_action_triggered(self):
        """
        设置菜单栏
        :return:
        """
        self.setting_signal.emit()

    @pyqtSlot()
    def on_actionDisable_triggered(self):
        """
        PDCA 关闭
        :return:
        """
        self.lb_Pdca.setText("NOPDCA")
        self.config_dict['PdcaMode'] = False
        self.pdca_signal.emit(False)

    @pyqtSlot()
    def on_actionEnable_triggered(self):
        """
        PDCA 开启
        :return:
        """
        self.lb_Pdca.setText("PDCA")
        self.config_dict['PdcaMode'] = True
        self.pdca_signal.emit(True)

    @pyqtSlot()
    def on_actionHelp_triggered(self):
        """
        帮助栏
        :return:
        """
        self.help = HelpPanel()
        self.help.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.close_signal.emit()
        super(MainPanel, self).closeEvent(a0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainPanel()
    main.show()
    sys.exit(app.exec_())
