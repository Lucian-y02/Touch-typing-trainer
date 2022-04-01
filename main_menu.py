import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QTimer, Qt
from random import sample
from os import listdir
from shutil import copyfile
from string import ascii_lowercase


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.level = QtWidgets.QComboBox(self.centralwidget)
        self.level.setObjectName("level")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.horizontalLayout.addWidget(self.level)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.number = QtWidgets.QComboBox(self.centralwidget)
        self.number.setObjectName("number")
        self.horizontalLayout.addWidget(self.number)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lang = QtWidgets.QComboBox(self.centralwidget)
        self.lang.setObjectName("lang")
        self.lang.addItem("")
        self.lang.addItem("")
        self.horizontalLayout.addWidget(self.lang)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.gridLayout.addWidget(self.start, 0, 3, 1, 1)
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setMinimumSize(QtCore.QSize(600, 91))
        self.text.setMaximumSize(QtCore.QSize(600, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.text.setFont(font)
        self.text.setTabChangesFocus(False)
        self.text.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.text.setReadOnly(True)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 1, 0, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.speed = QtWidgets.QLCDNumber(self.centralwidget)
        self.speed.setObjectName("speed")
        self.gridLayout.addWidget(self.speed, 2, 1, 1, 1)
        self.load = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.load.setFont(font)
        self.load.setObjectName("load")
        self.gridLayout.addWidget(self.load, 2, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Тренажёр для слепой печати"))
        self.label.setText(_translate("MainWindow", "Уровень"))
        self.level.setItemText(0, _translate("MainWindow", "Для начинающих"))
        self.level.setItemText(1, _translate("MainWindow", "Для опытных"))
        self.level.setItemText(2, _translate("MainWindow", "Для экспертов"))
        self.level.setItemText(3, _translate("MainWindow", "Пользовательские упражнения"))
        self.label_2.setText(_translate("MainWindow", "Номер урока"))
        self.label_3.setText(_translate("MainWindow", "Язык"))
        self.lang.setItemText(0, _translate("MainWindow", "ENG"))
        self.lang.setItemText(1, _translate("MainWindow", "РУС"))
        self.start.setText(_translate("MainWindow", "Открыть урок"))
        self.text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "Скорость печати (символов в секунду)"))
        self.load.setText(_translate("MainWindow", "Загрузить новый урок"))


class Ui_LoadWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 175)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.load = QtWidgets.QPushButton(self.centralwidget)
        self.load.setGeometry(QtCore.QRect(20, 100, 461, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.load.setFont(font)
        self.load.setObjectName("load")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.path_display = QtWidgets.QLineEdit(self.centralwidget)
        self.path_display.setGeometry(QtCore.QRect(50, 10, 351, 20))
        self.path_display.setObjectName("path_display")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(410, 10, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.browse.setFont(font)
        self.browse.setObjectName("browse")
        self.file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(120, 50, 361, 20))
        self.file_name.setObjectName("file_name")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Загрузка урока"))
        self.load.setText(_translate("MainWindow", "Загрузить"))
        self.label.setText(_translate("MainWindow", "Путь:"))
        self.label_2.setText(_translate("MainWindow", "Название урока:"))
        self.browse.setText(_translate("MainWindow", "Обзор"))


ALPHABET = {
    "ENG": set(list(ascii_lowercase)),
    "РУС": set(list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"))
}
EXCLUSION_KEYS = {Qt.Key_Backspace, Qt.Key_Tab, Qt.Key_Alt, Qt.Key_Control, Qt.Key_Shift}

LEVEL_NAME = {
    "Для начинающих": "For beginners",
    "Для опытных": "For advanced",
    "Для экспертов": "For experts",
}

FINGERS = {
    "Левый мизинец": ("z", "q", "a", "ё", "й", "ф", "я"),
    "Правый мизинец": ("p", "/", "'", ";", "з", "ж", "ъ", "э", "х", "\\"),
    "Левый безымянный палец": ("w", "s", "x", "ц", "ы", "ч"),
    "Правый безымянный палец": ("o", "l", ".", "щ", "д", "ю"),
    "Левый средний палец": ("e", "d", "c", "у", "в", "с"),
    "Правый средний палец": ("i", "k", ",", "ш", "л", "б"),
    "Левый указательный палец": ("r", "t", "f", "g", "v", "b", "к", "е", "а", "п", "м", "и"),
    "Правый указательный палец": ("y", "u", "h", "j", "n", "m", "н", "г", "р", "о", "т", "ь")
}


class LoadWindow(QMainWindow, Ui_LoadWindow):
    def __init__(self):
        super(LoadWindow, self).__init__()
        self.setupUi(self)
        self.initUi()

        self.path = ""

    def initUi(self):
        self.load.clicked.connect(self.click)
        self.browse.clicked.connect(self.click)

    def click(self):
        if self.sender().objectName() == "browse":
            self.path = QFileDialog.getOpenFileName(self, "Выбрать текст", "", "(*.txt)")[0]
            self.path_display.setText(self.path)
        if self.sender().objectName() == "load" and self.file_name.text() and self.path:
            self.load_lesson()
        elif self.sender().objectName() == "load":
            self.statusbar.showMessage("Укажите название урока", 8000)

    # Загрузка пользовательского урока
    def load_lesson(self):
        self.statusbar.showMessage(f"Урок \"{self.file_name.text()}\" загружен", 8000)
        copyfile(self.path, f"Lessons/Custom exercises/{self.file_name.text()}.txt")


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.initUi()

        # Текст
        self.lesson_text = list()
        # Текст для отображения
        self.lesson_text_for_display = str()

        self.caps_lock_active = False
        self.lesson_goes = False

        # Начало отсчёта
        self.start_stopwatch = False

        # Текущий символ для проверки
        self.now_sign = str()

        # Указатели для отображения определённой части текста
        self.start_pointer = 0
        self.end_pointer = 32

        # Счётчик правильно напечатанных символов
        self.counter = 0

        # Счётчик секунд
        self.time = 0

    def initUi(self):
        self.start.clicked.connect(self.click)
        self.load.clicked.connect(self.click)
        self.stopwatch = QTimer(self)
        self.level.currentTextChanged.connect(self.current_CBox)
        self.lang.currentTextChanged.connect(self.current_CBox_lang)
        self.current_CBox("Для начинающих")
        self.load_wnd = LoadWindow()

    # Функция для изменения ComboBox номера урока
    def current_CBox(self, text):
        self.number.clear()
        if text == "Пользовательские упражнения":
            self.number.clear()
            add_item = list(map(lambda y: y[: -4],
                                filter(lambda x: x.endswith(".txt"),
                                       listdir(f"Lessons/Custom exercises"))))
        elif text == "Для опытных":
            add_item = sorted(list(ALPHABET[self.lang.currentText()]))
            if self.lang.currentText() == "РУС":
                del add_item[-1]
                add_item.insert(6, "ё")
        else:
            add_item = list(map(lambda y: y[:-4],
                                filter(lambda x: x.endswith(".txt"),
                                       listdir(f"Lessons/{self.lang.currentText()}/"
                                               f"{LEVEL_NAME[text]}"))))
            if len(add_item) > 1:
                add_item.sort(key=lambda x: int(x.split()[1]))
        self.number.addItems(add_item)

    # Отслеживание изменения поля для выбора языка
    def current_CBox_lang(self):
        self.current_CBox(self.level.currentText())

    def click(self):
        if self.sender().objectName() == "start" and \
                self.level.currentText() == "Пользовательские упражнения":
            self.make_custom_lesson()
            self.restart_lesson()
        elif self.sender().objectName() == "start":
            self.make_lesson()
            self.restart_lesson()
        if self.sender().objectName() == "load":
            # self.load_lesson()
            self.load_wnd.show()

    # Замер скорости печати (символов в секунду)
    def set_speed(self):
        self.time += 1
        self.speed.display(round(self.counter / self.time, 1))

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        # Отсчёт времени начинается, если пользователь нажмёт любую клавишу
        if not self.start_stopwatch:
            self.start_stopwatch = True
            self.stopwatch.timeout.connect(self.set_speed)
            self.stopwatch.start(1000)

        # Нажатие кнопки caps lock
        if event.key() == Qt.Key_CapsLock:
            self.caps_lock_active = not self.caps_lock_active
            return None

        # Проверка на комбинацию c зажатой кнопкой Shift
        if event.modifiers() == Qt.ShiftModifier and self.lesson_goes:
            if event.key() not in EXCLUSION_KEYS:
                self.check_sign(event.key(), True)
        elif self.lesson_goes and event.key() not in EXCLUSION_KEYS:
            self.check_sign(event.key(), False)

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key_Space:
            self.check_sign(" ", False)

    # Перезапуск урока
    def restart_lesson(self):
        self.text.setFocus()
        self.lesson_goes = True
        self.start_stopwatch = False
        self.counter = 0
        self.start_pointer = 0
        self.end_pointer = 32
        self.time = 0
        self.now_sign = self.lesson_text.pop(0)
        self.get_finger()
        self.text.setText(self.lesson_text_for_display[self.start_pointer: self.end_pointer])
        self.text.setStyleSheet("text: rgb(0, 0, 0)")

    # Окончание урока
    def end(self):
        self.lesson_goes = False
        self.text.setText("Урок пройден!")
        self.text.setStyleSheet("text: rgb(0, 0, 0)")
        self.stopwatch.stop()
        self.statusbar.clearMessage()

    # Проверка введённого символа
    def check_sign(self, sign, shift_active):
        if shift_active and sign != " ":
            sign = chr(sign).lower() if self.caps_lock_active else chr(sign).upper()
        elif sign != " ":
            sign = chr(sign).upper() if self.caps_lock_active else chr(sign).lower()
        try:
            if sign == self.now_sign:
                self.now_sign = self.lesson_text.pop(0)
                self.get_finger()
                self.start_pointer += 1
                self.end_pointer += 1
                self.text.setStyleSheet("color: rgb(0, 200, 0)")
                self.text.setText(
                    self.lesson_text_for_display[self.start_pointer: self.end_pointer])
                self.counter += 1
            else:
                self.text.setStyleSheet("color: rgb(200, 0, 0)")
        except IndexError:
            self.end()

    def make_lesson(self):
        # Создание урока "Для опытных"
        if self.level.currentText() == "Для опытных":
            control_char = self.number.currentText()
            random_chars = "".join(sample(ALPHABET[self.lang.currentText()], 20))
            self.lesson_text_for_display = "".join(
                list((control_char + random_chars[x: x + 2] + " ") * 3
                     for x in range(0, 20, 2)))[: -1]
        else:
            with open(f"Lessons/{self.lang.currentText()}/{LEVEL_NAME[self.level.currentText()]}/"
                      f"{self.number.currentText()}.txt", "r", encoding="utf8") as file:
                # Создание урока "Для начинающих"
                if self.level.currentText() == "Для начинающих":
                    lesson_text = list(file.readline())
                    self.lesson_text_for_display = " ".join(
                        [" ".join(sample(lesson_text, len(lesson_text))) for _ in range(4)])
                # Создание урока "Для экспертов"
                else:
                    self.lesson_text_for_display = " ".join(map(lambda x: x.strip("\n"), file.readlines()))
                    self.lesson_text = list(self.lesson_text_for_display)

        self.lesson_text = list(self.lesson_text_for_display)

    # Создание пользовательского урока
    def make_custom_lesson(self):
        with open(f"Lessons/Custom exercises/{self.number.currentText()}.txt") as file:
            self.lesson_text_for_display = " ".join(map(lambda x: x.strip("\n"), file.readlines()))
            self.lesson_text = list(self.lesson_text_for_display)

    # Указание - каким пальцем нужно нажать клавишу
    def get_finger(self):
        for key in FINGERS.keys():
            if self.now_sign == " ":
                self.statusbar.showMessage("Большой палец пробел")
                break
            elif (self.now_sign in FINGERS[key] and self.now_sign.islower()) or \
                    (not self.now_sign.isalpha() and self.now_sign in FINGERS[key]):
                self.statusbar.showMessage(f"{key} {self.now_sign}")
                break
            elif self.now_sign.isupper() and self.now_sign.lower() in FINGERS[key]:
                self.statusbar.showMessage(f"{key} {self.now_sign}; Мизинцем противоположной руки shift")
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
