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
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from databaseconnect import *
import pymysql
secret_word = "sberbank"
try:
    connection = pymysql.connect(host='37.140.192.80',
                                 user='u0823922_hakaton',
                                 password='tB4nG4fN9sqG1vJ9',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="u0823922_hakaton")
    print("successfully...")
except Exception as ex:
    print(ex)
Builder.load_file('adminLogin.kv')
LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts\RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts\Finlandica-Regular.ttf')


class AdminLogApp(Screen):
    def check_admin(self):
        payload = {"login": str(self.username_input.text), "password": str(self.password_input.text)}

        jwt_token = jwt.encode(payload, "sberbank",  algorithm="HS256")
        print(jwt_token)
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT * FROM `admin_login` WHERE `jwt_token` = '{str(jwt_token)}'"
                cursor.execute(find_query)

                if len(cursor.fetchall()) == 0:
                    self.worst_login.text = "Неверный логин или пароль"
                    raise Exception()
                self.worst_login.text = "Зашел"
        except Exception as ex:
            print(ex)