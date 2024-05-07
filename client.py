from PySide6.QtCore import QDateTime
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtNetwork import QTcpSocket
import sys
import re

from cryption import decrypt, encrypt, check_key

from interface import Ui_MainWindow


class Client(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Client, self).__init__()
        self.setupUi(self)

        # # Инициализируем поля ввода
        # self.ui.ipAddressLineEdit.setText("localhost")  # IP-адрес по умолчанию
        # self.ui.portLineEdit.setText("9999")            # Порт по умолчанию
        # self.ui.keyLineEdit.setText("easykey")          # Ключ по умолчанию
        # self.ui.nameLineEdit.setText("Guest")           # Имя пользователя по умолчанию
        self.client_name = ''
        # Скрываем группы, которые должны быть видимы только после подключения
        # self.chatGroupBox.setVisible(False)
        self.serverConnectionGroupBox.setVisible(True)

        # Подключаем обработчики событий
        self.serverConnectionButton.clicked.connect(self.connect_to_server)
        self.sendButton.clicked.connect(self.send_message)
        self.disconnectButton.clicked.connect(self.disconnect_from_server)

        # Создаем сокет для сетевого взаимодействия
        self.socket = QTcpSocket(self)
        self.socket.readyRead.connect(self.on_ready_read)
        self.socket.disconnected.connect(self.on_disconnected)

    def connect_to_server(self):
        ip = self.ipAddressLineEdit.text()
        port = int(self.portLineEdit.text())

        self.socket.connectToHost(ip, port)
        if self.socket.waitForConnected(5000):
            self.client_name = self.nameLineEdit.text() if self.nameLineEdit.text() else 'guest'
            # Показываем чат после подключения
            self.chatGroupBox.setVisible(True)
            self.serverConnectionGroupBox.setVisible(False)
        else:
            self.statusLabel.setText("Failed to connect to the server.")

    # def send_message(self):
    #     message = self.messageLineEdit.text()
    #     if message:
    #         self.hangle_server_message(f"{self.client_name}: {message}\n".encode())
    #         self.messageLineEdit.clear()

    def disconnect_from_server(self):
        self.socket.disconnectFromHost()
        # Показываем группу подключения после отключения
        self.chatGroupBox.setVisible(False)
        self.serverConnectionGroupBox.setVisible(True)

    def on_ready_read(self):
        # Читаем данные из сокета
        data = self.socket.readAll().data().decode()

        # Регулярное выражение для поиска даты, имени клиента и сообщения
        pattern = r"\[(.*?)\] (.*?): (.*)"

        # Используем функцию re.search для поиска совпадений
        match = re.search(pattern, data)

        if match:
            # Дата
            date_time = match.group(1)
            # Имя клиента
            client_name = match.group(2)
            # Сообщение
            message = match.group(3)
        else:
            self.handle_server_message('Не удалось расшифровать сообщение')

        key = check_key()
        if key == "0":
            self.chatTextEdit.text = 'Неправильно задан ключ'
            self.socket.write('Неправильно задан ключ'.encode())
            return

        # Получаем текст из поля ввода сообщения и raZшифровываем
        message = decrypt(message, key)

        if not message:
            message = '#Неправильный ключ для расшифровки сообщения#'

        # Обрабатываем полученные данные
        self.handle_server_message(f"[{date_time}] {client_name}: {message}")

    def send_message(self):
        # Получаем ключ из поля ввода ключа
        key = check_key()
        if key == "0":
            self.chatTextEdit.text = 'Неправильно задан ключ'
            self.socket.write('Неправильно задан ключ'.encode())
            return
        # Получаем текст из поля ввода сообщения
        message = encrypt(self.messageLineEdit.text(), key)
        if not message:
            return
        # Получаем текущее время и имя клиента
        date_time = QDateTime.currentDateTime().toString('dd.MM.yyyy hh:mm:ss')

        # Формируем сообщение с датой, именем клиента и зашифрованным текстом
        encrypted_message = f"[{date_time}] {self.client_name}: {message}"

        # Отправляем зашифрованное сообщение на сервер
        self.socket.write(encrypted_message.encode())

        # Очищаем поле ввода сообщения
        self.messageLineEdit.clear()

    def on_disconnected(self):
        self.statusLabel.setText("Disconnected from the server.")
        self.chatGroupBox.setVisible(False)
        self.serverConnectionGroupBox.setVisible(True)

    def handle_server_message(self, message):
        self.chatTextEdit.append(message)

# Основная часть программы
app = QApplication([])
client = Client()
client.show()
sys.exit(app.exec())