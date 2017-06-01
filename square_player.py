'''

This code was a bit tricky to get going because
I had to literally copy and paste the code from "Collision game dixuyu" to
make this "square player" collide with the "brushes" aka "walls". it has to
check collision both times, for vertical and horizontal case cenarios.

Before this collision code, I used to make player vary it's position with
vectors (by calculating the difference between opposit directions velocities at same same,
so that it would stop when both keys (like right and left for example) were pressed at the same time,
and keep moving if one of them get up). I couldn't make this work with some kind of collision. :C

I think the code here is pretty straight forward, but if one is learning, it basically checks if player
collided with something, and makes that "something" know.

'''

from engine import *

class SquarePlayer:
    'A rectangle that moves with horizontal and vertical velocities'
    def __init__(self, screen, rect=[xu*8-xu/2,yu*8-yu/2,xu,yu]):
        self.rect = pygame.Rect(rect)
        self.vvel = int(xu/4)
        self.hvel = int(xu/4)
        self.screen = screen
        player_list.append(self)

    def moveup(self):
        self.move(0, -self.vvel)
        
    def movedown(self):
        self.move(0, self.vvel)
        
    def moveleft(self):
        self.move(-self.hvel, 0)
        
    def moveright(self):
        self.move(self.hvel, 0)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx,0)
        if dy != 0:
            self.move_single_axis(0,dy)

    def move_single_axis(self, dx, dy):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for brush in brush_list:
            if brush.issolid:
                if self.rect.colliderect(brush.rect):
                    brush.istouched = True
                    if brush.breakable:
                        brush.destroy()
                    
                    if dx > 0: # Moving right; Hit the left side of the wall
                        self.rect.right = brush.rect.left
                    if dx < 0: # Moving left; Hit the right side of the wall
                        self.rect.left = brush.rect.right

                        
                    if dy > 0: # Moving down; Hit the top side of the wall
                        self.rect.bottom = brush.rect.top
                    if dy < 0: # Moving up; Hit the bottom side of the wall
                        self.rect.top = brush.rect.bottom
                        
                else:
                    brush.istouched = False

    def render(self):
        pygame.draw.rect(self.screen, grey4,(self.rect),0)


class Brush():
    def __init__(self, screen, rect=(xu*4, yu*12, xu*8, yu), color=blue, active=True, solid=True, breakontouch=False, debug=False):
        self.screen = screen
        self.isactive = active
        self.issolid = solid
        self.debug = debug
        self.rect = pygame.Rect(rect)
        brush_list.append(self)
        self.istouched = False
        self.color = color
        self.breakable = breakontouch

    def destroy(self):
        self.isactive = False
        self.issolid = False
        
    def render(self):
        if self.isactive:
            for player in player_list:
                if self.rect.colliderect(player.rect):
                    pygame.draw.rect(self.screen, blue2, self.rect)

                elif self.istouched:
                    pygame.draw.rect(self.screen, yellow, self.rect)
                    
                else:
                    pygame.draw.rect(self.screen, self.color, self.rect)

        if self.debug:
            self.variables = font.render('solid: ' + str(self.issolid) \
                                            + ' breakable ' + str(self.breakable), True, white, black)
            self.screen.blit(self.variables, (self.rect[0], self.rect[1]-20))
    

player_list = []
brush_list = []
