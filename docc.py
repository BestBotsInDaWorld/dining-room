"""
from PyQt5.QtWidgets import QWidget, QCheckBox, QRadioButton, QPlainTextEdit
from PyQt5.QtWidgets import QLabel, QLineEdit, QLCDNumber, QPushButton, QButtonGroup

Проблемы с connect(func(args))?
Используйте connect(lambda: func(args))!
Кнопки привязываются к одним и тем же аргументам?
Используйте connect(functools.partial(func, args))!
Не забывай QCheckBox(self), или не будет показываться

isHidden() - спрятано ли
.hide() - спрятать
.show() - показать
если устанавливать в лейбл eval(), то нужно его приводить к строчному виду
str(eval())

import sys - заход/выход из системы

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox - приложение, виджет, кнопки, галочки
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QLCDNumber - окно, лэйблы, строки с редактом, счетчики

if __name__ == '__main__': - в конце для начала работы
    app = QApplication(sys.argv)
    ex = Evaluator()
    ex.show()
    sys.exit(app.exec())

QCheckBox
self.checkbox = QCheckBox('edit1', self)
self.checkbox.move(20, 20)
self.checkbox.stateChanged.connect(self.trick) - как clicked.connect у кнопок

self.setGeometry(x1, y1, x2, y2) - размеры окна (x1, y1 отвечают за место на экране монитора, на котором появится окно,
x2 и y2 за размер окна)

class Evaluator(QWidget): - наследование виджета обязательно для использования старших функций
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(x1, y1, x2, y2) - размеры окна (x1, y1 отвечают за место на экране монитора, на котором появится окно,
x2 и y2 за размер окна)
        self.setWindowTitle('Вторая программа') - название окна
        ...
        self.show() - возможно нужно

self.btn/label/name.text() - показать текст
self.btn/label/name.setText() - установить текст

self.name_label = QLabel(self) - во всех используемых экземплярах высших классов задаем дочерний экземпляр
self.name_label.setText("Введите имя: ")
self.name_label.move(40, 90) - лейбл, онли текст

self.name_input = QLineEdit(self) - ввод строк, текст сохраняется и его можно менять
self.name_input.move(130, 90)


self.btn = QPushButton('Кнопка', self) - кнопка
self.btn.resize(self.btn.sizeHint()) - размер кнопки под размер надписи
self.btn.move(100, 150) - левый верхний угол
self.button_1.setText("Кнопка 1") - установить текст
self.btn.clicked.connect(self.hello) - какая функция вызывается при нажатии


self.LCD_count = QLCDNumber(self) - счетчик
self.LCD_count.move(110, 80)
self.count = 0
self.count += 1
self.LCD_count.display(self.count) - показать счет


self.button_2.clicked.connect(self.run)
def run(self):
    print(self.sender().text()) - показать текст на кнопке - отправителе
"""