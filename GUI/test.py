from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton

app = QApplication()               # 实例化一个应用

window = QMainWindow()             # 实例化一个主窗口
window.resize(500, 400)            # 设置窗口大小
window.move(300, 310)              # 移动窗口距离屏幕左上角的位置。
window.setWindowTitle('这是标题')    # 设置窗口标题。

textEdit = QPlainTextEdit(window)              # 在主窗口中添加一个文本框。
textEdit.setPlaceholderText('默认输入内容……')     # 设置文本框内的默认内容。
textEdit.move(10, 25)
textEdit.resize(300, 350)

button = QPushButton('按钮', window)          # 在主窗口中添加一个按钮
button.move(350, 50)
button.clicked.connect(lambda x: print('点击了按钮'))  # 给按钮绑定调用函数。

window.show()       # 显示窗口

app.exec()         # 使窗口保持显示状态。
