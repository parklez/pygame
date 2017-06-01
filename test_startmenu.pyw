from engine import *

if fullscreen:
    display = pygame.display.set_mode((resolution), pygame.FULLSCREEN)
else:
    display = pygame.display.set_mode((resolution))

pygame.display.set_caption('Start Menu')
tick_rate = pygame.time.Clock()

########################################################################
StartButton = TextButton(display, 'New game', (xu, yu*8, 150, 25))
LoadButton = TextButton(display, 'Load save', (xu, yu*8+yu, 150, 25))
OptionsButton = TextButton(display, 'Options', (xu, yu*8+yu*2, 150, 25))
QuitButton = TextButton(display, 'Quit', (xu, yu*8+yu*3, 150, 25))
ReturnButton = TextButton(display, 'Back to menu', (xu, yu*8+yu*2, 200, 25))

if debug:
    IsDebugActive = TextButton(display, 'Activated', (xu+150, yu*4, 160, 25))
    ToggleButton = TextButton(display, 'Debug:  ', (xu, yu*4, 150, 25))
    for x in TextButton_list:
        x.debug = True
    for x in messagebox_list:
        x.debug = True
else:
    IsDebugActive = TextButton(display, 'Deactivated', (xu+150, yu*4, 160, 25))
    ToggleButton = TextButton(display, 'Debug:  ', (xu, yu*4, 150, 25), triggered = True)

MainButtons = (StartButton, LoadButton, QuitButton, OptionsButton)
OptionsButtons = (ReturnButton, ToggleButton,IsDebugActive)
LoadButtons = (ReturnButton, )
#########################################################################

j1 = MessageBox(display, 'Sorry buddy', 'Game\'s not ready yet', active=False)
j2 = CutieMB(display, 'Oh hey...', 'Please... don\'t close me... (>д<)', center_pos=(xu*13, yu*14))

bg = pygame.transform.scale(pygame.image.load('sprites/bg/outsider_by_kuroinolily.jpg'), (resolution[0],resolution[1]))


def j1_debug():
    'Quick function to debug j1, which is a window.'
    msg = font.render('isactive: ' + str(j1.isactive) + ' istouched: ' + str(j1.istouched) \
                      + ' cb_istouched: ' + str(j1.cb_istouched) + ' isfocused: ' + str(j1.isfocused) \
                     + ' played: ' + str(j1.played) + ' dragged: ' + str(j1.isdragged) , True, white, black)
    display.blit(msg, (0,yu*2))

def developer():
    'Everything I would like to be debugged when global "debug" is on.'
    if debug:
        grid2(display, color=grey2)
        j1_debug()
        showscale(display)
        showfps(display, tick_rate)
        b1 = font.render('StartButton.istriggered: ' + str(StartButton.istriggered), True, white, black)
        display.blit(b1,(0,yu*15))

mouse_pos = []

def mainmenu():
    global mouse_pos
    
    for x in MainButtons:
        x.mouse = mouse_pos

    while QuitButton.istriggered == False:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if events.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()

                for x in MainButtons:
                    x.mouse = mouse_pos

                for y in messagebox_list:
                    y.mouse = mouse_pos
                
            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:       
                                
                    for x in MainButtons:
                        if x.istouched:
                            x.istriggered = True
                            x.clicksound()

                            if StartButton.istriggered:
                                j1.update()
                                j1.isactive = True
                                
                            if OptionsButton.istriggered:
                                j1.isfocused = False
                                options()
                                
                            if LoadButton.istriggered:
                                j1.isfocused = False
                                loadmenu()
                                
                    for y in messagebox_list:
                        if y.isactive:
                            if y.istouched:
                                y.isfocused = True
                                y.isdragged = True
                                
                            else:
                                y.isfocused = False
                                
                            if y.cb_istouched:
                                y.isdragged = False
                                y.isactive = False
                                y.played = False
                                y.close.play()

                            if j1.cb_istouched:
                                StartButton.istriggered = False

                            if j2.cb_istouched:
                                'Cry sound here'
                                pass
                                
            if events.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed()[0] == False:
                    #Its not likely to have more than 1 dragged...
                    for y in messagebox_list:
                        y.isdragged = False

        display.fill(grey)
        display.blit(bg,(0,0))

        developer()

        for x in MainButtons:
            if x.isactive:
                x.update()
                x.render()

        for y in messagebox_list:
            if y.isactive:
                y.update()
                y.render()

        pygame.display.update()
        tick_rate.tick(60)
    pygame.quit()
    quit()

