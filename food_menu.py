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
        s2 = self.manager.get_screen("FoodCart")
        s2.deleting_dishes()


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
        our_order = list(food_cart.items())
        our_items = list(food_amound_price.items())
        order = 0
        for i in range(len(food_cart)):
            dish, total = our_order[i]
            amm = our_items[i][1][0]
            order += int(total)
            self.total_order.text = self.total_order.text + f'{dish} {amm} шт. {total} руб.\n'
        self.total_summ.text = f'{str(order)} руб.'

        self.widgets = [self.food_exclude_choice, self.food_exclude_button, self.amount_hint, self.price_hint,
                        self.total_hint, self.dish_del_counter, self.food_exclusion_image, self.cart_delete,
                        self.total_order, self.total_summ]

    def switch_image(self, text):
        link = Image_Switch(text)
        try:
            self.food_exclusion_image.source = link
        except Exception as e:
            pass

    def triple(self, text):
        self.food_exclude_choice.select(str(text))
        self.switch_image(str(text).split()[0])
        self.amount_hint.text = str(food_amound_price[str(text)][0])
        self.price_hint.text = str(food_amound_price[str(text)][1])
        self.total_hint.text = str(food_cart[str(text)])

    def deleting_dishes(self):
        try:
            text = str(self.food_exclude_button.text)
            minus_amount = self.dish_del_counter.text
            food_amound_price[text][0] = max(int(food_amound_price[text][0]) - int(minus_amount), 0)
            a, b = food_amound_price[text]
            food_cart[text] = int(a) * int(b)
        except Exception as e:
            print(e)
            pass
        self.reload()

    def reload(self):
        for i in self.widgets:
            self.remove_widget(i)
        self.__init__()
