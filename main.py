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
from Tools.utils import *

configBaseDir = os.path.expanduser("~/SIP_Tester3")
test_plan_path = os.path.join(configBaseDir, "TestPlan.csv")
config_json_path = os.path.join(configBaseDir, "config.json")


def read_test_plant(file_path):
    with open(file_path, 'r') as f:
        datas = []
        reader = csv.reader(f)
        reader = list(reader)
        header = reader[0]
        for row in reader[1:]:
            data = {}
            for i in range(len(header)):
                data[header[i]] = row[i]
            datas.append(data)
        return datas


def config_file_check():
    if not os.path.exists(configBaseDir):
        os.mkdir(configBaseDir)
    if not os.path.exists(test_plan_path) or not os.path.exists(config_json_path):
        QMessageBox.critical(None, "Error", "Config file not found, Please try again!")
        exit()


def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f, encoding='utf-8')
        return data


if __name__ == '__main__':
    app = QApplication(sys.argv)
    config_file_check()
    items = read_test_plant(test_plan_path)
    config_json = read_json(config_json_path)
    print(config_json)
    main = MainPanel(items,config_json)
    main.show()
    sys.exit(app.exec_())
