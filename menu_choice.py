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
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import pymysql
try:
    connection = pymysql.connect(host='37.140.192.80',
                                 user='u0823922_hakaton',
                                 password='tB4nG4fN9sqG1vJ9',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 database="u0823922_hakaton")
    print("successfully...")
except Exception as ex:
    print(ex)
Builder.load_file('menu_choice.kv')


class MenuChoiceApp(Screen):

    def __init__(self, **kwargs):
        super(MenuChoiceApp, self).__init__(**kwargs)
        self.point_choice_add = DropDown()
        adress = []
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT * FROM places"
                cursor.execute(find_query)
                adress = cursor.fetchall()
        except Exception as ex:
            print(ex)
        for index in range(len(adress)):
            btn = Button(text=adress[index]["Adress"], size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.point_choice_add.select(btn.text))
            self.point_choice_add.add_widget(btn)
        self.point_button_add.bind(on_release=self.point_choice_add.open)
        self.point_choice_add.bind(on_select=lambda instance, x: setattr(self.point_button_add, 'text', x))

        self.user_choice = DropDown()