def loadmenu():
    global mouse_pos
    
    for y in LoadButtons:
        y.mouse = mouse_pos

    while ReturnButton.istriggered == False:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if events.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for x in LoadButtons:
                    x.mouse = mouse_pos
                
                for y in messagebox_list:
                    y.mouse = mouse_pos
                
            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:

                    for y in messagebox_list:
                        if y.isactive:
                            if y.istouched:
                                y.isfocused = True
                                y.isdragged = True
                            else:
                                y.isfocused = False
                                
                            if y.cb_istouched:
                                y.isactive = False
                                y.played = False
                                y.close.play()
                                
                            if j1.cb_istouched:
                                StartButton.istriggered = False

                    for x in LoadButtons:
                        if x.istouched == True:
                            x.istriggered = True
                            x.clicksound()
                                
            if events.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed()[0] == False:
                    #Its not likely to have more than 1 dragged...
                    for y in messagebox_list:
                        y.isdragged = False

                            
        display.fill(grey4)

        developer()
                
        for x in LoadButtons:
            if x.isactive:
                x.update()
                x.render()
            
        for y in messagebox_list:
            if y.isactive:
                y.update()
                y.render()

        pygame.display.update()
        tick_rate.tick(60)

    ReturnButton.istriggered = False
    LoadButton.istriggered = False
    mainmenu()

def options():
    global mouse_pos, debug
    
    for x in OptionsButtons:
        x.mouse = mouse_pos
        
    while ReturnButton.istriggered == False:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if events.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for x in OptionsButtons:
                    x.mouse = mouse_pos
                    
                for y in messagebox_list:
                    y.mouse = mouse_pos
                
            if events.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for x in OptionsButtons:
                        if x.istouched == True:
                            x.clicksound()
                            if x.istriggered == False:
                                x.istriggered = True
                            else:
                                x.istriggered = False
    
                            if ToggleButton.istriggered:
                                IsDebugActive.text = 'Deactivated'
                                debug = False
                                for y in TextButton_list:
                                    y.debug = False
                                    
                                for y in messagebox_list:
                                    y.debug = False
                            else:
                                IsDebugActive.text = 'Activated'
                                debug = True
                                for y in TextButton_list:
                                    y.debug = True
                                    
                                for y in messagebox_list:
                                    y.debug = True

                    for y in messagebox_list:
                        if y.isactive:
                            if y.istouched:
                                y.isfocused = True
                                y.isdragged = True
                            else:
                                y.isfocused = False
                                
                            if y.cb_istouched:
                                y.isactive = False
                                y.played = False
                                y.close.play()
                                
                            if j1.cb_istouched:
                                StartButton.istriggered = False
                                    
            if events.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed()[0] == False:
                    #Its not likely to have more than 1 dragged...
                    for y in messagebox_list:
                        y.isdragged = False
                            
        display.fill(grey4)
        
        developer()

        for x in OptionsButtons:
            x.update()
            x.render()

        for y in messagebox_list:
            if y.isactive:
                y.update()
                y.render()
            
        pygame.display.update()
        tick_rate.tick(60)
        
    ReturnButton.istriggered = False
    OptionsButton.istriggered = False
    mainmenu()

if __name__ == "__main__":
    mainmenu()
