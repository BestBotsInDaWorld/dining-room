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

food_cart = {"Торт": 1000}
food_amound_price = {"Торт": [2, 500]}
LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts/RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts/Finlandica-Regular.ttf')

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
            btn.bind(on_release=lambda btn: self.double(btn.text))
            self.food_choice.add_widget(btn)
        self.food_button.bind(on_release=self.food_choice.open)
        self.food_choice.bind(on_select=lambda instance, x: setattr(self.food_button, 'text', x))

    def switch_image(self, text):
        link = Image_Switch(text)
        try:
            self.food_image.source = link
        except Exception as e:
            pass
    def double(self, text):
        self.food_choice.select(str(text))
        self.switch_image(str(text).split()[0])

    def add_to_order(self):
        global food_cart, food_amound_price
        amount = int(self.food_counter.text)
        name = str(self.food_button.text).split()[0]
        price = int(str(self.food_button.text).split()[1])
        food_cart[name] = food_cart.get(name, 0) + amount * price
        total = food_amound_price.get(name, [0, 0])[0] + amount
        food_amound_price[name] = [total, price]

class FoodCartApp(Screen):
    def __init__(self, **kwargs):
        super(FoodCartApp, self).__init__(**kwargs)

        self.food_exclude_choice = DropDown()
        positions = list(food_cart.items())
        for index in range(len(food_cart.keys())):
            btn = Button(text=f'{positions[index][0].split()[0]}',
                              size_hint_y=None, height=44, font_size=Window.width / 55)
            btn.bind(on_release=lambda btn: self.triple(btn.text))
            self.food_exclude_choice.add_widget(btn)
        self.food_exclude_button.bind(on_release=self.food_exclude_choice.open)
        self.food_exclude_choice.bind(on_select=lambda instance, x: setattr(self.food_exclude_button, 'text', x))

    def switch_image(self, text):
        link = Image_Switch(text)
        try:
            self.food_exclusion_image.source = link
        except Exception as e:
            pass
    def triple(self, text):
        self.food_exclude_choice.select(str(text))
        self.switch_image(str(text).split()[0])

    def reload(self):
        self.__init__()