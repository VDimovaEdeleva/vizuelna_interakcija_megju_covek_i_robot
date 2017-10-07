#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 09:25:22 2017

@author: viktorija
"""


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.vector import Vector
from kivy.uix.screenmanager import (ScreenManager, Screen)
from kivy.animation import Animation
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics.context_instructions import Rotate
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.graphics import Color

#from kivy.properties import ObjectProperty

from kivy.core.window import Window
Window.size = (1920/2,1080/2)
Window.clearcolor = (1, 0.9, 0.65, 1) #za menuvanje na pozadina



class AddLocationForm(RelativeLayout):
    started = BooleanProperty(False)
    eyebrows_removed = BooleanProperty(False)
    nose_removed = BooleanProperty(False)
    def start(self, eyes_normal = "images/eyes_normal.png", 
              eyes_sad = "images/eyes_sad.png", 
              eyes_cry = "images/eyes_cry.png", 
              mouth_happy = "images/mouth-happy.png", 
              mouth_neutral = "images/mouth-neutral.png",
              mouth_mad = "images/mouth-mad.png",
              mouth_sad = "images/mouth-very-sad.png",
              mouth_A = "images/mouth-A.png",
              mouth_E = "images/mouth-E.png",
              mouth_I = "images/mouth-I.png",
              mouth_O = "images/mouth-O.png",
              mouth_U = "images/mouth-U.png",
              nose = "images/nose.png",
              eyebrow_left = "images/eyebrow-left.png",
              eyebrow_right = "images/eyebrow-right.png",
              box = [0, 0, 100, 100], **kwargs):
        if (self.started == False):
            self.started = True
            self.direction = Vector(-1, 0)
            self.angle = 1
            self.size = (660,700)
            self.box = box
            self.center = (Window.width/2, Window.height/2)
            
            self.eyes_normal = Image(source=eyes_normal, allow_stretch=True, size=self.size)
            self.eyes_sad = Image(source=eyes_sad, allow_stretch=True, size=self.size)
            self.eyes_cry = Image(source=eyes_cry, allow_stretch=True, size=self.size)
            self.eyes = self.eyes_normal
            self.eyes.center_x = (Window.width)/2
            self.eyes.center_y = (Window.height)/2 
            self.target_pos = self.center
            self.add_widget(self.eyes)  
            
            self.mouth_happy = Image(source=mouth_happy, allow_stretch=True, size=self.size)
            self.mouth_sad = Image(source=mouth_sad, allow_stretch=True, size=self.size)
            self.mouth_mad = Image(source=mouth_mad, allow_stretch=True, size=self.size)
            self.mouth_neutral = Image(source=mouth_neutral, allow_stretch=True, size=self.size)
            self.mouth_A = Image(source=mouth_A, allow_stretch=True, size=self.size)
            self.mouth_E = Image(source=mouth_E, allow_stretch=True, size=self.size)
            self.mouth_I = Image(source=mouth_I, allow_stretch=True, size=self.size)
            self.mouth_O = Image(source=mouth_O, allow_stretch=True, size=self.size)
            self.mouth_U = Image(source=mouth_U, allow_stretch=True, size=self.size)
            self.mouth = self.mouth_neutral
            self.mouth.center_x = (Window.width)/2
            self.mouth.center_y = (Window.height)/2 
            self.target_pos = self.center
            self.add_widget(self.mouth)
            
    #        self.direction = Vector(-1, 0)
    #        self.angle = 1
    #        self.size = (30,30)
    #        self.box = box
    #        self.center = (Window.width/2, Window.height)
            self.nose = Image(source=nose, allow_stretch=True, size=self.size)
            self.nose.center_x = (Window.width)/2
    #        self.nose.center_y = 275
            self.nose.center_y = (Window.height)/2 
            self.target_pos = self.center
            self.add_widget(self.nose)       
            
            self.eyebrow_left = Image(source=eyebrow_left, allow_stretch=True, size=self.size)
            self.eyebrow_left.center_x = (Window.width)/2
            self.eyebrow_left.center_y = (Window.height)/2 
            self.target_pos = self.center
            self.add_widget(self.eyebrow_left)
            
    #        self.size = (15,3)
            self.eyebrow_right = Image(source=eyebrow_right, allow_stretch=True, size=self.size)
            self.eyebrow_right.center_x = (Window.width)/2
            self.eyebrow_right.center_y = (Window.height)/2
            self.target_pos = self.center
            self.add_widget(self.eyebrow_right)
            
        print("start")
        
    def transition_to_neutral(self):
        self.remove_widget(self.eyes)
        self.eyes = self.eyes_normal
        if self.eyebrows_removed:
            self.add_widget(self.eyebrow_right)
            self.add_widget(self.eyebrow_left)
            self.eyebrows_removed = False
        if self.nose_removed:
            self.add_widget(self.nose)
            self.nose_removed = False
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_neutral
        self.eyes = self.eyes_normal
        self.add_widget(self.eyes)
        self.add_widget(self.mouth)
        print("2neutral")
	
    def transition_to_happy(self):
        self.remove_widget(self.eyes)
        self.eyes = self.eyes_normal
        if self.eyebrows_removed:
            self.add_widget(self.eyebrow_right)
            self.add_widget(self.eyebrow_left)
            self.eyebrows_removed = False
        if self.nose_removed:
            self.add_widget(self.nose)
            self.nose_removed = False
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_happy
        self.eyes = self.eyes_normal
        self.add_widget(self.eyes)
        self.add_widget(self.mouth)
        print("2happy")
	
    def transition_to_sad(self):
        self.remove_widget(self.eyes)
#        self.on_opacity(self.eyes)
        self.eyes = self.eyes_sad
        if (self.eyebrows_removed == False):
            self.remove_widget(self.eyebrow_right)
            self.remove_widget(self.eyebrow_left)
            self.eyebrows_removed = True
        if self.nose_removed == False:
            self.remove_widget(self.nose)
            self.nose_removed = True
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_sad
        self.eyes = self.eyes_sad
        self.add_widget(self.eyes)
        self.add_widget(self.mouth)
#        self.fader = ScreenFader(size=Window.size)
#        anim = Animation(alpha = 0.0, d=0.8)
#        anim.bind(on_complete=lambda instance, value: self.eyes(self.fader))
#        anim.start(self.fader)
        print("2sad")
	
    def transition_to_angry(self):
        self.remove_widget(self.eyes)
        if (self.eyebrows_removed):
            self.add_widget(self.eyebrow_right)
            self.add_widget(self.eyebrow_left)
            self.eyebrows_removed = False
        if self.nose_removed:
            self.add_widget(self.nose)
            self.nose_removed = False
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_mad
        self.eyes = self.eyes_normal
        self.add_widget(self.eyes)
        self.add_widget(self.mouth)
        print("2angry")
	
    def transition_to_cry(self):
        self.remove_widget(self.eyes)
        if (self.eyebrows_removed == False):
            self.remove_widget(self.eyebrow_right)
            self.remove_widget(self.eyebrow_left)
            self.eyebrows_removed = True
        if self.nose_removed == False:
            self.remove_widget(self.nose)
            self.nose_removed = True
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_sad
        self.eyes = self.eyes_cry
        self.add_widget(self.eyes)
        self.add_widget(self.mouth)
        print("2cry")
        
    def a_sound(self):
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_A
        self.add_widget(self.mouth)
        print("Asound")      
        
    def e_sound(self):
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_E
        self.add_widget(self.mouth)
        print("Esound")  
        
    def i_sound(self):
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_I
        self.add_widget(self.mouth)
        print("Isound")  
        
    def o_sound(self):
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_O
        self.add_widget(self.mouth)
        print("Osound")  
        
    def u_sound(self):
        self.remove_widget(self.mouth)
        self.mouth = self.mouth_U
        self.add_widget(self.mouth)
        print("Usound")  

class ItarPejo(App):
    pass

class ScreenFader(Widget):

    alpha = NumericProperty(0.0)
    
    def __init__(self, alpha=0, **kwargs):
        super(ScreenFader, self).__init__(**kwargs)
        self.bind(alpha=self.on_alpha)
        self.alpha = alpha
            
    def on_alpha(self, instance, value):
        self.canvas.clear()
        with self.canvas:
            Color(1, 0.9, 0.65, value)
            Rectangle(pos=self.pos, size=self.size)

if __name__ == '__main__':
        ItarPejo().run()