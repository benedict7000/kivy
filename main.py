from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

KV = """
#:kivy 2.0

MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: '20dp'
        spacing: '20dp'
        
        MDLabel:
            text: 'Welcome to KivyMD'
            font_style: 'H4'
            halign: 'center'
        
        MDLabel:
            text: 'This is your first KivyMD app'
            halign: 'center'
        
        MDRaisedButton:
            text: 'Click Me'
            size_hint_x: 1
            on_press: app.on_button_press()
"""


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)
    
    def on_button_press(self):
        print("Button pressed!")


if __name__ == '__main__':
    MyApp().run()
