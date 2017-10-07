"""

"""

from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.properties import BooleanProperty


class Eyes(Widget):
    active = BooleanProperty(False)
    def __init__(self, image = "images/eyes_normal.png", box = [0, 0, 100, 100], **kwargs):

        self.direction = Vector(-1, 0)
        self.angle = 1
        self.size = (660,700)
        self.box = box
        self.center = (Window.width/2, Window.height)
        self.image = Image(source=image, allow_stretch=True, size=self.size)
        self.image.center_x = 405
        self.image.center_y = 370
        self.target_pos = self.center
        super(Eyes, self).__init__(**kwargs)
        self.add_widget(self.image)     