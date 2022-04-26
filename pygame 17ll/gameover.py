import pygame
def l():
    a = True
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
    o =  pygame.image.load("letter\\o.png")
    o = pygame.transform.scale(o,(200,200))
    yo = -200
    v =  pygame.image.load("letter\\v.png")
    v = pygame.transform.scale(v,(200,200))
    yv = -300
    e2 =  pygame.image.load("letter\\e.png")
    e2 = pygame.transform.scale(e2,(200,200))
    ye2 = -400
    r =  pygame.image.load("letter\\r.png")
    r = pygame.transform.scale(r,(200,200))
    yr = -500
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
            sc4.blit(o,(600,yo))
            if yo < 600:
                yo+=2
            sc4.blit(v,(750,yv))
            if yv < 600:
                yv+=2
            sc4.blit(e2,(900,ye2))
            if ye2 < 600:
                ye2+=2
            sc4.blit(r,(1050,yr))
            if yr < 600:
                yr+=2
            pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            settings = False
            
        
pygame.quit()
