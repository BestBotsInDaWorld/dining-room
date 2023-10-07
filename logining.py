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
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from databaseconnect import *
import pymysql
try:
    connection = pymysql.connect(host='37.140.192.80',
                                 user='u0823922_codolo1',
                                 password='codologia1',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="u0823922_test")
    print("successfully...")
except Exception as ex:
    print(ex)
Builder.load_file('login.kv')

class MyLabel(Label):
    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        font_path = r"C:\Users\Даниил\Documents\GitHub\dining-room\fonts\RubikMonoOne-Regular.ttf"
        self.finlandica_medium = font_path
        font_path = r"C:\Users\Даниил\Documents\GitHub\dining-room\fonts\RubikMonoOne-Regular.ttf"
        self.finlandica_regular = font_path
        font_path = r"C:\Users\Даниил\Documents\GitHub\dining-room\fonts\RubikMonoOne-Regular.ttf"
        self.rubikMonoOne_regular = font_path

class Logining(Widget):
    def enter(self):
        # try:
        #     with cursor.connect as cursor:
        #         pass
        # except Exception as ex:
        #     print(ex)
        pass


class RegApp(App):
    def build(self):
        return Logining()


if __name__ == '__main__':
    RegApp().run()
