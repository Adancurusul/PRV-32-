from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QByteArray, QDataStream
import datetime
import time

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
        self.lb_speed = QtWidgets.QLabel()
        self.psbar = QtWidgets.QProgressBar()

        self.layer_1 = QtWidgets.QHBoxLayout()
        self.layer_1.addWidget(self.lb_psbar)
        self.layer_1.addWidget(self.psbar)
        self.layer_1.addWidget(self.lb_speed)

        self.layer_2 = QtWidgets.QHBoxLayout()
        self.layer_2.addWidget(self.btnOpen)
        self.layer_2.addWidget(self.btnSend)

        self.layer_0 = QtWidgets.QVBoxLayout()
        self.layer_0.addWidget(self.bwr)
        self.layer_0.addLayout(self.layer_1)
        self.layer_0.addLayout(self.layer_2)

        Form.setLayout(self.layer_0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)  # 需要定义控件的setObjectName

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lb_psbar.setText(_translate("Form", "进度"))
        self.lb_speed.setText(_translate("Form", "speed"))
        self.btnOpen.setText(_translate("Form", "open"))
        self.btnSend.setText(_translate("Fomr", "Send"))


class Client(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Client, self).__init__(parent)
        self.setupUi(self)

        self.psbar.hide()

        self.socket = QtNetwork.QTcpSocket()
        self.socket.setObjectName("socket")

        # self.socket.readyRead.connect(self.readResponse)
        self.socket.connectToHost("192.168.1.150", PORT)
        self.socket.bytesWritten.connect(self.on_server_bytesWritten)

        self.filename = ""
        self.outblock = QByteArray()

    @pyqtSlot()
    def on_socket_readyRead(self):
        pass

    @robust
    @pyqtSlot()
    def on_btnOpen_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet

        # 初始化文件信息
        self.loadsize = 0
        self.byte2write = 0
        self.totalsize = 0
        # self.outblock.clear()

        self.filename = QtWidgets.QFileDialog().getOpenFileName(self)[0]

        self.localfile = QtCore.QFile(self.filename)
        self.localfile.open(QtCore.QFile.ReadOnly)

        tmp_log = "[open file]  %s[sucessed]" % self.filename
        self.sock.write("hello")

        self.on_bwr_update(tmp_log)

    def on_bwr_update(self, tmp_log):
        current_time = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        self.bwr.append("%s  %s" % (current_time, tmp_log))

    @pyqtSlot()
    def on_btnSend_clicked(self):
        self.send()
        self.old_time = time.time()
        self.start_time = time.time()
        self.bitch_send_bytes = 0

    def send(self):
        self.byte2write = self.localfile.size()
        self.totalsize = self.localfile.size()

        self.loadsize = 4 * 1024

        out = QDataStream(self.outblock, QtCore.QIODevice.WriteOnly)
        current_filename = self.filename.split("/")[-1]

        out.writeInt64(0)
        out.writeInt64(0)

        self.totalsize += self.outblock.size()
        self.byte2write += self.outblock.size()

        out.writeQString(current_filename)
        out.device().seek(0)
        out.writeInt64(self.totalsize)
        out.writeInt64(self.outblock.size())

        self.socket.write(self.outblock)

        self.psbar.show()
        self.psbar.setMaximum(self.totalsize)
        self.psbar.setValue(self.totalsize - self.byte2write)

    def on_server_bytesWritten(self, num_bytes):
        self.byte2write -= num_bytes
        self.outblock = self.localfile.read(min(self.byte2write, self.loadsize))
        self.socket.write(self.outblock)
        self.psbar.setMaximum(self.totalsize)
        self.psbar.setValue(self.totalsize - self.byte2write)

        self.bitch_send_bytes += num_bytes
        self.now_time = time.time()
        if self.now_time - self.old_time >= 1:
            speed = self.bitch_send_bytes / (self.now_time - self.old_time) / 1024
            self.bitch_send_bytes = 0
            speed = speed / 1024
            self.old_time = self.now_time

            self.lb_speed.setText("%0.2f M/s" % (speed))

        if self.byte2write == 0:
            self.outblock = QByteArray()
            self.on_bwr_update("completed!!![sucessed]")
            print("spent time : %f" % (time.time() - self.start_time))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dlg = Client()
    dlg.show()
    sys.exit(app.exec_())
