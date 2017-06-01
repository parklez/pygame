#############################
#       User Config
#############################
resolution = (800, 600)
fullscreen = False
debug = False

#############################
#       Modules
#############################
import os
import math

import pygame

from colors import *

#############################
#       Init
#############################
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()

#############################
#       Scaling
#############################
def engine_scale(resolution):
    global scale, di, xu, yu
    scale = 16
    di = math.sqrt(resolution[0]**2+resolution[1]**2)
    xu = resolution[0]/scale
    yu = resolution[1]/scale
    
engine_scale(resolution)

#############################
#       Fonts
#############################
menufont = pygame.font.Font(None, 40)
#font = pygame.font.SysFont("Comic Sans MS", 15)
font = pygame.font.Font(None, 20)

#############################
#       Classes
#############################

TextButton_list = []
messagebox_list = []

class MouseCollision():
    'Checks if mouse is over a rectangle.'
    def __init__(self, rect, mouse=[0,0]):
        self.mouse = mouse
        self.rect = rect
        self.istouched = False
        
    def touching(self):
        if self.mouse[0] > self.rect[0] and self.mouse[0] < (self.rect[0] + self.rect[2]) and \
           self.mouse[1] > self.rect[1] and self.mouse[1] < (self.rect[1] + self.rect[3]):       
            self.istouched = True
        else:
            self.istouched = False

            
class TextButton(MouseCollision):
    '''Creates a button that lights up and plays a sound when mouse is over 
    the rectangle with a text. It can also be activated/triggered.'''
    def __init__(self, screen, text, rect, active=True, triggered=False, debug=False):
        MouseCollision.__init__(self, rect)
        self.text = text
        self.isactive = active
        self.istriggered = triggered
        self.screen = screen
        self.roll = pygame.mixer.Sound('sound/UI/buttonrollover.wav')
        self.click = pygame.mixer.Sound('sound/UI/buttonclick.wav')
        self.played = False
        self.debug = debug
        TextButton_list.append(self)

    def rollsound(self):
        if self.played == False:
            self.roll.play()
            self.played = True
            
    def clicksound(self):
        self.click.play()

    def update(self):
        self.touching()
        
        if self.istouched:
            self.rendertext = menufont.render(self.text, True, green)
            self.rollsound()
        else:
            self.rendertext = menufont.render(self.text, True, white)
            self.played = False

        if self.debug:
            pygame.draw.rect(self.screen, yellow, self.rect)
            self.variables = font.render('isactive: ' + str(self.isactive) + ' istriggered: ' + str(self.istriggered) \
                                    , True, white, black)
            
    def render(self):
        self.screen.blit(self.rendertext, (self.rect[0],self.rect[1]))

        if self.debug:
            self.screen.blit(self.variables,(self.rect[0]+self.rect[2],self.rect[1]))

            
class MessageBox(MouseCollision):
    'Creates a window that can be closed, focused, and dragged around, just like in a regular OS.'
    def __init__(self, screen, title='Default title', message='Default text', center_pos=(xu*8,yu*8),\
                 active=True, focus=True, debug=False):

        self.screen = screen
        self.title = title
        self.message = message
        
        self.rect = [center_pos[0] - (font.size(message)[0]+40)/2, \
                     center_pos[1] - ((font.size(message)[1] + font.size(title)[1]) + 40)/2, \
                     font.size(message)[0]+40, \
                     font.size(message)[1] + font.size(title)[1] + 40]

        MouseCollision.__init__(self, self.rect)
        
        self.isactive = active
        self.isfocused = focus
        self.istouched = False
        
        self.cb_istouched = False
        self.cb_rect = [self.rect[0]+6,self.rect[1]+6,18,18]
        
        self.isdragged = False
        self.gap = []
        
        self.open = pygame.mixer.Sound('sound/UI/hint.wav')
        self.close = pygame.mixer.Sound('sound/UI/buttonclickrelease.wav')
        self.played = False

        self.debug = debug
        
        messagebox_list.append(self)
        
    def drag(self):
        'I felt like a genious when I figured out how to make this function.'
        self.rect[0] = self.mouse[0] + (self.gap[0] - self.gap[2])
        self.rect[1] = self.mouse[1] + (self.gap[1] - self.gap[3])

    def cb_touching(self):
        'cb stands for "close button".'
        if self.mouse[0] > self.cb_rect[0] and self.mouse[0] < (self.cb_rect[0] + self.cb_rect[2]) and \
           self.mouse[1] > self.cb_rect[1] and self.mouse[1] < (self.cb_rect[1] + self.cb_rect[3]):       
            self.cb_istouched = True
        else:
            self.cb_istouched = False
            
    def update(self):
        self.touching()
        self.cb_touching()
        
        if self.played == False:
            self.open.play()
            self.played = True

        if self.isfocused:
            self.titlecolor = icy
            self.messagecolor = white
        else:
            self.titlecolor = grey
            self.messagecolor = grey2
            
        self.titletext = font.render(self.title, True, self.titlecolor)
        self.messagetext = font.render(self.message, True, self.messagecolor)

        if self.isdragged:
            self.drag()
        else:
            self.gap = [self.rect[0], self.rect[1], self.mouse[0], self.mouse[1]]

        if self.debug:
            self.variables = font.render('active: ' + str(self.isactive) + ' focus: ' + str(self.isfocused) \
                                        + ' touched: ' + str(self.istouched) + ' cb_istouched: ' + str(self.cb_istouched) \
                                         + ' dragged: ' + str(self.isdragged), True, white, black)
        
        self.cb_rect[0] = self.rect[0]+6
        self.cb_rect[1] = self.rect[1]+6
            
    def render(self):
        #Border Shadow
        pygame.draw.rect(self.screen, black, (self.rect[0]-3,self.rect[1]-3,self.rect[2]+6,self.rect[3]+6))

        #Main rectangle 
        pygame.draw.rect(self.screen, grey4, self.rect)
        
        #Button shadow and color
        pygame.draw.rect(self.screen, black,(self.cb_rect[0]-2, self.cb_rect[1]-2, self.cb_rect[2]+4, self.cb_rect[3]+4))
        pygame.draw.rect(self.screen, red, self.cb_rect)
        
        #Blit messages
        self.screen.blit(self.titletext, ((self.rect[0]+(self.rect[2]-font.size(self.title)[0])/2),self.rect[1]+5))
        self.screen.blit(self.messagetext, ((self.rect[0]+(self.rect[2]-font.size(self.message)[0])/2), self.rect[1] + self.rect[3]/2))
    
        if self.debug:
            self.screen.blit(self.variables,(self.rect[0],self.rect[1]-20))

            
