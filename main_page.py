from registration import *
from logining import *
from main_menu import *

Builder.load_file('registrate.kv')
Builder.load_file('mainPage.kv')
LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts\RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts\Finlandica-Regular.ttf')


class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LogApp(name='Log'))
        sm.add_widget(RegApp(name='Reg'))
        sm.add_widget(MainMenuApp(name='Menu'))
        sm.current = 'Menu'
        return sm


if __name__ == '__main__':
    TestApp().run()
