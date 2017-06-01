from engine import *

import terrorist_player

display = pygame.display.set_mode(resolution)
tick_rate = pygame.time.Clock()

player = terrorist_player.Player(display, rect=[xu*8-xu/2, yu*11, yu, yu], scale=yu*4)

def game():
    while True:
        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                quit()
                    
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            player.move_left()
            
        if key[pygame.K_d]:
            player.move_right()
            
        if key[pygame.K_w]:
            player.move_up()
            
        if key[pygame.K_s]:
            player.move_down()
            
        if key[pygame.K_a] == False and key[pygame.K_d] == False and key[pygame.K_w] == False and key[pygame.K_s] == False:
            player.stop()

        if key[pygame.K_a] and key[pygame.K_d]:
            player.stop()
            
        display.fill(white)
        grid2(display, color=white2)
        
        player.update()
        player.render()

        showfps(display, tick_rate)

        pygame.display.update()
        tick_rate.tick(60)
        
if __name__ == "__main__":
    game()
