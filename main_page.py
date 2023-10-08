from registration import *
from logining import *
from main_menu import *
from adminLogin import *
from kivymd.uix.screen import MDScreen


Builder.load_file('registrate.kv')
Builder.load_file('mainPage.kv')
LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts\RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts\Finlandica-Regular.ttf')


class TestApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LogApp(name='Log'))
        sm.add_widget(RegApp(name='Reg'))
        sm.add_widget(MainMenuApp(name='Menu'))
        sm.add_widget(AdminLogApp(name="AdminLog"))
        sm.current = 'AdminLog'
        return sm


if __name__ == '__main__':
    TestApp().run()
