'''import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(mygrid, self).__init__(**kwargs)
        self.cols=1
     
        self.inside = GridLayout()
        self.inside.cols = 2 
        
        self.inside.add_widget(Label(text='Name: '))
        self.name = TextInput(multiline = False)
        self.inside.add_widget(self.name)
        
        self.inside.add_widget(Label(text='Last name: '))
        self.lastname = TextInput(multiline = False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        
        self.submit = Button(text='submit', font_size=40 )
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    def pressed(self, instance):    
        name = self.name.text
        last = self.lastname.text
        email = self.email.text
        
        print('Name: ', name, "last name:", last,'Email:', email)
        self.name.text = ''
        self.lastname.text = ''
        self.email.text = ''

class myapp(App):
    def build(self):
        return mygrid()


if __name__ == '__main__':
    myapp().run()    


#this is for design
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class mygrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def btn(self):
        print('Name: ', self.name.text, 'email: ', self.email.text)
        self.name.text = '' 
        self.email.text= ''
    
def btn(instance):    
    print('run')

class myapp(App):
    def build(self):
        return mygrid()
    
    
if __name__ == '__main__':
    myapp().run()
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout   

class mehapp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    mehapp().run()

import kivy
from kivy.app  import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class touch(Widget):
    btn = ObjectProperty(None)
    
    def on_touch_down(self, touch):
        print('Mouse down', touch)
        self.btn.opacity = 0.3
    
    def on_touch_move(self, touch):
        print('Mouse move', touch)
    
    
    def on_touch_up(self, touch):
        print('Mouse up', touch)
        self.btn.opacity = 1
        
    
    

class mapp(App):
    def build(self):
        return touch()
    
if __name__ == '__main__':
    mapp().run()

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from docutils.nodes import line

class Touch(Widget):
    def __init__(self ,**kwargs):    
        super(Touch, self).__init__(**kwargs)
        
        with self.canvas:
            Color(0, 1, 0, .5, mods='rgbs')
            Line(points=(20,30, 400 ,500,60,500 ))
            Color(1, 0, 0, .5, mods='rgbs')
            self.rect = Rectangle(pos=(0,0), size=(50,50))

    
    
    def on_touch_down(self, touch): 
        self.rect.pos = touch.pos
        print("Mouse Down", touch)
        
    def on_touch_move(self, touch):
        self.rect.pos = touch.pos
        print('Mouse move', touch)
   
        
class myapp(App):
    def build (self):
        return Touch()
    
    
if __name__=='__main__':
    myapp().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("mol.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
'''

import kivy
from kivy.app import App
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass


class melApp(App):
    def build(self):
        return Widgets()


def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()


if __name__ == "__main__":
    melApp().run()