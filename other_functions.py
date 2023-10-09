import kivy
import jwt
import os
import uuid
import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import pymysql
Builder.load_file('otherFunctions.kv')

LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts\RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts\Finlandica-Regular.ttf')

try:
    connection = pymysql.connect(host='37.140.192.80',
                                 user='u0823922_hakaton',
                                 password='tB4nG4fN9sqG1vJ9',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="u0823922_hakaton")
    print("successfully...")
except Exception as ex:
    print(ex)

class AboutUsApp(Screen):
    pass


class OtherSystemsApp(Screen):
    pass


class BalanceApp(Screen):
    def update_balance(self, res):
        self.user_balance.text = f"{res}"


def isfloat(num):
    try:
        float(str(num))
        return True
    except ValueError:
        return False


class DepositApp(Screen):
    def confirm_deposit(self):
        from logining import encoded_try
        print(encoded_try)

        if isfloat(str(self.deposit.text)):
            try:
                with connection.cursor() as cursor:
                    print(float(self.deposit.text))
                    find_query = f"SELECT balance FROM users WHERE jwt='{encoded_try}'"
                    cursor.execute(find_query)
                    summ = cursor.fetchall()[0]["balance"]
                    print(summ)
                    ress = float(self.deposit.text) + summ
                    update_query = f"UPDATE `users` SET `balance`='{ress}' WHERE jwt ='{encoded_try}'"
                    cursor.execute(update_query)
                    connection.commit()

                    self.deposit.text = ""
                    BalanceApp.update_balance(res=ress)
            except Exception as ex:
                print(ex)
        else:
            print("else")

