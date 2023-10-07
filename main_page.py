from registration import *
from logining import *

Builder.load_file('registrate.kv')
LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts\RuslanDisplay-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts\Finlandica-Regular.ttf')


class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(RegApp(name='Reg'))
        sm.add_widget(LogApp(name='Log'))
        sm.current = 'Log'
        return sm


if __name__ == '__main__':
    TestApp().run()
