#!/usr/bin/python3
# -- coding: utf-8 --
# @Author : Long.Hou
# @Email : Long2.Hou@luxshare-ict.com
# @File : main.py
# @Project : SIP-Tester3_1
# @Time : 2022/6/7 14:23
# -------------------------------
import csv, json
import os.path
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from Resource.mainPanel import MainPanel
from Resource.longinpanel import LoginPanel
from Tools.utils import *

configBaseDir = os.path.expanduser("~/SIP_Tester3")
test_plan_path = os.path.join(configBaseDir, "TestPlan.csv")
config_json_path = os.path.join(configBaseDir, "config.json")


def config_file_check():
    if not os.path.exists(configBaseDir):
        os.mkdir(configBaseDir)
    if not os.path.exists(test_plan_path) or not os.path.exists(config_json_path):
        QMessageBox.critical(None, "Error", "Config file not found, Please try again!")
        exit()


def main_signal_connect():
    main.setting_signal.connect(main_setting_signal_slot)


def main_setting_signal_slot():
    main.hide()
    login.show()


def login_signal_connect():
    login.cancel_signal.connect(login_cancel_signal_slot)


def login_cancel_signal_slot():
    login.hide()
    main.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    helper = CommonHelper()
    config_file_check()
    items = helper.read_test_plant(test_plan_path)
    config_json = helper.read_json(config_json_path)
    main = MainPanel(items, config_json)
    main_signal_connect()
    login = LoginPanel('admin')
    login_signal_connect()
    main.show()
    sys.exit(app.exec_())
