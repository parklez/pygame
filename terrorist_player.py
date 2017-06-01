import pygame

class Player():
    def __init__(self, display, rect=[0, 0, 40, 40], right=True, velocity=10, scale=1):
    
        self.rect = pygame.Rect(rect)
        self.surface = display
        self.right = right
        self.scale = scale
        
        self.tr_un = pygame.transform.scale(pygame.image.load('sprites/tr_un.png'),(int(self.scale),int(self.scale)))
        self.tr_ak = pygame.transform.scale(pygame.image.load('sprites/tr_ak.png'),(int(self.scale),int(self.scale)))
        self.tr_legs_0 = pygame.transform.scale(pygame.image.load('sprites/tr_legs_0.png'),(int(self.scale),int(self.scale)))
        self.tr_legs_1 = pygame.transform.scale(pygame.image.load('sprites/tr_legs_1.png'),(int(self.scale),int(self.scale)))
        
        self.upper = self.tr_ak
        self.lower = self.tr_legs_0
        self.velocity = velocity
        self.frame = 0
        
        self.current_weapon = 'ak47'
        
        self.walking = False
        self.walking_loop = [self.tr_legs_0, self.tr_legs_1]
        self.walking_current_sprite_index = 0
        self.lower = self.walking_loop[self.walking_current_sprite_index]
        
    def move_right(self):
        self.walking = True
        self.right = True
        self.move('right')
        
    def move_left(self):
        self.walking = True
        self.right = False
        self.move('left')
        
    def move_up(self):
        self.walking = True
        self.move('up')
        
    def move_down(self):
        self.walking = True
        self.move('down')
        
    def move(self, direction=''):
        if direction == 'right':
            self.rect[0] += self.velocity
            
        if direction == 'left':
            self.rect[0] -= self.velocity
            
        if direction == 'up':
            self.rect[1] -= self.velocity
            
        if direction == 'down':
            self.rect[1] += self.velocity
            
    def stop(self):
        self.walking = False
        
    def update(self):
        self.frame += 1
        
        if self.walking:
            
            if self.frame >= 20:
                self.walking_current_sprite_index += 1
                
                if self.walking_current_sprite_index == 2:
                    self.walking_current_sprite_index = 0
            
                self.lower = self.walking_loop[self.walking_current_sprite_index]
                self.frame = 0

        else:
            self.walking_current_sprite_index = 0 
            
        if self.right:
            self.lower = self.walking_loop[self.walking_current_sprite_index]
            self.upper = self.tr_ak
        
        else:
            self.lower = pygame.transform.flip(self.walking_loop[self.walking_current_sprite_index], 40,0)
            self.upper = pygame.transform.flip(self.tr_ak, 40,0)
            
    def render(self):
        self.surface.blit(self.lower, (self.rect[0], self.rect[1]))
        self.surface.blit(self.upper, (self.rect[0], self.rect[1]))
