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
    def check_not_occupied(self):
        from point_choice import adress
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT tables FROM points WHERE Adress='{adress}'"
                cursor.execute(find_query)
                table = cursor.fetchall()
                print(table)

        except Exception as ex:
            print(ex)


