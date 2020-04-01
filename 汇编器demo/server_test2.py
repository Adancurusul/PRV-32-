import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)

        #垂直布局
        layout=QVBoxLayout()

        #创建按钮1
        self.btn1=QPushButton('Button1')
        #setCheckable()：设置按钮是否已经被选中，如果为True，则表示按钮将保持已点击和释放状态
        self.btn1.setCheckable(True)
        #toggle()：在按钮状态之间进行切换
        self.btn1.toggle()
        #点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
        self.btn1.clicked.connect(lambda :self.whichbtn(self.btn1))
        #点击信号与槽函数进行连接，实现的目的：输入安妞的当前状态，按下还是释放
        self.btn1.clicked.connect(self.btnstate)

        #添加控件到布局中
        layout.addWidget(self.btn1)

        #创建按钮2
        self.btn2=QPushButton('image')
        #为按钮2添加图标
        self.btn2.setIcon(QIcon(QPixmap('E:\pyqt5快速开发与实战\第四章\images\python.png')))
        ##点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
        self.btn2.clicked.connect(lambda :self.whichbtn(self.btn2))

        layout.addWidget(self.btn2)

        self.btn3=QPushButton('Disabled')
        #setEnabled()设置按钮是否可以使用，当设置为False的时候，按钮变成不可用状态，点击它不会发射信号
        self.btn3.setEnabled(False)

        layout.addWidget(self.btn3)

        #创建按钮并添加快捷键
        self.btn4=QPushButton('&Download')
        #setDefault()：设置按钮的默认状态
        self.btn4.setDefault(True)
        ##点击信号与槽函数进行连接，这一步实现：在控制台输出被点击的按钮
        self.btn4.clicked.connect(lambda :self.whichbtn(self.btn4))

        layout.addWidget(self.btn4)

        self.setWindowTitle("Button demo")
        self.setLayout(layout)

    def btnstate(self):
        #isChecked()：判断按钮的状态，返回值为True或False
        if self.btn1.isChecked():
            print('button pressed')
        else:
            print('button released')

    def whichbtn(self,btn):
        #输出被点击的按钮
        print('clicked button is '+btn.text())
if __name__ == '__main__':
    app=QApplication(sys.argv)
    btnDemo=Form()
    btnDemo.show()
    sys.exit(app.exec_())