class CutieMB(MessageBox):
    'subclass of MessageBox without much efford'
    
    def render(self):
        #Border Shadow
        pygame.draw.rect(self.screen, white, (self.rect[0]-3,self.rect[1]-3,self.rect[2]+6,self.rect[3]+6))

        #Main rectangle 
        pygame.draw.rect(self.screen, pink2, self.rect)
        
        #Button shadow and color
        pygame.draw.rect(self.screen, white,(self.cb_rect[0]-2, self.cb_rect[1]-2, self.cb_rect[2]+4, self.cb_rect[3]+4))
        pygame.draw.rect(self.screen, pink2, self.cb_rect)
        
        #Extra line for the cuteness
        pygame.draw.line(self.screen, white,(self.rect[0], self.cb_rect[1]-2 + self.cb_rect[3]+4 + 4),(self.rect[0] + self.rect[2], self.cb_rect[1]-2 + self.cb_rect[3]+4 + 4), 1)
        
        #Blit messages
        self.screen.blit(self.titletext, ((self.rect[0]+(self.rect[2]-font.size(self.title)[0])/2),self.rect[1]+5))
        self.screen.blit(self.messagetext, ((self.rect[0]+(self.rect[2]-font.size(self.message)[0])/2), self.rect[1] + self.rect[3]/2))
    
        if self.debug:
            self.screen.blit(self.variables,(self.rect[0],self.rect[1]-20))
    
    
class FancyText():
    def __init__(self, surface, text, AA=False):
        'Renders text with shadow.'
        self.surface = surface
        self.AA = AA
        self.text = font.render(text, self.AA, (255, 255, 255))
        self.text_shadow = font.render(text, self.AA, (0, 0, 0))
        
    def render(self, pos):
        #Borders / Shadows
        self.surface.blit(self.text_shadow, (pos[0] - 1, pos[1] - 1)) # up right
        self.surface.blit(self.text_shadow, (pos[0] + 1, pos[1] - 1)) # up left
        self.surface.blit(self.text_shadow, (pos[0] - 1, pos[1] + 1)) # down left
        self.surface.blit(self.text_shadow, (pos[0] + 1, pos[1] + 1)) # down right
        
        #White
        self.surface.blit(self.text, (pos[0], pos[1]))

        
#############################
#       Functions
#############################
    
def grid1(screen, space=64, color=(255,255,255), width=1):
    'Creates a grid with fixed mouse spacing between lines.'
    info = pygame.display.Info()
    res = (info.current_w, info.current_h)
    array = [0,0]
    if space <= 0:
        space = 1
    for lines in range(int(info.current_h/space+1)):
        #Horizontal
        pygame.draw.line(screen,color,(0,array[0]),(res[0],array[0]), width)
        array[0] += space
    for lines in range(int(info.current_w/space+1)):
        #Vertical
        pygame.draw.line(screen,color,(array[1],0),(array[1],res[1]), width)
        array[1] += space

def grid2(screen, scale=16, color=(255,255,255), width=1):
    'Creates a grid within the screen resolution to see how "xu" and "yu" are.'
    info = pygame.display.Info()
    res = (info.current_w, info.current_h)
    xu = res[0]/scale
    yu = res[1]/scale
    array = [0,0]
    for lines in range(scale):
        #Horizontal
        pygame.draw.line(screen,color,(0,array[0]),(res[0],array[0]), width)
        array[0] += yu
        #Vertical
        pygame.draw.line(screen,color,(array[1],0),(array[1],res[1]), width)
        array[1] += xu

def showfps(screen, tick_rate):
    fps = font.render(' ' + str(round(tick_rate.get_fps())) + ' ', True, white, black)
    screen.blit(fps, (0,0))

def showscale(screen):
    'Show how much are di, xu and yu.'
    variables = font.render('di: ' + str(di) + ' xu: ' + str(xu) + ' yu: ' + str(yu), True, white, black)
    screen.blit(variables, (0, yu))

    
