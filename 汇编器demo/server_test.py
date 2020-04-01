from PyQt5.QtWidgets import \
    QWidget, QMainWindow, QAction, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QMessageBox, QApplication
from PyQt5.QtGui import QTextCursor, QIcon
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    server_chinese_encoding = 'gbk'

    def __init__(self):
        QWidget.__init__(self)

        self.sock = None
        self.isConnectedToServer = False

        self.textEdit = None
        self.lineEdit = None
        self.pushButton = None
        self.vBox = None

        self._create_widgets()

    def _create_widgets(self):
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        p = self.textEdit.viewport().palette()
        p.setColor(self.textEdit.viewport().backgroundRole(), Qt.transparent)
        self.textEdit.viewport().setPalette(p)

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Enter message")
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setEnabled(False)

        self.pushButton = QPushButton("Send")
        self.pushButton.setEnabled(False)

        self.vBox = QVBoxLayout(self)
        self.vBox.addWidget(self.textEdit)
        self.vBox.addWidget(self.lineEdit)
        self.vBox.addWidget(self.pushButton)
        self.setLayout(self.vBox)

        self.pushButton.released.connect(self.push_button_event)

    def add_message(self, message):
        self.textEdit.moveCursor(QTextCursor.End)
        self.textEdit.insertPlainText(message)
        self.textEdit.moveCursor(QTextCursor.End)

    def connect(self):
        if self.isConnectedToServer:
            return True

        self.sock = QTcpSocket(self)
        host_ip_addr = '192.168.1.150'
        port = 8080
        self.sock.connectToHost(host_ip_addr, port)

        if not self.sock.waitForConnected(2500):
            msg = self.sock.errorString()
            self.add_message(msg + '\n')
            QMessageBox.critical(self, "Error", msg)
            return False

        self.sock.connected.connect(self.on_socket_connected)
        self.sock.disconnected.connect(self.on_socket_disconnected)
        self.sock.readyRead.connect(self.on_socket_receive)
        self.sock.bytesWritten.connect(self.on_socket_transmit)

        self.add_message("Connected to {} on port {}\n".format(host_ip_addr, port))

        self.isConnectedToServer = True
        self.lineEdit.setEnabled(True)
        self.pushButton.setEnabled(True)

        return True

    def push_button_event(self):
        txString = self.lineEdit.text()
        #self.sock.write('hello my friend')

        if self.isConnectedToServer and len(txString) > 0:
            self.sock.write(txString.encode(self.server_chinese_encoding))
            self.add_message("Wrote '" + txString + "'")
        else:
            self.add_message("You must enter a message\n")
            QMessageBox.critical(self, "Error", "You must enter a message")

    def on_socket_connected(self):
        pass

    def on_socket_disconnected(self):
        self.add_message("Disconnected from server\n")
        self.lineEdit.setEnabled(False)
        self.pushButton.setEnabled(False)

    def on_socket_receive(self):
        rxData = self.sock.readAll()
        self.add_message("Received '" + rxData.data().decode(self.server_chinese_encoding) + "'\n")

    def on_socket_transmit(self, numBytes):
        self.add_message(" (" + str(numBytes) + " bytes)\n")

    # noinspection PyBroadException
    def disconnect(self):
        if not self.isConnectedToServer:
            return
        try:
            self.sock.connected.disconncet()
        except:
            pass
        try:
            self.sock.disconnected.disconncet()
        except:
            pass
        try:
            self.sock.readyRead.disconncet()
        except:
            pass
        try:
            self.sock.bytesWritten.disconncet()
        except:
            pass
        self.sock.close()
        self.lineEdit.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.isConnectedToServer = False


def resource_path(relative_path):
    import os.path

    return os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.btnConnect = None
        self.btnDisconnect = None
        self._create_toolbar()

        self.client = None
        self._create_widgets()

    def _create_toolbar(self):
        self.btnConnect = QAction(QIcon(resource_path('connect.png')), 'Connect')
        self.btnDisconnect = QAction(QIcon(resource_path('disconnect.png')), 'Disconnect')

        self.btnConnect.setEnabled(True)
        self.btnDisconnect.setEnabled(False)

        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction(self.btnConnect)
        toolbar.addAction(self.btnDisconnect)

        self.btnConnect.triggered.connect(self.on_tcp_connect)
        self.btnDisconnect.triggered.connect(self.on_tcp_disconnect)

    def _create_widgets(self):
        self.client = MyWidget()

        self.setCentralWidget(self.client)

    def on_tcp_connect(self):
        status = self.client.connect()

        if status:
            self.btnConnect.setEnabled(False)
            self.btnDisconnect.setEnabled(True)

    def on_tcp_disconnect(self):
        self.client.disconnect()

        self.btnConnect.setEnabled(True)
        self.btnDisconnect.setEnabled(False)


if __name__ == '__main__':
    import sys

    # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    # logging.debug('This is a log message.')
    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    mainWindow.resize(320, 320)
    mainWindow.setWindowTitle('PyQt5-Socket-Client')
    # mainWindow.setWindowIcon(QIcon(resource_path('window.png')))
    mainWindow.show()

    sys.exit(app.exec_())

