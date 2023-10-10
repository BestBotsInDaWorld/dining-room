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
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.image import Image
Builder.load_file('food_menu.kv')
from kivymd.uix.list import OneLineIconListItem

LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts/RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts/Finlandica-Regular.ttf')
class ImageButton(Button):
    def __init__(self, im="", **kwargs):
        super(ImageButton, self).__init__(**kwargs)
        print(im)
        self.image = Image(source=im, size =self.size, pos = self.pos)
        self.add_widget(self.image)



class FoodMenuApp(Screen):
    def __init__(self, **kwargs):
        super(FoodMenuApp, self).__init__(**kwargs)
        self.food_choice = DropDown()
        food = []
        try:
            with connection.cursor() as cursor:
                find_query = f"SELECT * FROM menu"
                cursor.execute(find_query)
                food = cursor.fetchall()
        except Exception as ex:
            print(ex)
        for index in range(len(food)):
            print(food[index]["image"])
            btn = Button(text=f'{food[index]["dish"]} {food[index]["price"]} руб.',
                              size_hint_y=None, height=44, font_size=Window.width / 55)
            btn.bind(on_release=lambda btn: self.food_choice.select(btn.text))
            self.food_choice.add_widget(btn)
        self.food_button.bind(on_release=self.food_choice.open)
        self.food_choice.bind(on_select=lambda instance, x: setattr(self.food_button, 'text', x))

    def switch_image(self):
        text = str(self.food_button.text).split()[0]
        print(text)
