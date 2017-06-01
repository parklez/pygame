# First time programming an animation.

from engine import *

resolution = (800, 600)

display = pygame.display.set_mode(resolution)
tick_rate = pygame.time.Clock()

scale = 16
di = math.sqrt(resolution[0]**2+resolution[1]**2)
xu = resolution[0]/scale
yu = resolution[1]/scale

class Animation():
    def __init__(self, display):
        self.display = display
        self.frame = 0
        self.sprite_files = ('sprites/yoshi/yoshi0.png', 'sprites/yoshi/yoshi1.png', 'sprites/yoshi/yoshi2.png',
        'sprites/yoshi/yoshi3.png', 'sprites/yoshi/yoshi4.png')
        self.sprites = [pygame.transform.scale(pygame.image.load(file), (int(xu*4), int(xu*4))) for file in self.sprite_files]
        #self.sprites = [pygame.image.load(file) for file in self.sprite_files]
        self.sprite_loop = [self.sprites[2], self.sprites[3], self.sprites[4], self.sprites[3], self.sprites[1], 
        self.sprites[0], self.sprites[1]]
        
        self.current_sprite_index = 0
        self.current_sprite = self.sprite_loop[self.current_sprite_index]
        
    def update(self):
        self.frame += 1
        
        if self.frame == 6:
            self.frame = 0
            self.current_sprite_index += 1
        
        if self.current_sprite_index == 7:
            self.current_sprite_index = 0
            
        self.current_sprite = self.sprite_loop[self.current_sprite_index]
    
    def render(self):
        self.display.blit(self.current_sprite, (400 - xu*2, 300 - xu*2)) 
        

def game():

    text = FancyText(display, 'Yoshi! <3', True)
    yoshi = Animation(display)

    while True:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_a:
                    pass
                        
        display.fill(white)

        grid2(display, color=white2)

        showfps(display, tick_rate)
        
        yoshi.update()
        yoshi.render()
        text.render((xu*8, yu))
        print(xu, xu*8)
        
        showscale(display)
        
        pygame.display.update()
        tick_rate.tick(60)
        
        
        
if __name__ == "__main__":
    game()
