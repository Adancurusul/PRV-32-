from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QByteArray, QDataStream
import datetime

PORT = 8080
SIZEOF_UINT16 = 2


def robust(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except Exception as e:
            print('Error execute: %s \nException: %s' % (actual_do.__name__, e))

    return add_robust


class Ui_Form(object):
    def setupUi(self, Form: QtWidgets.QWidget):
        Form.setObjectName("Form")

        self.bwr = QtWidgets.QTextBrowser()
        self.btnSend = QtWidgets.QPushButton()
        self.btnSend.setObjectName("btnSend")

        self.btnOpen = QtWidgets.QPushButton()
        self.btnOpen.setObjectName("btnOpen")

        self.lb_psbar = QtWidgets.QLabel()
        self.psbar = QtWidgets.QProgressBar()

        self.layer_1 = QtWidgets.QHBoxLayout()
        self.layer_1.addWidget(self.lb_psbar)
        self.layer_1.addWidget(self.psbar)

        self.layer_2 = QtWidgets.QHBoxLayout()
        self.layer_2.addWidget(self.btnOpen)
        # self.layer_2.addWidget(self.btnSend)

        self.layer_0 = QtWidgets.QVBoxLayout()
        self.layer_0.addWidget(self.bwr)
        self.layer_0.addLayout(self.layer_1)
        self.layer_0.addLayout(self.layer_2)

        Form.setLayout(self.layer_0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)  # 需要定义控件的setObjectName

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "JTTAG"))
        self.lb_psbar.setText(_translate("Form", "进度"))
        self.btnOpen.setText(_translate("Form", "open"))
        # self.btnSend.setText(_translate("Fomr", "Send"))


class Server(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Server, self).__init__(parent)
        self.setupUi(self)
        self.psbar.hide()

        self.socket = QtNetwork.QTcpSocket()

    @pyqtSlot()
    def on_btnOpen_clicked(self):
        self.server = QtNetwork.QTcpServer()
        self.server.listen(QtNetwork.QHostAddress("0.0.0.0"), PORT)
        self.server.setObjectName("server")
        self.server.newConnection.connect(self.on_server_newConnection)

        self.totalsize = 0
        self.bytereceived = 0
        self.filename = ""
        self.inblock = QByteArray()

        self.on_bwr_update("open server begin receiving")

    def on_bwr_update(self, tmp_log):
        current_time = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        self.bwr.append("%s  %s" % (current_time, tmp_log))

    # @pyqtSlot()
    def on_server_newConnection(self):
        self.on_bwr_update("connected jttag")
        self.socket = self.server.nextPendingConnection()
        self.socket.setObjectName("socket")
        self.socket.write(b'hello')

        self.socket.readyRead.connect(self.on_socket_readyRead)

    # @pyqtSlot()
    @robust
    def on_socket_readyRead(self):
        self.inblock = self.socket.readAll()
        self.inblock = str(self.inblock)[2:-1]
        self.on_bwr_update(self.inblock)
        '''

        if self.bytereceived == 0:
            self.on_bwr_update("receiving...")
            self.psbar.setValue(0)

            recv = QDataStream(self.socket)



            self.totalsize = recv.readInt64()
            self.bytereceived = recv.readInt64()

            self.filename = recv.readQString()
            self.on_bwr_update(self.filename)
            self.filename = "Download/" + self.filename
            self.new_file = QtCore.QFile(self.filename)
            self.new_file.open(QtCore.QFile.WriteOnly)

        else:
            self.inblock = self.socket.readAll()
            self.on_bwr_update(self.inblock)
            
            self.bytereceived += self.inblock.size()
            self.new_file.write(self.inblock)
            self.new_file.flush()
            

        self.psbar.show()
        self.psbar.setMaximum(self.totalsize)
        self.psbar.setValue(self.bytereceived)
        if self.bytereceived == self.totalsize:
            self.on_bwr_update("[completed] received!!!")
            self.new_file.close()  # 接受完成关闭文件
            self.end_recv()  # 接受完毕初始化文件信息
            self.inblock.clear()  # 清空接受缓存
        '''

    def end_recv(self):
        self.totalsize = 0
        self.bytereceived = 0
        self.filename = ""


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlg = Server()
    dlg.show()
    sys.exit(app.exec_())
