"""

"""

from math import sin, cos, radians

from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.properties import BooleanProperty, NumericProperty, BoundedNumericProperty


class Eyes(Scatter):
    active = BooleanProperty(False)
    alive = BooleanProperty(True)
    navigating = BooleanProperty(False)
    
    # Max level 8
    obese_lvl = BoundedNumericProperty(1, min=0, max=8)
    

    def __init__(self, image = "images/eyes_normal.png", box = [0, 0, 100, 100], **kwargs):
        self.direction = Vector(-1, 0)
        self.angle = 5
        
        self.size = (700,700)
        self.box = box
        self.center = (Window.width/2, Window.height)
        self.image = Image(source=image, allow_stretch=True, size=self.size)
        
        self.image.texture = self.image.texture.get_region(0, 0, 316, 168)
        
        self.target_pos = self.center
        
        super(Eyes, self).__init__(**kwargs)
        self.add_widget(self.image)
        
        self.register_event_type('on_death')
        
        # Every living creature consumes own self
#        self.bind(active=lambda instance, value: Clock.schedule_interval(instance.consume_calories, 0.5) if value else Clock.unschedule(instance.consume_calories))
        # Dynamic entry
        self.bind(active=lambda instance, value: Animation(y=Window.height - 520, t="out_back", d=1.2).start(instance) if value else True)
        # Too many calories make you obese
#        self.bind(total_calories=self.lvlup)
                
    def swim(self, dt):
        anim = Animation(center=self.target_pos, d=0.1)
        anim.start(self)    
        
    def on_death(self):
        self.alive = False
        self.active = False
            
    def on_touch_down(self, touch):
        if not self.collide_point(touch.x, touch.y):
            return False    
        if self.active and self.alive:
            Clock.schedule_interval(self.swim, 0.1)  
            self.navigating = True      
        
    def on_touch_move(self, touch):
        if not self.alive:
            return False

        # Bounding box
        x = touch.x
        if touch.x >= self.box[2]:
            x = self.box[2]
        elif touch.x <= self.box[0]:
            x = self.box[0]
            
        y = touch.y
        if touch.y >= self.box[3]:
            y = self.box[3]
        elif touch.y <= self.box[1]:
            y = self.box[1]
            
        self.target_pos = (x, y)
        
    def on_touch_up(self, touch):
        if not self.navigating:
            return False
        
        self.navigating = False
        
        Clock.unschedule(self.swim)
        
        speed = Vector((0,0)).distance((touch.dsx, touch.dsy)) * 5000
        
        angle = self.direction.angle((touch.dsx, touch.dsy))
        if angle < 0:
            angle = 360 + angle
        angle = 270 - angle

        anim = Animation(center=(self.target_pos[0] + sin(radians(angle)) * speed,self.target_pos[1] - cos(radians(angle)) * speed), t="out_cubic", d=0.6)
        anim.start(self)
        
