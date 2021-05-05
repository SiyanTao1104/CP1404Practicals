from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class NameApp(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "list of names"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root


NameApp().run()