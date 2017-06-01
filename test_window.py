# This is a clear and simple way to make tests from scratch.

from engine import *

display = pygame.display.set_mode(resolution)
tick_rate = pygame.time.Clock()


def game():
    while True:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if x.type == pygame.KEYDOWN:
                if x.key == pygame.K_a:
                    pass
                        
        display.fill(grey4)

        grid2(display, color=grey3)
        #grid1(display, color=grey4)

        showfps(display, tick_rate)
        
        pygame.display.update()
        tick_rate.tick(60)
        
if __name__ == "__main__":
    game()
