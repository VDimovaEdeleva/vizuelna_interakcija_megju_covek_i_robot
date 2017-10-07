"""
    mouth 286x86
"""
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.vector import Vector
from kivy.properties import BooleanProperty


class Mouth(Widget, Animation):
    active = BooleanProperty(False)
    def __init__(self, image = "images/mouth-happy.png", box = [0, 0, 100, 100], **kwargs):

        self.direction = Vector(-1, 0)
        self.angle = 1
        self.size = (610,700)
        self.box = box
        self.center = (Window.width/2, Window.height)
        self.image = Image(source=image, allow_stretch=True, size=self.size)
        self.image.center_x = 405
        self.image.center_y = 255
        self.target_pos = self.center
        super(Mouth, self).__init__(**kwargs)
        self.add_widget(self.image)
