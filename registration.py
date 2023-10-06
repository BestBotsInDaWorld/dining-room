import kivy
import jwt
import uuid
import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from databaseconnect import *


secret_word = "sberbank"
Builder.load_file('registrate.kv')

properties = ["имя", "фамилию", "отчество", "дату рождения", "пол"]


class wrong_log_check(Exception):
    pass


class wrong_check_password(Exception):
    pass


class wrong_check_difference(Exception):
    pass


class emptiness(Exception):
    pass


class not_chosen(Exception):
    pass


def check_login(log):
    pass


def check_sex(cb1, cb2):
    if cb1.active:
        return "Мужской"
    elif cb2.active:
        return "Женский"
    raise not_chosen("Выберите пол")


def validate(date_text):
    try:
        text = ""
        if len(date_text) == 10:
            text = date_text[6:] + "-" + date_text[3:5] + "-" + date_text[:2]
        datetime.date.fromisoformat(text)
    except ValueError:
        raise ValueError("Дата должна быть в формате ДД.ММ.ГГГГ")


def check_password(number):
    if len(number) <= 8:
        raise wrong_check_password('В пароле должно быть \n хотя бы 9 символов')
    is_up = False
    is_down = False
    has_dig = False
    for i in range(len(number)):
        if number[i].isupper():
            is_up = True
        elif number[i].islower():
            is_down = True
        if number[i].isdigit():
            has_dig = True
    if not is_up or not is_down:
        raise wrong_check_password('В пароле должна быть \n хотя бы одна заглавная и \n одна строчная буква')
    if not has_dig:
        raise wrong_check_password('В пароле должна быть \n хотя бы одна цифра')
    return 'ok'


def check_difference(password1, password2):
    if password1 != password2:
        raise wrong_check_difference('Пароли различаются')


def check_emptiness(line):
    if len(line) == 0:
        raise emptiness("Заполните строку")


class Registring(Widget):

    def btn_click(self):
        global secret_word, sex
        all_elements = [self.name, self.surname, self.last_name, self.born]
        self.check_1.text = ""
        self.check_2.text = ""
        self.check_3.text = ""
        self.empty_line.text = ""
        for i in range(len(all_elements)):
            try:
                check_emptiness(all_elements[i].text)
            except emptiness as e:
                self.empty_line.text = f'Введите {properties[i]}'
                return 0
            if i == 3:
                try:
                    validate(all_elements[3].text)
                except ValueError as v:
                    self.empty_line.text = str(v)
                    return 0
        try:
            check_sex(self.cb1, self.cb2)
        except not_chosen as n:
            self.empty_line.text = str(n)
            return 0
        try:
            check_login(self.login.text)
        except wrong_log_check as log_err:
            self.check_1.text = log_err
            return 0
        try:
            check_password(self.password.text)
        except wrong_check_password as pass_err:
            self.check_2.text = str(pass_err)
            return 0
        try:
            check_difference(self.password.text, self.confirm_password.text)
        except wrong_check_difference as dif_err:
            self.check_3.text = str(dif_err)
            return 0
        sex = check_sex(self.cb1, self.cb2)
        login, password = str(self.login.text), str(self.password.text)
        name, surname, last_name, born = str(self.name.text), str(self.surname.text), \
            str(self.last_name.text), str(self.born.text)
        jwt_id = str(uuid.uuid4())
        payload = {
            "login": login,
            "password": password,
        }
        encoded_jwt = jwt.encode(payload, secret_word, algorithm="HS256")
        # aleph = jwt.decode(encoded_jwt, secret_word, algorithms=["HS256"]) дешифратор выдает сразу словарь payload
        databaseconnect.Register_Finish(encoded_jwt, name, surname, last_name)
        return [encoded_jwt, name, surname, last_name, sex, born]


class RegApp(App):
    def build(self):
        return Registring()


if __name__ == '__main__':
    RegApp().run()
