#Python 3 version from the following:
#http://www.pygame.org/project-Rect+Collision+Response-1061-.html

from engine import *

class Player():
    def __init__(self):
        self.rect = pygame.Rect(xu, yu, xu, yu)

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
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

class Wall():
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], xu, yu)

display = pygame.display.set_mode(resolution)

tick_rate = pygame.time.Clock()

walls = []

player = Player()

level = [
"WWWWWWWWWWWWWWWW",
"W              W",
"W             WW",
"W   WWWW       W",
"W   W          W",
"W WWW  WWWW    W",
"W   W     W W  W",
"W   W     W    W",
"W   WWW WWW    W",
"W     W   W    W",
"WWW   W   WWW WW",
"W W      WW    W",
"W W   WWWW    WW",
"W     W    E   W",
"W     W    E   W",
"WWWWWWWWWWWWWWWW",
]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, xu, yu)
        x += xu
    y += yu
    x = 0

def game():
    running = True
    while running:
        
        tick_rate.tick(60)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                running = False
        
        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            player.move(-10, 0)
        if key[pygame.K_d]:
            player.move(10, 0)
        if key[pygame.K_w]:
            player.move(0, -10)
        if key[pygame.K_s]:
            player.move(0, 10)
        
        # Just added this to make it slightly fun ;)
        if player.rect.colliderect(end_rect):
            running = False
        
        # Draw the scene
        display.fill(grey4)
        
        for wall in walls:
            pygame.draw.rect(display, grey3, wall.rect)
            
        grid2(display, color=grey3)
            
        pygame.draw.rect(display, red, end_rect)
        pygame.draw.rect(display, blue, player.rect)

        pygame.display.flip()

if __name__ == "__main__":
    game()
 
pygame.quit()
exit()
