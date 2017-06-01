'''

With the code from "test_maze_dixuyu" I could test out some
simple possibilities with collidable objects.

'''

from engine import *
from terrorist_player import *
from square_player import *

display = pygame.display.set_mode(resolution)
tick_rate = pygame.time.Clock()


player = SquarePlayer(display, rect=[xu*8-xu/2,yu*8-yu/2,yu,yu])

downplat = Brush(display, color=pink, debug=True)
upperplat = Brush(display,(xu*4, yu*4, xu*8, yu), orange, solid=False, debug=True)
leftplat = Brush(display,(xu*2,yu*6,yu,yu*4), active = False, debug=True)
rightplat = Brush(display,(xu*13,yu*6,yu,yu*4), white, breakontouch = True, debug=True)

left_outscreen = Brush(display, (-xu, -yu, xu, yu*17))
right_outscreen = Brush(display, (xu*16, -yu, xu, yu*17))
up_outscreen = Brush(display, (-xu, -yu, xu*17, yu))
down_outscreen = Brush(display, (-xu, yu*16, xu*17, yu))



def game():
    while True:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            player.moveleft()
            
        if key[pygame.K_d]:
            player.moveright()

        if key[pygame.K_w]:
            player.moveup()
            
        if key[pygame.K_s]:
            player.movedown()

                
        display.fill(grey3)
        grid2(display, color=grey2)

        for brush in brush_list:
            brush.render()

        player.render()

        showfps(display, tick_rate)

        pygame.display.update()
        tick_rate.tick(60)
        
if __name__ == "__main__":
    game()
