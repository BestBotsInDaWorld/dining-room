import kivy
import jwt
import uuid
from kivymd.app import MDApp
import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import databaseconnect
from databaseconnect import *

Builder.load_file("Points.kv")


class SomePointApp(Screen):
    def check_not_occupied1(self):
        from point_choice import adress
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT tables FROM points WHERE Adress='{adress}'"
                cursor.execute(find_query)
                table = cursor.fetchall()[0]["tables"].split(",")[1]

                if table == '1':
                    self.table1.text = "Стол занят"
                else:
                    return 1
        except Exception as ex:
            print(ex)

    def check_not_occupied2(self):
        from point_choice import adress
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT tables FROM points WHERE Adress='{adress}'"
                cursor.execute(find_query)
                table = cursor.fetchall()[0]["tables"].split(",")[1]

                if table == '1':
                    self.table1.text = "Стол занят"
                else:
                    return 1
        except Exception as ex:
            print(ex)

    def check_not_occupied3(self):
        from point_choice import adress
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT tables FROM points WHERE Adress='{adress}'"
                cursor.execute(find_query)
                table = cursor.fetchall()[0]["tables"].split(",")[1]

                if table == '1':
                    self.table1.text = "Стол занят"
                else:
                    return 1
        except Exception as ex:
            print(ex)

    def check_not_occupied4(self):
        from point_choice import adress
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT tables FROM points WHERE Adress='{adress}'"
                cursor.execute(find_query)
                table = cursor.fetchall()[0]["tables"].split(",")[1]
                if table == '1':
                    self.table1.text = "Стол занят"
                else:
                    return 1

        except Exception as ex:
            print(ex)
