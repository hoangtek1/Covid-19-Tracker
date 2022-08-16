from ChartCovid import getChartCountry
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
import requests
import json
import sys
import matplotlib.pyplot as plt
import threading
import time
import datetime

today = datetime.date.today()

from datetime import datetime


url = "https://covid-193.p.rapidapi.com/countries"
headers = {
'x-rapidapi-key': "d75d11379dmsh2fb9e7d45403dbfp1c5a3bjsn935caac1a850",
'x-rapidapi-host': "covid-193.p.rapidapi.com"}
response = requests.request("GET", url, headers=headers)
dataAllNameCountry = response.json()


urlData = "https://covid-193.p.rapidapi.com/statistics?country="
headersData = {
'x-rapidapi-key': "c0dced8bb9mshbc64e8fcf6cc50ap124d32jsn54f979df4709",
'x-rapidapi-host': "covid-193.p.rapidapi.com"}
responseData = requests.request("GET", urlData + "all", headers=headersData)
dataTotalCaseAllWorld = responseData.json()



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.setGeometry(340,150,1270,398)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(30)
        Dialog.setFont(font)
        Dialog.setStyleSheet(
        "QPushButton#pushButton{\n"
        "    background-color: qlineargradient(spread: pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgb(96, 100, 96), stop:1 rgba(85,98,112,266));\n"
        "    color:rgba(255,255,255,210);\n"
        "    border-radius: 5px;\n"
        "}\n"
        "\n"
        "QPushButton#pushButton:hover{\n"
        "    background-color: qlineargradient(spread:pad, x:0, y1:0.505682, x2:1, y2:0.477, stop: 0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
        "}\n"
        "\n"
        "QPushButton#pushButton:pressed{\n"
        "    padding-left: 5px;\n"
        "    padding-top: 5px;\n"
        "    background-color: rgba(150,123,111,255);\n"
        "}\n"
        "QDialog{\n"
        "    background-color: rgb(234, 239, 255);\n"
        "}")

        self.model = QStandardItemModel()
        for i in dataAllNameCountry['response']:
            country = QStandardItem(i)
            self.model.appendRow(country)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(50, 140, 241, 32))
        palette = QtGui.QPalette()
        self.comboBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setStyleSheet("border: none;\n""")
        self.comboBox.setEditable(True)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox.setIconSize(QtCore.QSize(30, 20))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setModel(self.model)


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(97, 291, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)


        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 215, 80, 30))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_1.clicked.connect(self.clicked_button1)
        self.pushButton_1.setStyleSheet(
        "border-radius: 5px;\n" 
        "border:1px solid;\n"               
        "background-color: rgb(255, 230, 229);\n"
        "color:black;\n"
        "text-align: center;")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 215, 80, 30))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.clicked.connect(self.clicked_button2)
        self.pushButton_2.setStyleSheet(
        "border-radius: 5px;\n"   
        "border:1px solid;\n"              
        "background-color: rgb(255, 230, 229);\n"
        "color:black;\n"
        "text-align: center;")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 241, 22))
        self.lineEdit.setEnabled(False)
        self.lineEdit.setStyleSheet(
        "background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-top: 2px solid rgba(46,82,101,200);\n"
        "color: rgba(0,0,0,240);\n"
        "padding-top: 7px;")
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 91, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 170, 241, 22))
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setStyleSheet(
        "background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-top: 2px solid rgba(46,82,101,200);\n"
        "color: rgba(0,0,0,240);\n"
        "padding-top: 7px;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(360, 70, 821, 301))
        self.label_3.setStyleSheet(
        "background-color: #f8f9fa;\n"
        "border-radius: 10px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 220, 751, 22))
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setStyleSheet(
        "background-color: rgba(0,0,0,0);\n"
        "border:none;\n"
        "border-top: 1px solid #999;\n"
        "color: rgba(0,0,0,240);\n"
        "padding-top: 7px;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(370, 78, 245, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(
        "border-radius: 5px;\n"               
        "background-color: rgb(255, 108, 71);\n"
        "text-align: center;")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(370, 228, 90, 36))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(
        "border-radius: 5px;\n"
        "background-color: rgb(57, 119, 200);\n"
        "color:white;\n"
        "text-align: center;")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(410, 120, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(
            "color: #c9302c;\n"
            )
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(590, 120, 130, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgb(89, 89, 89);")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(960, 120, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgb(11, 152, 47);")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(780, 120, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 171, 25);")
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(370, 190, 61, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(370, 342, 61, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(410, 269, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #c9302c;")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(590, 269, 130, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:rgb(89, 89, 89);")
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(780, 269, 110, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 171, 25);")
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(960, 269, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:rgb(11, 152, 47);")
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(410, 158, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: #c9302c;")
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(410, 190, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 10, 10);")
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(590, 158, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:rgb(89, 89, 89);")
        self.label_18.setObjectName("label_18")

        self.label_19 = QtWidgets.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(780, 158, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 171, 25);")
        self.label_19.setObjectName("label_19")

        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(960, 158, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color:rgb(11, 152, 47);")
        self.label_20.setObjectName("label_20")

        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(590, 190, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(255, 10, 10);")
        self.label_21.setObjectName("label_21")


        self.label_date = QtWidgets.QLabel(Dialog)
        self.label_date.setGeometry(QtCore.QRect(630, 18, 180, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_date.setFont(font)
        self.label_date.setObjectName("label_date")

        self.label_date1 = QtWidgets.QLabel(Dialog)
        self.label_date1.setGeometry(QtCore.QRect(770, 8, 95, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_date1.setStyleSheet(
        "border: 2px solid white;\n"
        "background-color: rgb(79, 200, 255);\n"
        "border-radius: 5px;")
        self.label_date1.setFont(font)
        self.label_date1.setObjectName("label_date")

        self.label_23 = QtWidgets.QLabel(Dialog)
        self.label_23.setGeometry(QtCore.QRect(410, 307, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: #c9302c;")
        self.label_23.setObjectName("label_23")

        self.label_24 = QtWidgets.QLabel(Dialog)
        self.label_24.setGeometry(QtCore.QRect(590, 307, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:rgb(89, 89, 89);")
        self.label_24.setObjectName("label_24")

        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setGeometry(QtCore.QRect(780, 307, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(255, 171, 25);")
        self.label_25.setObjectName("label_25")

        self.label_26 = QtWidgets.QLabel(Dialog)
        self.label_26.setGeometry(QtCore.QRect(960, 307, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:rgb(11, 152, 47);")
        self.label_26.setObjectName("label_26")

        self.label_27 = QtWidgets.QLabel(Dialog)
        self.label_27.setGeometry(QtCore.QRect(410, 339, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(255, 10, 10);")
        self.label_27.setObjectName("label_27")

        self.label_28 = QtWidgets.QLabel(Dialog)
        self.label_28.setGeometry(QtCore.QRect(590, 339, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Yu Gothic UI Semibold")
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(255, 10, 10);")
        self.label_28.setObjectName("label_28")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.isThreadDataRun = False
        self.isThreadTimerRun = False

        timerThreadRunWhenAppRun = threading.Thread(target = self.runThreadTimer, daemon=True)  
        timerThreadRunWhenAppRun.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Select"))
        self.pushButton_1.setText(_translate("Dialog", "Start"))
        self.pushButton_2.setText(_translate("Dialog", "End"))
        self.label.setText(_translate("Dialog", "COVID-19  Tracker"))
        self.label_2.setText(_translate("Dialog", "Select Country"))
        
        self.label_5.setText(_translate("Dialog", "  World"))
        self.label_6.setText(_translate("Dialog", "TOTAL CASE"))
        self.label_7.setText(_translate("Dialog", "TOTAL DEATHS"))
        self.label_8.setText(_translate("Dialog", "TOTAL RECOVERED"))
        self.label_9.setText(_translate("Dialog", "ACTIVE CASE"))
        self.label_10.setText(_translate("Dialog", "New"))
        self.label_11.setText(_translate("Dialog", "New"))
        self.label_12.setText(_translate("Dialog", "TOTAL CASE"))
        self.label_13.setText(_translate("Dialog", "TOTAL DEATHS"))
        self.label_14.setText(_translate("Dialog", "ACTIVE CASE"))
        self.label_15.setText(_translate("Dialog", "TOTAL RECOVERED"))

        day = str(today.day) + "-" + str(today.month) + "-" + str(today.year) 
        dayInWeek = datetime.today().strftime('%a');
        self.label_date.setText(_translate("Dialog",dayInWeek.upper() + "  " +  day))
        
        self.dataAllWorld()

        

    def checkNone(self,Str):
        strr = str(Str)
        if strr == "None":
            strr = "0"
        else:
            checkDataIsNewCase = ""
            caseString = ""
            thousandPoint = 3
            milionPoint = 6
            bilionPoint = 9
            thousandBilionPoint = 12
            milionBilionPoint = 15
            if(strr[0] == "+"):
                checkDataIsNewCase = strr[0]
                strr = strr[1:]
            strrReverse = strr[::-1]
            for i in range(len(strrReverse)):
                if(i == thousandPoint or i == milionPoint or i == bilionPoint or i == thousandBilionPoint or i == milionBilionPoint):
                    caseString += ("." + strrReverse[i] ) 
                else:
                    caseString += strrReverse[i]
            if(checkDataIsNewCase == "+"):
                strr = "+" + caseString[::-1]
            else:
                strr = caseString[::-1]
        return strr        

    def clicked(self):
        self.comboBox.currentText()
        self.selectData(self.comboBox.currentText())
        getChartCountry(self.comboBox.currentText())


    def runThreadData(self):
        self.isThreadDataRun = True
        while(self.isThreadDataRun):
            self.comboBox.currentText()
            self.selectData(self.comboBox.currentText())
            minutes = 15
            seconds = 60
            time.sleep(minutes*seconds)

    def runThreadTimer(self):
        self.isThreadTimerRun = True
        _translate = QtCore.QCoreApplication.translate
        while(self.isThreadTimerRun):
            currentTime = datetime.now()
            time1 = currentTime.strftime("%H:%M:%S")
            self.label_date1.setText(_translate("Dialog","  " + time1))
            time.sleep(0.93)        

    def clicked_button1(self):
        dataThreadRunWhenClickButton = threading.Thread(target = self.runThreadData, daemon=True)
        dataThreadRunWhenClickButton.start()


    def clicked_button2(self):  
        self.isThreadDataRun = False  


    def selectData(self, input_country):
        url = "https://covid-193.p.rapidapi.com/statistics?country="
        headers = {
            'x-rapidapi-key': "c0dced8bb9mshbc64e8fcf6cc50ap124d32jsn54f979df4709",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"}

        response = requests.request("GET", url + input_country, headers=headers)
        dataOfSelectCountry = response.json()
        self.getDataCountry(dataOfSelectCountry) 


    def getDataCountry(self,dataAllNameCountry):
        _translate = QtCore.QCoreApplication.translate
        for c in dataAllNameCountry['response']:
            self.label_4.setText(_translate("Dialog", "  " + c['country']))    
            self.label_16.setText(_translate("Dialog", self.checkNone(c['cases']['total'])))
            self.label_18.setText(_translate("Dialog", self.checkNone(c['deaths']['total'])))
            self.label_19.setText(_translate("Dialog", self.checkNone(c['cases']['active'])))
            self.label_20.setText(_translate("Dialog", self.checkNone(c['cases']['recovered'])))
            self.label_17.setText(_translate("Dialog", self.checkNone(c['cases']['new'])))
            self.label_21.setText(_translate("Dialog", self.checkNone(c['deaths']['new'])))
            

    def dataAllWorld(self):
        _translate = QtCore.QCoreApplication.translate
        for c in dataTotalCaseAllWorld['response']:
            self.label_23.setText(_translate("Dialog", self.checkNone(c['cases']['total'])))
            self.label_24.setText(_translate("Dialog", self.checkNone(c['deaths']['total'])))
            self.label_25.setText(_translate("Dialog", self.checkNone(c['cases']['active'])))
            self.label_26.setText(_translate("Dialog", self.checkNone(c['cases']['recovered'])))
            self.label_27.setText(_translate("Dialog", self.checkNone(c['cases']['new'])))
            self.label_28.setText(_translate("Dialog", self.checkNone(c['deaths']['new'])))        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

