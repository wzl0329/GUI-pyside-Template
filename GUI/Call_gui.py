import os
import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot, QObject, SignalInstance, Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QFileDialog

from GUI import Ui_Form


class CustomSignal(QObject):  # 自定义一个信号类
    on_progress_value_change: SignalInstance = Signal(int)  # 自定义一个事件，底层是c++，所以严格的写参数类型


customSignal = CustomSignal()  # 创建一个全局变量 自定义信号类实例


class MyWindow(QtWidgets.QWidget, Ui_Form):  # 继承QMainWindow
    def __init__(self):
        super().__init__()
        # 在此创建窗体上的部件
        self.setupUi(self)
        # 下拉框的设置方式
        self.mychoose.addItems(['1', '2', "3"])
        self.mychoose.addItem("second")
        self.buttonGroup.buttonClicked.connect(self.afterclick)  # 按钮组没有槽函数
        # self.pushButton.clicked.connect(self.onBTNClick)
        self.clipboard = QGuiApplication.clipboard()  # 创建剪切板
        # 信号槽的初始化
        self.showProgress.reset()  # 全清除
        self.showProgress.setRange(0, 100)  # 设置进度条范围
        # 将on_progress_value_change事件信号和自定义函数相关联
        customSignal.on_progress_value_change.connect(self.setProgressValue)
        self.value = 0

    # 单选按钮组的函数
    def afterclick(self):
        btn = self.buttonGroup.checkedButton()
        print(btn.text())

    # 利用connect的点击
    # def onBTNClick(self):
    #     print('onBTN')

    def setProgressValue(self, value: int):
        """
        设置progress的值
        :param value:
        :return:
        """
        self.showProgress.setValue(value)

    #  推荐@Slot()
    @Slot()
    def on_pushButton_clicked(self):
        print('on_pushButton')

        # 单行文本框line文本设置
        # self.getInputpwd.setText("我们设置文本为")
        # self.getInputpwd.clear()  # 文本清除
        getText = self.getInputpwd.text()
        self.clipboard.setText(getText)  # 为剪切板设置文本
        print(self.clipboard.text())
        """
        """

        # 标签文本
        self.mylabel.setText("标签变了")

        # Num选择框
        # getNum = self.getmyNum.value()
        # print(getNum, f"{type(getNum)}")
        self.getmyNum.setValue(20)

        # 按钮文本及不响应
        self.pushButton.setText("改变了")
        #  self.pushButton.setEnabled(False)  # 不响应

        # 消息框设置文本
        # self.showMSG.toPlainText() # 获取文本
        # self.showMSG.setText() # 设置文本
        self.showMSG.append("1")
        self.showMSG.ensureCursorVisible()  # 光标到最新的地方

        # 复选框
        # getchoose = self.mychoose.currentText()
        # print(getchoose)
        # self.mychoose.clear() # 将复选框清除

        # 进度条清零
        # self.showProgress.reset()  # 全清除
        # self.showProgress.setRange(0, 0)  # 设置进度条范围
        # self.showProgress.setValue(46)  # 设置具体值

        # 打印风格 ['Windows', 'Fusion']
        print(QtWidgets.QStyleFactory.keys())

        # 单选框 不实时获取
        isC = self.radioButton.isChecked()
        isC2 = self.radioButton_2.isChecked()
        print('raido_1', isC)  # True和False
        print('raido_1', isC2)
        # 复选框和单选框使用一致

        # 点击按钮选择文件
        # flie_dir,filter_ = QFileDialog.getOpenFileName(self,caption="选择你需要的py文件",dir=os.getcwd(),filter="选择python文件(*.py)")
        # caption是提示,os.getcwd()获取当前文件路径，filter过滤器
        # print(f"文件路径为{flie_dir}",f"过滤器为{filter_}")
        # save_flie_dir, _ = QFileDialog.getSaveFileName(self, caption="保存py文件", dir=os.getcwd(), filter="保存python文件(*.py)")
        # 返回参数和上面一致
        flie_dir, _ = QFileDialog.getOpenFileNames(self, caption="选择你需要的py文件", dir=os.getcwd(),
                                                   filter="选择python文件(*.py)")
        # 选择多个文件，filename是文件路径列表
        # r'G:\研究生项目文件\电镀工艺\小批多镀线\diandu_start\data' 用r保持原有意思

        self.value += 5
        # 后台发送信号
        customSignal.on_progress_value_change.emit(self.value)

    @Slot()
    def on_getmyNum_valueChanged(self):
        getNum = self.getmyNum.value()
        print(getNum, f"{type(getNum)}")

    @Slot()
    def on_getInputpwd_textChanged(self):
        getText = self.getInputpwd.text()
        print('on_pwd_changed')
        print(f"文本是：{getText}")

    @Slot()  # 复选框
    def on_mychoose_currentTextChanged(self):
        print(self.mychoose.currentText())


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle(QtWidgets.QStyleFactory.create('windowvista'))
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    view = MyWindow()
    view.show()
    sys.exit(app.exec())
