"""
diplomska rabota
Viktorija Dimova
"""

from random import random, randint
from functools import partial
from datetime import datetime

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.graphics import Color
from kivy.graphics.vertex_instructions import *
from kivy.properties import BooleanProperty, StringProperty, NumericProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton

from kivy.lang import Builder
from kivy.logger import Logger

from eyes import Eyes
from nose import Nose
from mouth import Mouth

class ItarPejoInit(Image):
    eyes = ObjectProperty(None)
    nose = ObjectProperty(None)
    mouth = ObjectProperty(None)
    
    def __init__(self, *args, **kwargs):
        self.size = (Window.width, Window.height)

        super(ItarPejoInit, self).__init__(*args, **kwargs)
        self.start.bind(on_press=self.set_objects)
        self.neutral_face.bind(on_press=self.transition_to_neutral)
        self.happy_face.bind(on_press=self.transition_to_happy)
        self.sad_face.bind(on_press=self.transition_to_sad)
        self.angry_face.bind(on_press=self.transition_to_angry)
        self.cry_face.bind(on_press=self.transition_to_cry)

    def transition_to_neutral(self):
		pass
	
    def transition_to_happy(self):
		pass
	
    def transition_to_sad(self):
		pass
	
    def transition_to_angry(self):
		pass
	
    def transition_to_cry(self):
		pass
        
    def set_objects(self):
        Builder.load_file("main.kv")
        self.size = (Window.width, Window.height)
        self.eyes = Eyes(box=[self.game_area.x, self.game_area.y + 65, 
                              self.game_area.width, self.game_area.height - 175])

        self.nose = Nose(box=[self.game_area.x, self.game_area.y + 65, 
                              self.game_area.width, self.game_area.height - 175])        
 
        self.mouth = Mouth(box=[self.game_area.x, self.game_area.y + 65, 
                              self.game_area.width, self.game_area.height - 175])

        self.game_area.add_widget(self.eyes, index=1)
        self.eyes.active = True

        self.game_area.add_widget(self.mouth, index=1)
        self.mouth.active = True
#        self.auto_bring_to_front(self.mouth) # nekoja vakva kombinacija da se napravi :)
         
        self.game_area.add_widget(self.nose, index=1)
        self.nose.active = True	
        
#    def play(self, *largs):
#    
#        self.game_area.add_widget(self.eyes, index=1)
#        self.eyes.active = True
#
#        self.game_area.add_widget(self.mouth, index=1)
#        self.mouth.active = True
#        self.auto_bring_to_front(self.mouth) # nekoja vakva kombinacija da se napravi :)
         
#        self.game_area.add_widget(self.nose, index=1)
#        self.nose.active = True
        
#        self.start_time = datetime.now() 
        
        
    def the_end(self, instance):
        self.pause()
        self.victory_screen.calories_score.text = str(self.eyes.total_calories)
        self.victory_screen.junk_score.text = str(self.eyes.junk_swallowed)
        self.victory_screen.total_score.text = "On %s a fish was caught, size of %s, which well fed the people of the world for %s days straight!" % (datetime.now().strftime("%B %d, %Y"), self.eyes.rank[self.eyes.obese_lvl - 1], (datetime.now() - self.start_time).seconds )
        self.victory_screen.open()


        
class ItarPejo(App):
    Builder.load_file("intro.kv")
    def __init__(self, *args, **kwargs):
        super(ItarPejo, self).__init__(*args, **kwargs)

    def build(self):
        Builder.load_file("intro.kv")
        self.intro = ItarPejoInit()
#        self.intro.go_btn.bind(on_release=self._transition_outof_intro)
        return self.intro
            
if __name__ == '__main__':
    ItarPejo().run()
    
