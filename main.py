from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.vector import Vector
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty, BooleanProperty
from kivy.graphics import Color
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.video import Video

from kivy.core.window import Window
Window.size = (1920/2,1080/2)
Window.clearcolor = (1, 0.9, 0.65, 1) #za menuvanje na pozadina

class Objekti(FloatLayout,BoxLayout):
    started = BooleanProperty(False)
    eyebrows_removed = BooleanProperty(False)
    nose_removed = BooleanProperty(False)
    active = BooleanProperty(False)
    animation = ObjectProperty(None, allow_none = True)
    present_state = StringProperty()
    previous_state = StringProperty()
    video_on = BooleanProperty(False)
    emotion_on = BooleanProperty(False)
    emotion_last = StringProperty()

    def start(self, eyes_normal = "images/eyes_normal.png", 
              eyes_sad = "images/eyes_sad.png", 
              eyes_cry = "images/eyes_cry.png", 
              eyes_angry = "images/eyes_angry.png", 
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
              neutral2sad = "neutral2sad.avi",
              neutral2happy = "neutral2happy.avi",
              happy2neutral = "happy2neutral.avi",
              neutral2angry = "neutral2angry.avi",
              sad2neutral = "sad2neutral.avi",
              sad2cry = "sad2cry.avi",
              cry2sad = "cry2sad.avi",
              angry2neutral = "angry2neutral.avi",              
              box = [0, 0, 100, 100], **kwargs):
        
        super(Objekti, self).__init__(**kwargs)
        if (self.started == False):
            print 'in start'
            self.started = True
            self.direction = Vector(-1, 0)
            self.angle = 1
            self.size = (660,700)
            self.box = box
            self.center = (Window.width/2, Window.height/2)
            print 'load'
            self.neutral2sad = Video(source = neutral2sad, allow_fullscreen=False)
            self.neutral2happy = Video(source = neutral2happy, allow_fullscreen=False)
            self.happy2neutral = Video(source = happy2neutral, allow_fullscreen=False)
            self.neutral2angry = Video(source = neutral2angry, allow_fullscreen=False)
            self.sad2neutral = Video(source = sad2neutral, allow_fullscreen=False)
            self.sad2cry = Video(source = sad2cry, allow_fullscreen=False)
            self.cry2sad = Video(source = cry2sad, allow_fullscreen=False)
            self.angry2neutral = Video(source = angry2neutral, allow_fullscreen=False)
            
            self.eyes_normal = Image(source=eyes_normal, allow_stretch=True, size=self.size)
            self.eyes_sad = Image(source=eyes_sad, allow_stretch=True, size=self.size)
            self.eyes_cry = Image(source=eyes_cry, allow_stretch=True, size=self.size)
            self.eyes_angry = Image(source=eyes_angry, allow_stretch=True, size=self.size)
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

            self.nose = Image(source=nose, allow_stretch=True, size=self.size)
            self.nose.center_x = (Window.width)/2
            self.nose.center_y = (Window.height)/2 
            self.target_pos = self.center
            self.add_widget(self.nose)       
            
            self.eyebrow_left = Image(source=eyebrow_left, allow_stretch=True, size=self.size)
            self.eyebrow_left.center_x = (Window.width)/2
            self.eyebrow_left.center_y = (Window.height)/2 
            self.target_pos = self.center
            self.add_widget(self.eyebrow_left)

            self.eyebrow_right = Image(source=eyebrow_right, allow_stretch=True, size=self.size)
            self.eyebrow_right.center_x = (Window.width)/2
            self.eyebrow_right.center_y = (Window.height)/2
            self.target_pos = self.center
            self.add_widget(self.eyebrow_right)
            
            self.emotion_last = "neutral"
            self.animation = Animation(y=33, d=6)
            self.present_state = "neutral"
            self.video_on == False 
            print("start")
        
    def transition_to_neutral(self):
        if self.video_on == True :
            self.remove_widget(self.videoo)
            self.video_on = False
        if self.present_state == "sad" :
            self.videoo = self.sad2neutral
        if self.present_state == "happy" :
            self.videoo = self.happy2neutral
        if self.present_state == "angry" :
            self.videoo = self.angry2neutral 
        if self.present_state == "cry" :
            self.transition_to_sad() 
            self.remove_widget(self.videoo)
        self.add_widget(self.videoo)
        self.videoo.play = True
        self.video_on = True
        self.previous_state = self.present_state        
        self.present_state = "neutral"
        
        print("2neutral")
	
    def transition_to_happy(self):
        if self.video_on == True :
            self.remove_widget(self.videoo)
            self.video_on = False 
        if self.present_state != "neutral" :
            self.video_on == False
            self.transition_to_neutral() 
            self.remove_widget(self.videoo)
        self.videoo = self.neutral2happy
        self.add_widget(self.videoo)
        self.videoo.play = True
        self.video_on = True
        self.previous_state = self.present_state        
        self.present_state = "happy"        
        
        print("2happy")
	
    def transition_to_sad(self):
        if self.video_on == True :
            self.remove_widget(self.videoo)
            self.video_on = False
        if self.present_state != "neutral" :
            if self.present_state != "cry" :
                self.video_on == False
                self.transition_to_neutral()
                self.remove_widget(self.videoo)            
        if self.present_state == "neutral" :
            self.videoo = self.neutral2sad
            self.remove_widget(self.videoo)
        if self.present_state == "cry" :
            self.videoo = self.cry2sad
            self.remove_widget(self.videoo)
            print "cry2sad"
            
        self.add_widget(self.videoo)
        self.video_on = True
        self.videoo.play = True
        self.previous_state = self.present_state        
        self.present_state = "sad"
        
        print("2sad")
	
    def transition_to_angry(self):
        if self.video_on == True :
            self.remove_widget(self.videoo)
            self.video_on = False  
        if self.present_state != "neutral" :
            self.video_on == False
            self.transition_to_neutral() 
            self.remove_widget(self.videoo)            
        self.videoo = self.neutral2angry           
        self.add_widget(self.videoo)
        self.videoo.play = True
        self.video_on = True
        self.previous_state = self.present_state
        self.present_state = "angry"        
        
        print("2angry")
	
        
    def transition_to_cry(self):
        if self.video_on == True :
            self.remove_widget(self.videoo)
            self.video_on = False   
        if self.present_state != "sad" :
            self.video_on == False
            self.transition_to_sad()
            self.remove_widget(self.videoo)             
        self.videoo = self.sad2cry          
        self.add_widget(self.videoo)
        self.videoo.play = True
        self.video_on = True
        self.previous_state = self.present_state        
        self.present_state = "cry"           
        

    def add_emotion(self):
        if self.emotion_last == "neutral" or self.emotion_last == "happy":
            self.eyes = self.eyes_normal
            self.add_widget(self.nose)           
            self.add_widget(self.eyes)
            print "add neutral"
            self.add_widget(self.eyebrow_left)
            self.add_widget(self.eyebrow_right)
            
        if self.emotion_last == "cry" :
            self.eyes = self.eyes_cry    
            print "add cry"
            self.add_widget(self.eyes)
            
        if self.emotion_last == "sad" :
            self.eyes = self.eyes_sad      
            print "add sad"
            self.add_widget(self.eyes)
            
        if self.emotion_last == "angry" :
            self.eyes = self.eyes_angry      
            self.add_widget(self.eyes)
            print "add angry"

            
    def remove_emotion(self):
        if self.emotion_last == "neutral" or self.emotion_last == "happy":
            self.remove_widget(self.nose)           
            self.remove_widget(self.eyes)
            self.remove_widget(self.eyebrow_left)
            self.remove_widget(self.eyebrow_right)
            
        if self.emotion_last == "cry" :     
            self.remove_widget(self.eyes)
            
        if self.emotion_last == "sad" :
            self.remove_widget(self.eyes)
            
        if self.emotion_last == "angry" :
            self.remove_widget(self.eyes)     
        
            
    def a_sound(self):
        self.remove_emotion()
        if self.video_on == True :
            self.video_on = False
            self.remove_widget(self.videoo) 
        self.remove_widget(self.mouth)
        self.emotion_last = self.present_state
        self.add_emotion()
        self.mouth = self.mouth_A
        self.add_widget(self.mouth)
        print("Asound")      
        
        
    def e_sound(self):
        self.remove_emotion()
        if self.video_on == True :
            self.video_on = False
            self.remove_widget(self.videoo) 
        self.remove_widget(self.mouth)
        self.emotion_last = self.present_state
        self.add_emotion()
        self.mouth = self.mouth_E
        self.add_widget(self.mouth)
        print("Esound")  
        
        
    def i_sound(self):
        self.remove_emotion()
        if self.video_on == True :
            self.video_on = False
            self.remove_widget(self.videoo) 
        self.remove_widget(self.mouth)
        self.emotion_last = self.present_state
        self.add_emotion()
        self.emotion_last = self.present_state
        self.mouth = self.mouth_I
        self.add_widget(self.mouth)
        print("Isound")  
        
        
    def o_sound(self):
        self.remove_emotion()
        if self.video_on == True :
            self.video_on = False
            self.remove_widget(self.videoo) 
        self.remove_widget(self.mouth)
        self.emotion_last = self.present_state
        self.add_emotion()
        self.mouth = self.mouth_O
        self.add_widget(self.mouth)
        print("Osound")  
        
        
    def u_sound(self):
        self.remove_emotion()
        if self.video_on == True :
            self.video_on = False
            self.remove_widget(self.videoo) 
        self.remove_widget(self.mouth)  
        self.emotion_last = self.present_state
        self.add_emotion()
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