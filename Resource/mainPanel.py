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
    QLabel
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal
from Resource.UI.main_ui import Ui_MainWindow


class MainPanel(QMainWindow, Ui_MainWindow):
    setting_signal = pyqtSignal()

    def __init__(self, items, config_dict):
        super(MainPanel, self).__init__()
        self.show_result_list = []
        self.items = items
        self.config_dict = config_dict
        self.setupUi(self)
        self.init_ui()
        self.set_style_from_file("./Resource/Style/PDCA.css")

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

    def set_style_from_file(self, file_path):
        with open(file_path, "r") as f:
            style = f.read()
            self.setStyleSheet(style)

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
            if type(chi) == QLabel:
                self.show_result_list.append(chi)
                chi.setGeometry(7 + (i * 65), 3, 55, 25)
                chi.setText("Ready")
                chi.setAlignment(Qt.AlignCenter)
                i += 1

    def test_slot_show_result(self, result: str, slot: int):
        if result == 'PASS':
            self.show_result_list[slot].setStyleSheet("background-color: green;")
            self.show_result_list[slot].setText("PASS")
        elif result == "FAIL":
            self.show_result_list[slot].setStyleSheet("background-color: red;")
            self.show_result_list[slot].setText("FAIL")
        elif result == "TEST":
            self.show_result_list[slot].setStyleSheet("background-color: yellow;")
            self.show_result_list[slot].setText("Testing")

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
    def on_actionPDCA_triggered(self):
        """
        PDCA 设置栏
        :return:
        """
        ...

    @pyqtSlot()
    def on_actionHelp_triggered(self):
        """
        帮助栏
        :return:
        """
        ...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainPanel()
    main.show()
    sys.exit(app.exec_())
