import pygame, sys
from setings import seting
from project import game
from project2 import game2

def menu():
    pygame.init()
    pygame.mixer.music.load("music/2.mp3")
    pygame.mixer.music.play(1)
    sc = pygame.display.set_mode((1920,1080))#screen size
    menu = pygame.image.load("background/bg.jpg")#menu
    start = pygame.image.load('img\\st.png')#start
    exit_1 = pygame.image.load('img\\qu.png')#quit
    set_1 = pygame.image.load('img\\sett.png')#settings
    set_1 = pygame.transform.scale(set_1,(200,200))#settings size
    game_start = True#varitble for game start
    while game_start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()#code for game close
        mouse = pygame.mouse.get_pos()#varitble for mouse
        
            
        if 830+200 > mouse[0] > 830 and 420+60 > mouse[1] > 420:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game()#code for game start
        if 880+180 > mouse[0] > 880 and 540+60 > mouse[1] > 540:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.quit()#code for game quit
                    sys.exit()
        if 880+180 > mouse[0] > 880 and 660+600 > mouse[1] > 660:
           if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    seting()#code for settings

        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            pygame.mixer.music.pause()
            
                # pygame.mixer.music.stop()
        if keys[pygame.K_2]:
            pygame.mixer.music.unpause()
                        # pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)
            
        if keys[pygame.K_3]:
            pygame.mixer.music.unpause()
                        # pygame.mixer.music.play()
            pygame.mixer.music.set_volume(1)
            
            
            
        sc.fill((255, 255, 255))#screen cooler
        sc.blit(menu,(0,0))
        sc.blit(start,(830,280))
        sc.blit(exit_1,(880,470))
        sc.blit(set_1,(880,610))
        pygame.display.update()
    pygame.quit()
menu()
