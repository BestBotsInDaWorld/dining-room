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
    pass


class PointsApp(Screen):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SomePointApp(name='SomePoint'))
        sm.add_widget(PointsApp(name='Points'))
        sm.current = 'Points'
        return sm
