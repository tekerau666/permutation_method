# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(630, 503)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.chatGroupBox = QGroupBox(self.centralwidget)
        self.chatGroupBox.setObjectName(u"chatGroupBox")
        self.chatGroupBox.setEnabled(True)
        self.chatGroupBox.setGeometry(QRect(10, 0, 601, 431))
        self.chatTextEdit = QTextEdit(self.chatGroupBox)
        self.chatTextEdit.setObjectName(u"chatTextEdit")
        self.chatTextEdit.setGeometry(QRect(10, 50, 551, 231))
        self.chatTextEdit.setReadOnly(True)
        self.sendButton = QPushButton(self.chatGroupBox)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(10, 380, 91, 41))
        self.messageLineEdit = QLineEdit(self.chatGroupBox)
        self.messageLineEdit.setObjectName(u"messageLineEdit")
        self.messageLineEdit.setGeometry(QRect(10, 320, 551, 31))
        self.disconnectButton = QPushButton(self.chatGroupBox)
        self.disconnectButton.setObjectName(u"disconnectButton")
        self.disconnectButton.setGeometry(QRect(470, 380, 91, 41))
        self.serverConnectionGroupBox = QGroupBox(self.centralwidget)
        self.serverConnectionGroupBox.setObjectName(u"serverConnectionGroupBox")
        self.serverConnectionGroupBox.setGeometry(QRect(180, 80, 241, 181))
        self.label_3 = QLabel(self.serverConnectionGroupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 85, 32, 16))
        self.nameLineEdit = QLineEdit(self.serverConnectionGroupBox)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(71, 85, 133, 22))
        self.label_2 = QLabel(self.serverConnectionGroupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 56, 22, 16))
        self.serverConnectionButton = QPushButton(self.serverConnectionGroupBox)
        self.serverConnectionButton.setObjectName(u"serverConnectionButton")
        self.serverConnectionButton.setGeometry(QRect(71, 114, 90, 24))
        self.label = QLabel(self.serverConnectionGroupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 27, 55, 16))
        self.portLineEdit = QLineEdit(self.serverConnectionGroupBox)
        self.portLineEdit.setObjectName(u"portLineEdit")
        self.portLineEdit.setGeometry(QRect(71, 56, 133, 22))
        self.ipAddressLineEdit = QLineEdit(self.serverConnectionGroupBox)
        self.ipAddressLineEdit.setObjectName(u"ipAddressLineEdit")
        self.ipAddressLineEdit.setGeometry(QRect(71, 27, 133, 22))
        self.label_4 = QLabel(self.serverConnectionGroupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 150, 49, 16))
        self.statusLabel = QLabel(self.serverConnectionGroupBox)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(60, 150, 171, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 630, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.chatGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.chatTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f \u0431\u0443\u0434\u0443 \u0437\u0434\u0435\u0441\u044c", None))
        self.sendButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.messageLineEdit.setText("")
        self.messageLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0432\u0432\u043e\u0434\u0438 \u0441\u044e\u0434\u0430", None))
        self.disconnectButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.serverConnectionGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Enter", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.serverConnectionButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.statusLabel.setText("")
    # retranslateUi

