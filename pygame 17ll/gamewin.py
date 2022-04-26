import pygame
def win():
    pygame.init()
    sc4 = pygame.display.set_mode((1920,1080))
    g =  pygame.image.load("letter\\g.png")
    g = pygame.transform.scale(g,(200,200))
    yg = -1000
    a =  pygame.image.load("letter\\a.png")
    a = pygame.transform.scale(a,(200,200))
    ya = -900
    m =  pygame.image.load("letter\\m.png")
    m = pygame.transform.scale(m,(200,200))
    ym = -800
    e =  pygame.image.load("letter\\e.png")
    e = pygame.transform.scale(e,(200,200))
    ye = -700
    w =  pygame.image.load("letter\\w.png")
    w = pygame.transform.scale(w,(200,200))
    yw = -200
    i =  pygame.image.load("letter\\i.png")
    i = pygame.transform.scale(i,(200,200))
    yi = -300
    n =  pygame.image.load("letter\\n.png")
    n = pygame.transform.scale(n,(200,200))
    yn = -400
    k = True
    settings = True
    while settings:
        if k:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    k = False
        if k:
            mouse = pygame.mouse.get_pos()
            sc4.fill((255,255,255))
            sc4.blit(g,(600,yg))
            if yg < 400:
                yg+=2
            sc4.blit(a,(750,ya))
            if ya < 400:
                ya+=2
            sc4.blit(m,(900,ym))
            if ym < 400:
                ym+=2
            sc4.blit(e,(1050,ye))
            if ye < 400:
                ye+=2
            sc4.blit(w,(650,yw))
            if yw < 600:
                yw+=2
            sc4.blit(i,(800,yi))
            if yi < 600:
                yi+=2
            sc4.blit(n,(950,yn))
            if yn < 600:
                yn+=2
            pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
                settings = False
pygame.quit()

