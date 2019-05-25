from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets   
import mysql.connector
from PyQt5.QtCore import QTimer

authorized = True #ИЗМЕНИТЬ НА FALSE

user_id = 2

try:
    cnx = mysql.connector.connect(user='root', password='i130813',
                                  host='127.0.0.1',
                                  database='maindb')

    cursor = cnx.cursor(buffered=True)
    bcursor = cnx.cursor(buffered=True)
    ccursor = cnx.cursor(buffered=True)

except BaseException as e:
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    msgbox = QtWidgets.QMessageBox()
    msgbox.setWindowTitle("Ошибка соединения с базой данных")
    msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/x.png')))
    msgbox.setText('Проверьте подключение к Базе Данных')
    msgbox.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
    msgbox.setDetailedText(str(e))
    msgbox.exec()

playlist = QtMultimedia.QMediaPlaylist()
playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)

player = QtMultimedia.QMediaPlayer()
player.setPlaylist(playlist)


class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 289))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 5)
        self.profilebutton = QtWidgets.QPushButton(self.centralwidget)
        self.profilebutton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.profilebutton.setObjectName("profilebutton")
        self.gridLayout.addWidget(self.profilebutton, 0, 0, 1, 1)
        self.basketbutton = QtWidgets.QPushButton(self.centralwidget)
        self.basketbutton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.basketbutton.setObjectName("basketbutton")
        self.gridLayout.addWidget(self.basketbutton, 0, 4, 1, 1)
        self.beatsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.beatsbutton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.beatsbutton.setObjectName("beatsbutton")
        self.gridLayout.addWidget(self.beatsbutton, 0, 2, 1, 1)
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.searchbutton.setObjectName("searchbutton")
        self.gridLayout.addWidget(self.searchbutton, 0, 1, 1, 1)
        self.newsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.newsbutton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.newsbutton.setObjectName("newsbutton")
        self.gridLayout.addWidget(self.newsbutton, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setText("Прослушать")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 5)


        self.groupBox_2.setVisible(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Beat Store by Rodionov"))
        self.groupBox.setTitle(_translate("MainWindow", "Лучшее"))
        self.profilebutton.setText(_translate("MainWindow", "Профиль"))
        self.basketbutton.setText(_translate("MainWindow", "Корзина"))
        self.beatsbutton.setText(_translate("MainWindow", "Биты"))
        self.searchbutton.setText(_translate("MainWindow", "Поиск"))
        self.newsbutton.setText(_translate("MainWindow", "Новости"))

        self.profilebutton.clicked.connect(self.profile)
        self.profilebutton.setStyleSheet("background-color: #353535; border: 0px;")

        self.basketbutton.clicked.connect(self.basket)
        self.basketbutton.setStyleSheet("background-color: #353535; border: 0px;")

        self.beatsbutton.clicked.connect(self.beats)
        self.beatsbutton.setStyleSheet("background-color: #353535; border: 0px;")

        self.searchbutton.clicked.connect(self.search)
        self.searchbutton.setStyleSheet("background-color: #353535; border: 0px;")

        self.newsbutton.clicked.connect(self.news)
        self.newsbutton.setStyleSheet("background-color: #353535; border: 0px;")

        self.pushButton_6.clicked.connect(self.launch)
        
        self.beats()

    def launch(self):
        global player
        if self.pushButton_6.text() == "Прослушать":
            player.play()
            self.pushButton_6.setText("Приостановить")
        else:
            player.stop()
            self.pushButton_6.setText("Прослушать")

    def cleanlayout(self):
        for i in reversed(range(self.gridLayout_2.count())):
            self.gridLayout_2.itemAt(i).widget().deleteLater()

    def profile(self):

        global authorized

        self.cleanlayout()
        self.groupBox.setTitle("Профиль")

        if authorized:
            global user_id
            data = (user_id, )

            query = "select f_name, l_name, nick, country, city, about, reg_date from user_acc where u_id = %s;"
            cursor.execute(query, data)

            i = 0
            j = 0

            for item in cursor:
                for value in item:
                    value = str(value)
                    if j == 0:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel("Имя " + value), j, 0, 1, 1)
                    if j == 1:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel("Фамилия " + value), j, 0, 1, 1)
                    if j == 2:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel("Никнейм " + value), j, 0, 1, 1)
                        self.profilebutton.setText("Вы авторизованы как " + value)
                        nick = value
                    if j == 3:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel("Cтрана " + value), j, 0, 1, 1)
                    if j == 4:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel("Город " + value), j, 0, 1, 1)
                    if j == 5:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel("О себе " + value), j, 0, 1, 1)
                    if j == 6:
                        self.gridLayout_2.addWidget(QtWidgets.QLabel("Дата регистрации " + value), j, 0, 1, 1)
                    j += 1

            button = QtWidgets.QPushButton("Добавить трек")
            button.clicked.connect(self.addtrack)
            self.gridLayout_2.addWidget(button, j, 0, 1, 1)

            j += 1

            modify_button = QtWidgets.QPushButton("Изменить данные")
            modify_button.clicked.connect(self.modify)
            self.gridLayout_2.addWidget(modify_button, j, 0, 1, 1)

            j += 1

            message_button = QtWidgets.QPushButton("Сообщения")
            message_button.clicked.connect(self.messages)
            self.gridLayout_2.addWidget(message_button, j, 0, 1, 1)

            def admin(i, j):
                k = 0
                i += 1
                query = "select s_id, s_name, au_name, upload_date from samples order by amount desc;"
                cursor.execute(query)
                for item in cursor:
                    for value in item:
                        value = str(value)
                        if k == 0:
                            id = value
                            k += 1
                            continue
                        self.gridLayout_2.addWidget(QtWidgets.QLabel(value), i, j, 1, 1)
                        j += 1
                    button = QtWidgets.QPushButton("Удалить")
                    self.gridLayout_2.addWidget(button, i, j+1, 1, 1)
                    button.clicked.connect(lambda state, line=id: delete_beat(line))
                    j = 0
                    i += 1
                    k = 0

                def delete_beat(id):
                    data = (id, )
                    query = "delete from samples where s_id = %s"
                    cursor.execute(query, data)
                    cnx.commit()

                    self.profile()

                def delete_news(id):
                    data = (id, )
                    query = "delete from news where idnews = %s"
                    cursor.execute(query, data)
                    cnx.commit()

                    self.profile()

                query = "select idnews, title, body from news;"
                cursor.execute(query)

                for item in cursor:
                    for value in item:
                        if j == 0:
                            id = str(value)
                        value = str(value)
                        self.gridLayout_2.addWidget(QtWidgets.QLabel(value), i, j, 1, 1)
                        j += 1
                    button = QtWidgets.QPushButton("Удалить")
                    self.gridLayout_2.addWidget(button, i, j + 1, 1, 1)
                    button.clicked.connect(lambda state, line=id: delete_news(line))
                    i += 1
                    j = 0

            def user(i, j):
                k = 0
                i += 1
                query = "select s_id, s_name, au_name, upload_date from samples where au_name = %s order by amount desc;"
                data = (nick, )
                cursor.execute(query, data)
                for item in cursor:
                    for value in item:
                        value = str(value)
                        if k == 0:
                            id = value
                            k += 1
                            continue
                        self.gridLayout_2.addWidget(QtWidgets.QLabel(value), i, j, 1, 1)
                        j += 1
                    button = QtWidgets.QPushButton("Удалить")
                    self.gridLayout_2.addWidget(button, i, j + 1, 1, 1)
                    button.clicked.connect(lambda state, line=id: delete_beat(line))
                    j = 0
                    i += 1
                    k = 0

                def delete_beat(id):
                    data = (id,)
                    query = "delete from samples where s_id = %s"
                    cursor.execute(query, data)
                    cnx.commit()

                    self.profile()


            query = "select acc_type from user_acc where u_id = %s"
            data = (user_id, )
            cursor.execute(query, data)
            for item in cursor:
                for value in item:
                    value = str(value)
                    if value == "admin":
                        admin(j, i)
                    else:
                        user(j, i)


        else:
            self.label_2 = QtWidgets.QLabel()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
            self.label_2.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")
            self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
            self.label = QtWidgets.QLabel(self.centralwidget)
            font = QtGui.QFont()
            font.setPointSize(30)
            self.label.setFont(font)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
            self.loginedit = QtWidgets.QLineEdit()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.loginedit.sizePolicy().hasHeightForWidth())
            self.loginedit.setSizePolicy(sizePolicy)
            self.loginedit.setObjectName("loginedit")
            self.gridLayout_2.addWidget(self.loginedit, 1, 1, 1, 1)
            self.label_3 = QtWidgets.QLabel()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
            self.label_3.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(10)
            self.label_3.setFont(font)
            self.label_3.setObjectName("label_3")
            self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
            self.passedit = QtWidgets.QLineEdit()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.passedit.sizePolicy().hasHeightForWidth())
            self.passedit.setSizePolicy(sizePolicy)
            self.passedit.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.passedit.setAlignment(QtCore.Qt.AlignCenter)
            self.passedit.setObjectName("passedit")
            self.gridLayout_2.addWidget(self.passedit, 2, 1, 1, 1)
            self.login = QtWidgets.QPushButton()
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.login.sizePolicy().hasHeightForWidth())
            self.login.setSizePolicy(sizePolicy)
            self.login.setObjectName("loginbutton")
            self.gridLayout_2.addWidget(self.login, 3, 1, 1, 1)

            self.label_2.setText(("Логин"))
            self.label.setText(("Авторизация"))
            self.label_3.setText(("Пароль"))
            self.login.setText(("Вход"))

            def login():
                data = (self.loginedit.text(), )
                query = "select password from user_acc where mail = %s"
                cursor.execute(query, data)

                for item in cursor:
                    for value in item:
                        value = str(value)
                        if value == self.passedit.text():
                            global authorized
                            authorized = True
                            Message.show(Message, "Информация", "Авторизация успешна")

                            query = "select u_id from user_acc where mail = %s"
                            cursor.execute(query, data)
                            for item in cursor:
                                for value in item:
                                    global user_id
                                    user_id = str(value)

                            self.profile()
                        else:
                            Message.show(Message, "Информация", "Проверьте правильность ввода данных")
                        if value == "None":
                            Message.show(Message, "Информация", "Проверьте правильность ввода данных")

                if self.passedit.text() == "" or self.loginedit.text() == "":
                    Message.show(Message, "Информация", "Проверьте правильность ввода данных")

            self.login.clicked.connect(login)

    def basket(self):
        self.cleanlayout()
        self.groupBox.setTitle("Корзина")

    def beats(self):
        self.cleanlayout()

        i = 0
        j = 0

        query = "select s_name, au_name, style, price, upload_date, amount from samples order by amount desc;"
        cursor.execute(query)

        for item in cursor:
            item_group = QtWidgets.QGroupBox(" ")
            categorieslayout = QtWidgets.QGridLayout(item_group)
            self.gridLayout_2.addWidget(item_group, i, 0, 1, 1)
            for value in item:
                value = str(value)
                if j == 0:
                    beat = value
                if j == 2:
                    style = value
                    button = QtWidgets.QPushButton(value)
                    button.setStyleSheet("background-color: #353535; border: 0px;")
                    categorieslayout.addWidget(button, i, j, 1, 1)
                    button.clicked.connect(lambda state, line = style: display_style(line))
                else:
                    categorieslayout.addWidget(QtWidgets.QLabel(value), i, j, 1, 1)
                j += 1
            button = QtWidgets.QPushButton("Прослушать")
            #button.setIcon(QtGui.QIcon("play.svg"))
            button.clicked.connect(lambda state, item = beat: play(item))
            categorieslayout.addWidget(button, i, j, 1, 1)
            button = QtWidgets.QPushButton("Приобрести")
            button.setStyleSheet("background-color: #cc0000;")
            button.clicked.connect(lambda state, beat=id: play(id))
            categorieslayout.addWidget(button, i, j+1, 1, 1)
            i += 1
            j = 0

        def display_style(style):
            self.cleanlayout()

            query = "select s_name, au_name, style, price, upload_date from samples where style = %s order by amount desc;"

            self.groupBox.setTitle("Лучшее в жанре " + style)
            data = (style, )
            cursor.execute(query, data)

            j = 0
            i = 1

            for item in cursor:
                item_group = QtWidgets.QGroupBox(" ")
                categorieslayout = QtWidgets.QGridLayout(item_group)
                self.gridLayout_2.addWidget(item_group, i, 0, 1, 1)
                for value in item:
                    value = str(value)
                    if j == 0:
                        beat = value
                    categorieslayout.addWidget(QtWidgets.QLabel(value), i, j, 1, 1)
                    j += 1
                button = QtWidgets.QPushButton("Прослушать")
                # button.setIcon(QtGui.QIcon("play.svg"))
                button.clicked.connect(lambda state, item=beat: play(item))
                categorieslayout.addWidget(button, i, j, 1, 1)
                button = QtWidgets.QPushButton("Приобрести")
                button.setStyleSheet("background-color: #cc0000;")
                button.clicked.connect(lambda state, beat=id: play(id))
                categorieslayout.addWidget(button, i, j + 1, 1, 1)
                i += 1
                j = 0

            def play(id):

                if self.groupBox_2.isVisible():
                    pass
                else:
                    self.groupBox_2.setVisible(True)

                global playlist
                global player

                url = QtCore.QUrl.fromLocalFile("./" + id + ".mp3")
                playlist.addMedia(QtMultimedia.QMediaContent(url))

                query = "update samples set amount = amount + 1 where s_name = %s;"
                data = (id,)
                cursor.execute(query, data)
                cnx.commit()

                player.play()
                self.pushButton_6.setText("Приостановить")
                self.label.setText(id)

        def play(id):

            if self.groupBox_2.isVisible():
                pass
            else:
                self.groupBox_2.setVisible(True)

            global playlist
            global player

            url = QtCore.QUrl.fromLocalFile("./" + id + ".mp3")
            playlist.addMedia(QtMultimedia.QMediaContent(url))

            query = "update samples set amount = amount + 1 where s_name = %s;"
            data = (id, )
            cursor.execute(query, data)
            cnx.commit()

            player.play()
            self.pushButton_6.setText("Приостановить")
            self.label.setText(id)

    def search(self):
        self.cleanlayout()
        self.groupBox.setTitle("Поиск")

        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 0, 2, 1, 1)
        self.pushButton_7.setText("Найти")

        self.comboBox.addItem("Ник")
        self.comboBox.addItem("Жанр")
        self.comboBox.addItem("Название")

        def result():
            data = (self.lineEdit.text(), )
            if self.comboBox.currentIndex() == 0:
                query = "select s_name, au_name, style, price, upload_date from samples where au_name = %s order by amount desc;"
            if self.comboBox.currentIndex() == 1:
                query = "select s_name, au_name, style, price, upload_date from samples where style = %s order by amount desc;"
            if self.comboBox.currentIndex() == 2:
                query = "select s_name, au_name, style, price, upload_date from samples where s_name = %s order by amount desc;"

            cursor.execute(query, data)

            j = 0
            i = 1

            for item in cursor:
                item_group = QtWidgets.QGroupBox(" ")
                categorieslayout = QtWidgets.QGridLayout(item_group)
                self.gridLayout_2.addWidget(item_group, i, 0, 1, 1)
                for value in item:
                    value = str(value)
                    if j == 0:
                        beat = value
                    categorieslayout.addWidget(QtWidgets.QLabel(value), i, j, 1, 1)
                    j += 1
                button = QtWidgets.QPushButton("Прослушать")
                # button.setIcon(QtGui.QIcon("play.svg"))
                button.clicked.connect(lambda state, item=beat: play(item))
                categorieslayout.addWidget(button, i, j, 1, 1)
                button = QtWidgets.QPushButton("Приобрести")
                button.setStyleSheet("background-color: #cc0000;")
                button.clicked.connect(lambda state, beat=id: play(id))
                categorieslayout.addWidget(button, i, j + 1, 1, 1)
                i += 1
                j = 0

            def play(id):

                if self.groupBox_2.isVisible():
                    pass
                else:
                    self.groupBox_2.setVisible(True)

                global playlist
                global player

                url = QtCore.QUrl.fromLocalFile("./" + id + ".mp3")
                playlist.addMedia(QtMultimedia.QMediaContent(url))

                query = "update samples set amount = amount + 1 where s_name = %s;"
                data = (id,)
                cursor.execute(query, data)
                cnx.commit()

                player.play()
                self.pushButton_6.setText("Приостановить")
                self.label.setText(id)

        self.pushButton_7.clicked.connect(result)

    def news(self):
        self.cleanlayout()
        self.groupBox.setTitle("Новости")

        query = "select title, body from news;"
        cursor.execute(query)

        j = 0
        i = 0

        for item in cursor:
            item_group = QtWidgets.QGroupBox(" ")
            categorieslayout = QtWidgets.QGridLayout(item_group)
            self.gridLayout_2.addWidget(item_group, i, 0, 1, 1)
            for value in item:
                if j == 0:
                    item_group.setTitle(str(value))
                    j += 1
                    continue
                value = str(value)
                categorieslayout.addWidget(QtWidgets.QLabel(value), i, j, 1, 1)
                j += 1
            i += 1
            j = 0

    def addtrack(self):

        self.cleanlayout()

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("Название трека")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("Стиль")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setText("Цена")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 2, 1, 1)

        button = QtWidgets.QPushButton("Добавить")
        self.gridLayout_2.addWidget(button, 2, 0, 2, 2)

        def adder():
            global user_id

            query = "select nick from user_acc where u_id = %s"
            data = (user_id, )
            cursor.execute(query, data)

            for item in cursor:
                for value in item:
                    nickname = str(value)

            try:
                data = (self.lineEdit.text(), nickname, user_id, self.lineEdit_2.text(), self.lineEdit_4.text(), str(self.lineEdit.text() + ".mp3"))
                query = "insert into samples value (default, %s, %s ,%s, %s, %s, current_date(), %s, default)"
                cursor.execute(query, data)
                cnx.commit()
            except BaseException:
                pass

            self.beats()

        button.clicked.connect(adder)

    def modify(self):
        self.cleanlayout()

        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 5, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 6, 1, 1, 1)

        global user_id
        data = (user_id,)

        query = "select f_name, l_name, nick, country, city, about, reg_date from user_acc where u_id = %s;"
        cursor.execute(query, data)

        i = 0
        j = 0

        for item in cursor:
            for value in item:
                value = str(value)
                if j == 0:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Имя "), j, 0, 1, 1)
                    self.lineEdit.setText(value)
                if j == 1:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Фамилия "), j, 0, 1, 1)
                    self.lineEdit_2.setText(value)
                if j == 2:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Никнейм "), j, 0, 1, 1)
                    nick = value
                    self.lineEdit_3.setText(value)
                if j == 3:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Cтрана "), j, 0, 1, 1)
                    self.lineEdit_4.setText(value)
                if j == 4:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("Город "), j, 0, 1, 1)
                    self.lineEdit_5.setText(value)
                if j == 5:
                    self.gridLayout_2.addWidget(QtWidgets.QLabel("О себе "), j, 0, 1, 1)
                    self.lineEdit_6.setText(value)
                j += 1

        self.pushButton_6.setText("Cохранить")
        self.pushButton_6.clicked.connect(lambda: mod(nick))

        def mod(nick):
            data = (self.lineEdit.text(),self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(), nick)
            query = "UPDATE user_acc SET f_name = %s, l_name = %s, nick = %s, country = %s, city = %s, about = %s WHERE nick = %s;"
            cursor.execute(query, data)
            cnx.commit()
            self.profile()


        '''
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        '''

    def messages(self):
        self.cleanlayout()

        global user_id

        self.groupBox.setTitle("Cообщения")

        self.scrollArea_2 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 68, 263))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 436, 263))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.addWidget(self.scrollArea_3, 0, 1, 1, 1)

        query = "select nick from user_acc where u_id in (select sender_id from messages where reciver_id = %s);"
        data = (user_id, )
        cursor.execute(query, data)

        for item in cursor:
            for value in item:
                value = str(value)
                nick = value
                button = QtWidgets.QPushButton(value)
                self.verticalLayout_2.addWidget(button)
                button.clicked.connect(lambda state, id = nick: dialog(id))

        new_message_button = QtWidgets.QPushButton("Написать")
        new_message_button.clicked.connect(lambda: new())
        self.verticalLayout_2.addWidget(new_message_button)

        def new():
            text, ok = QtWidgets.QInputDialog.getText(self, "Новое сообщение", "Никнейм")

            if ok and text != "" and text != " ":
                dialog(text)

        def dialog(id):

            for i in reversed(range(self.verticalLayout_3.count())):
                self.verticalLayout_3.itemAt(i).widget().deleteLater()

            query = 'select u_id from user_acc where nick = %s'
            cursor.execute(query, (id, ))
            for item in cursor:
                for value in item:
                    id = str(value)

            query = "select text from messages where (reciver_id = %s and sender_id = %s) or (sender_id = %s and reciver_id = %s);"
            data = (user_id, id, user_id, id)
            cursor.execute(query, data)
            for item in cursor:
                for value in item:
                    self.verticalLayout_3.addWidget(QtWidgets.QLabel(str(value)))

            item_group = QtWidgets.QGroupBox("")
            categorieslayout = QtWidgets.QHBoxLayout(item_group)
            self.verticalLayout_3.addWidget(item_group)

            line_edit = QtWidgets.QLineEdit()
            categorieslayout.addWidget(line_edit)

            button = QtWidgets.QPushButton("Отправить")
            categorieslayout.addWidget(button)
            button.clicked.connect(lambda: send(id))

            def send(id):
                query = "insert into messages values (default, %s, %s, %s, now())"
                data = (user_id, id, line_edit.text())
                cursor.execute(query, data)
                cnx.commit()

                query = 'select nick from user_acc where u_id = %s'
                cursor.execute(query, (id,))
                for item in cursor:
                    for value in item:
                        id = str(value)

                dialog(id)


class Message(object):
    def show(self, Title, Text):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setWindowTitle(Title)
        msgbox.setWindowIcon(QtGui.QIcon(QtGui.QPixmap('icons/i.png')))
        msgbox.setText(Text)
        msgbox.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    dark_palette = QtGui.QPalette()

    dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.WindowText,  QtGui.QColor(255, 255, 255))
    dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(255, 255, 255))
    dark_palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(255, 255, 255))
    dark_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(255, 255, 255))
    dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(0, 100, 0))
    dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255, 255, 255))
    dark_palette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255, 255, 255))
    dark_palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    dark_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(0, 0, 0))

    app.setPalette(dark_palette)

    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 2px solid white; }")

    font = QtGui.QFont("Rostov")
    font.setPointSize(18)

    app.setFont(font)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
