#!/usr/bin/python3
# -- coding: utf-8 --
# @Author : Long.Hou
# @Email : Long2.Hou@luxshare-ict.com
# @File : utils.py
# @Project : SIP-Tester3_1
# @Time : 2022/6/8 09:24
# -------------------------------
import csv
import json


class TestItem:
    def __init__(self, **args):
        if "TestName" in args.keys():
            self._TestName = args['TestName']
        else:
            self._TestName = None
        if "TestResult" in args.keys():
            self._TestResult = args['TestResult']
        else:
            self._TestResult = None
        if "TestLower" in args.keys():
            self._TestLower = args['TestLower']
        else:
            self._TestLower = None
        if "TestUpper" in args.keys():
            self._TestUpper = args['TestUpper']
        else:
            self._TestUpper = None
        if "TestEnabled" in args.keys():
            if args["TestEnabled"].lower() == "true":
                self._IsEnabled = True
            else:
                self._IsEnabled = False
        else:
            self._IsEnabled = False
        if 'TestCmd' in args.keys():
            self._TestCmd = args["TestCmd"]
        else:
            self._TestCmd = None
        if "ReMarket" in args.keys():
            self._ReMarket = args["ReMarket"]
        else:
            self._ReMarket = None
        if "DecisionMode" in args.keys():
            self._DecisionMode = args["DecisionMode"]
        else:
            self._DecisionMode = None
        if "TestMode" in args.keys():
            self._TestMode = args["TestMode"]
        else:
            self._TestMode = None
        if "TestValue" in args.keys():
            self._TestValue = args["TestValue"]
        else:
            self._TestValue = None
        if "ReTestTime" in args.keys():
            self._ReTestTime = args["ReTestTime"]
        else:
            self._ReTestTime = None

    @property
    def ReTestTime(self):
        return self._ReTestTime

    @property
    def TestResult(self):
        return self._TestResult

    @property
    def TestMode(self):
        return self._TestMode

    @TestResult.setter
    def TestValue(self, value):
        self._TestResult = value

    @property
    def DecisionMode(self):
        return self._DecisionMode

    @property
    def ReMarket(self):
        return self._ReMarket

    @ReMarket.setter
    def ReMarket(self, value):
        self._ReMarket = value

    @property
    def TestValue(self):
        return self._TestValue

    @TestValue.setter
    def TestValue(self, value):
        self._TestValue = value

    @property
    def TestName(self):
        return self._TestName

    @TestName.setter
    def TestName(self, name):
        self._TestName = name

    @property
    def TestLower(self):
        return self._TestLower

    @TestLower.setter
    def TestLower(self, Lower):
        self._TestLower = Lower

    @property
    def TestUpper(self):
        return self._TestUpper

    @TestUpper.setter
    def TestUpper(self, upper):
        self._TestUpper = upper

    @property
    def isEnabled(self):
        return self._IsEnabled

    @isEnabled.setter
    def isEnabled(self, enabled):
        self._IsEnabled = enabled

    @property
    def TestCmd(self):
        return self._TestCmd


class CommonHelper:
    @staticmethod
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

    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f, encoding='utf-8')
            return data

if __name__ == '__main__':
    ...
