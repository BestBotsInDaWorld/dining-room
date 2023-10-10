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
Builder.load_file('mainPage.kv')

LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts/RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts/Finlandica-Regular.ttf')
LabelBase.register(name='MartianMono-SemiBold',
                   fn_regular=r'fonts/MartianMono-SemiBold.ttf')

class MainMenuApp(Screen):
    pass