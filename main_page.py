from registration import *
from logining import *
from main_menu import *
from adminLogin import *
from Admin_panel import *
from point_choice import *
from other_functions import *
from Points import *
from food_menu import *
from kivymd.uix.screen import MDScreen


Builder.load_file('registrate.kv')
Builder.load_file('mainPage.kv')
LabelBase.register(name='RubikMonoOne-Regular',
                   fn_regular=r'fonts/RubikMonoOne-Regular.ttf')
LabelBase.register(name='Finlandica-Regular',
                   fn_regular=r'fonts/Finlandica-Regular.ttf')


class TestApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LogApp(name='Log'))
        sm.add_widget(RegApp(name='Reg'))
        sm.add_widget(MainMenuApp(name='Menu'))
        sm.add_widget(AdminLogApp(name="AdminLog"))
        sm.add_widget(PointChoiceApp(name="PointChoice"))
        sm.add_widget(AboutUsApp(name="AboutUs"))
        sm.add_widget(OtherSystemsApp(name="OtherSystems"))
        sm.add_widget(AdminPanelApp(name="AdminPanel"))
        sm.add_widget(BalanceApp(name="Balance"))
        sm.add_widget(DepositApp(name="Deposit"))
        sm.add_widget(SomePointApp(name="SomePoint"))
        sm.add_widget(FoodMenuApp(name="FoodMenu"))
        sm.add_widget(FoodCartApp(name="FoodCart"))
        sm.add_widget(NewAndHitsApp(name="NewAndHits"))
        sm.current = 'Log'
        return sm


if __name__ == '__main__':
    TestApp().run()
