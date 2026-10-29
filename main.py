from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello Sourabh! APK Ready Hai")

MyApp().run()