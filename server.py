import sys
from PySide6.QtCore import QCoreApplication, QObject, Slot
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress


class Server(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.server = QTcpServer(self)
        self.clients = []

        if not self.server.listen(QHostAddress.Any, 9090):
            print("Unable to start the server:", self.server.errorString())
            return
        print(f"Сервер слушается на {self.server.serverPort()}")
        self.server.newConnection.connect(self.on_new_connection)

    @Slot()
    def on_new_connection(self):
        client_socket = self.server.nextPendingConnection()
        client_socket.readyRead.connect(lambda: self.on_ready_read(client_socket))
        client_socket.disconnected.connect(lambda: self.on_disconnected(client_socket))
        self.clients.append(client_socket)
        print("Новое подключение.")

    @Slot()
    def on_ready_read(self, client_socket):
        data = client_socket.readAll().data().decode()
        print(f"Получено от клиента: {data}")
        self.broadcast_message(data) # отправляем сообщение всем клиентам

    @Slot()
    def on_disconnected(self, client_socket):
        self.clients.remove(client_socket) #удаляем сокет клиента из массив чтобы к нему не доходили сообщение
        client_socket.deleteLater()
        print("Пользователь отключился.")

    def broadcast_message(self, message):
        for client in self.clients:
            client.write(message.encode())
            client.flush()


app = QCoreApplication(sys.argv)
server = Server()
sys.exit(app.exec())