"""
    nos 45x23
"""
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.properties import BooleanProperty

class Nose(Widget):
    active = BooleanProperty(False)
    def __init__(self, image = "images/nose.png", box = [0, 0, 100, 100], **kwargs):

        self.direction = Vector(-1, 0)
        self.angle = 1
        self.size = (30,30)
        self.box = box
        self.center = (Window.width/2, Window.height)
        self.image = Image(source=image, allow_stretch=True, size=self.size)
        self.image.center_x = 405
        self.image.center_y = 275
        self.target_pos = self.center
        super(Nose, self).__init__(**kwargs)
        self.add_widget(self.image)
    
    
#    active = BooleanProperty(False) 
#    def __init__(self, image = "images/nose.png", box = [0, 0, 100, 100], **kwargs):
#        self.direction = Vector(-1, 0)
#        self.angle = 1
#        self.size = (30,30)
#        self.box = box
#        self.center = (Window.width/2, Window.height)
#        self.image = Image(source=image, allow_stretch=True, size=self.size)
#        self.image.texture = self.image.texture.get_region(0, 0, 45, 23)
#        self.target_pos = self.center
#        super(Nose, self).__init__(**kwargs)
#        self.add_widget(self.image)
##        self.register_event_type('on_death')
#        # Dynamic entry
##        self.bind(active=lambda instance, value: Animation(y=Window.height - 620, t="out_back", d=1.2).start(instance) if value else True)
#        self.bind(active=lambda instance, value: Animation(y=Window.height - 320, t="out_back", d=1.2).start(instance) if value else True)
   
