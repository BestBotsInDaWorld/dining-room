import kivy
import jwt
import uuid
import datetime
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
#from databaseconnect import *


kv = Builder.load_file('reg.kv')

class WindowManager(ScreenManager):
    pass


class MainMenu(Screen):
    def btn_click(self):
        self.money.text = '50'


class Points(Screen):
    def checkbox_click(self, instance, value):
        pass


class MenuPoint1(Screen):
    pass


class MenuPoint2(Screen):
    pass


class MenuPoint3(Screen):
    pass


class MenuApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MenuApp().run()
