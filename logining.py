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
from databaseconnect import *
import pymysql
from kivy.uix.screenmanager import Screen, ScreenManager


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
LabelBase.register(name='RubikMonoOne_Regular',
                   fn_regular=r'fonts\RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts\Finlandica-Regular.ttf')



class WindowManager(ScreenManager):
    pass


class Logining(Widget):
    def enter(self):
        # try:
        #     with cursor.connect as cursor:
        #         pass
        # except Exception as ex:
        #     print(ex)
        pass

    def Registration_button(self):
        pass




class RegApp(App):
    def build(self):
        return Logining()


if __name__ == '__main__':
    RegApp().run()
