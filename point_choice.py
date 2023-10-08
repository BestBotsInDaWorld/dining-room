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
Builder.load_file('point_choice.kv')


class PointChoiceApp(Screen):

    def __init__(self, **kwargs):
        super(PointChoiceApp, self).__init__(**kwargs)
        self.point_choice = DropDown()
        adress = []
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT * FROM places"
                cursor.execute(find_query)
                adress = cursor.fetchall()
                print(adress)
        except Exception as ex:
            print(ex)
        for index in range(len(adress)):
            btn = Button(text='Value %d' % adress[index]["Adress"], size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.point_choice.select(btn.text))
            self.point_choice.add_widget(btn)
        self.point_button.bind(on_release=self.point_choice.open)
        self.point_choice.bind(on_select=lambda instance, x: setattr(self.point_button, 'text', x))