import pygame
pygame.init()
def seting():
    sc3 = pygame.display.set_mode((1920,1080))
    menu = pygame.image.load("background\\menu.png")
    z_1 =  pygame.image.load("img\\11.png")
    z_2 =  pygame.image.load("img\\10.png")
    z_3 =  pygame.image.load("img\\3.png")
    z_4 =  pygame.image.load("img\\4.png")
    retturn = pygame.image.load('img\\01.png')#retturn
    settings = True
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        mouse = pygame.mouse.get_pos()
        if 1300+100 > mouse[0] > 1300 and 800+60 > mouse[1] > 800:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                        settings = False
        sc3.fill((255,255,255))
        sc3.blit(menu,(470,200))
        sc3.blit(retturn,(1300,800))
        sc3.blit(z_1,(500,250))
        sc3.blit(z_2,(600,250))
        sc3.blit(z_3,(700,250))
        sc3.blit(z_4,(800,250))
        pygame.display.update()
pygame.quit()

