import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.uix.label import Label

class myApp(App):
    def build(self):
        return Label(text='Hello cruel world')

if __name__ == '__main__':
    myApp().run()
