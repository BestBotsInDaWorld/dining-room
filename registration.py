import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('reg.kv')


class wrong_log_check(Exception):
    pass


class wrong_check_password(Exception):
    pass


class password_different(Exception):
    pass


def check_password(number):
    if len(number) <= 8:
        raise wrong_check_password('В пароле должно быть хотя бы 9 символов')
    is_up = False
    is_down = False
    has_dig = False
    has_seq = False
    for i in range(len(number)):
        if number[i].isupper():
            is_up = True
        elif number[i].islower():
            is_down = True
        if number[i].isdigit():
            has_dig = True
    if not is_up or not is_down:
        raise wrong_check_password('В пароле должна быть хотя бы одна заглавная и одна строчная буква')
    if not has_dig:
        raise wrong_check_password('В пароле должна быть хотя бы одна цифра')
    return 'ok'


def check_difference(password1, password2):
    if password1 != password2:
        raise password_different('Пароли различаются')


class Registring(Widget):
    sex = ""
    name = ObjectProperty(None)
    surname = ObjectProperty(None)
    last_name = ObjectProperty(None)
    number = ObjectProperty(None)
    login = ObjectProperty(None)
    password = ObjectProperty(None)
    confirm_password = ObjectProperty(None)

    def press(self):
        check_password()
        name = self.name.text
        number = self.number.text

    def sex_choice(self, instance, value, gender):
        sex = gender

    def btn_click(self):
        check_password()
        return []


class RegApp(App):
    def build(self):
        return Registring()


if __name__ == '__main__':
    RegApp().run()
