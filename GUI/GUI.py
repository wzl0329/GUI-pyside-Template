# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(484, 392)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 130, 75, 24))
        self.getInputpwd = QLineEdit(Form)
        self.getInputpwd.setObjectName(u"getInputpwd")
        self.getInputpwd.setGeometry(QRect(320, 80, 113, 20))
        self.mylabel = QLabel(Form)
        self.mylabel.setObjectName(u"mylabel")
        self.mylabel.setGeometry(QRect(60, 10, 131, 61))
        self.mylabel.setLayoutDirection(Qt.LeftToRight)
        self.mylabel.setAlignment(Qt.AlignCenter)
        self.getmyNum = QSpinBox(Form)
        self.getmyNum.setObjectName(u"getmyNum")
        self.getmyNum.setGeometry(QRect(20, 30, 41, 21))
        self.getmyNum.setValue(2)
        self.showMSG = QTextBrowser(Form)
        self.showMSG.setObjectName(u"showMSG")
        self.showMSG.setGeometry(QRect(50, 100, 256, 192))
        self.mychoose = QComboBox(Form)
        self.mychoose.setObjectName(u"mychoose")
        self.mychoose.setGeometry(QRect(190, 30, 68, 22))
        self.showProgress = QProgressBar(Form)
        self.showProgress.setObjectName(u"showProgress")
        self.showProgress.setGeometry(QRect(120, 320, 118, 23))
        self.showProgress.setValue(24)
        self.showProgress.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.radioButton = QRadioButton(Form)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(330, 180, 95, 20))
        self.radioButton_2 = QRadioButton(Form)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(330, 210, 95, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.getInputpwd.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u6388\u6743\u7801", None))
        self.mylabel.setText(QCoreApplication.translate("Form", u"\u8fd9\u662f\u4e00\u4e2a\u6807\u7b7e", None))
        self.showMSG.setPlaceholderText(QCoreApplication.translate("Form", u"showMSG", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"RadioButton", None))
    # retranslateUi

