import time
import pygame
import random
from gameover import l

def game():
    pygame.init()
    sc2 = pygame.display.set_mode((1930,1080))
    bg = pygame.image.load("background\\bg1.jpg")
    money = pygame.image.load("money/Money1.png")
    pygame.mixer.music.load("music/1.mp3")
    pygame.mixer.music.play(1)
    tile2 = pygame.image.load("Tile/Tile2.png")
    tile2 = pygame.transform.scale(tile2,(150,100))
    tile3 = pygame.image.load("Tile/Tile3.png")
    tile3 = pygame.transform.scale(tile3,(150,100))
    tile4 = pygame.image.load("Tile/Tile4.png")
    tile4 = pygame.transform.scale(tile4,(150,100))
    tile5 = pygame.image.load("Tile/Tile5.png")
    tile5 = pygame.transform.scale(tile5,(150,100))
    spike2 = pygame.image.load("Tile/spike.png")
    spike2 = pygame.transform.scale(spike2,(150,100))
    tile6 = pygame.image.load("Tile/Tile2.png")
    tile6 = pygame.transform.scale(tile2,(150,100))
    tile7 = pygame.image.load("Tile/Tile2.png")
    tile7 = pygame.transform.scale(tile2,(150,100))
    tile8 = pygame.image.load("Tile/Tile3.png")
    tile8 = pygame.transform.scale(tile3,(150,100))
    tile9 = pygame.image.load("Tile/Tile4.png")
    tile9 = pygame.transform.scale(tile4,(150,100))
    tile10 = pygame.image.load("Tile/Tile5.png")
    tile10 = pygame.transform.scale(tile5,(150,100))
    spike3 = pygame.image.load("Tile/spike.png")
    spike3 = pygame.transform.scale(spike2,(150,100))
    tile11 = pygame.image.load("Tile/Tile2.png")
    tile11 = pygame.transform.scale(tile2,(150,100))
    tile12 = pygame.image.load("Tile/Tile2.png")
    tile12 = pygame.transform.scale(tile2,(150,100))
    tile13 = pygame.image.load("Tile/Tile2.png")
    tile13 = pygame.transform.scale(tile2,(150,100))
    a = 1100
    b = 400
    x = 40
    y = 700
    width = 400
    height = 300
    speed = 10
    isJump = False
    jumpCount = 10
    Money2 = pygame.image.load("money/Money17.png")
    Money2 = pygame.transform.scale(Money2,(125,75))
    Money3 = pygame.image.load("money/Money16.png")
    Money3 = pygame.transform.scale(Money3,(125,75))
    Money4 = pygame.image.load("money/Money15.png")
    Money4 = pygame.transform.scale(Money4,(125,75))
    Money5 = pygame.image.load("money/Money14.png")
    Money5 = pygame.transform.scale(Money5,(125,75))
    Money6 = pygame.image.load("money/Money13.png")
    Money6 = pygame.transform.scale(Money6,(125,75))
    Money7 = pygame.image.load("money/Money12.png")
    Money7 = pygame.transform.scale(Money7,(125,75))
    Money8 = pygame.image.load("money/Money11.png")
    Money8 = pygame.transform.scale(Money8,(125,75))
    Money9 = pygame.image.load("money/Money10.png")
    Money9 = pygame.transform.scale(Money9,(125,75))
    Money10 = pygame.image.load("money/Money9.png")
    Money10 = pygame.transform.scale(Money10,(125,75))
    Money11 = pygame.image.load("money/Money8.png")
    Money11= pygame.transform.scale(Money11,(125,75))
    Money12 = pygame.image.load("money/Money7.png")
    Money12 = pygame.transform.scale(Money12,(125,75))
    Money13 = pygame.image.load("money/Money6.png")
    Money13 = pygame.transform.scale(Money13,(125,75))
    Money14 = pygame.image.load("money/Money5.png")
    Money14 = pygame.transform.scale(Money14,(125,75))
    Money15 = pygame.image.load("money/Money4.png")
    Money15 = pygame.transform.scale(Money15,(125,75))
    Money16 = pygame.image.load("money/Money3.png")
    Money16 = pygame.transform.scale(Money16,(125,75))
    Money17 = pygame.image.load("money/Money2.png")
    Money17 = pygame.transform.scale(Money17,(125,75))
    scmon = 0
    anim_left = [pygame.image.load("img/Bikerrun1.png"),
    pygame.image.load("img/Biker_run6.png"),pygame.image.load("img/Biker_run7.png"),
    pygame.image.load("img/Biker_run8.png"),pygame.image.load("img/Biker_run9.png"),
    pygame.image.load("img/Biker_run10.png")]
    anim_right = [pygame.image.load("img/Bikerrun.png"),
    pygame.image.load("img/Biker_run1.png"),
    pygame.image.load("img/Biker_run2.png"),pygame.image.load("img/Biker_run3.png"),
    pygame.image.load("img/Biker_run4.png"),pygame.image.load("img/Biker_run5.png")]
    left = False
    right = False
    k = True
    animCount = 0
    lastMove = "right"
    kyanq1 = pygame.image.load('img\\s1.png')
    kyanq2 = pygame.image.load('img\\s1.png')
    kyanq3 = pygame.image.load('img\\s1.png')
    kyanq4 = pygame.image.load('img\\s1.png')
    kyanqkes = pygame.image.load('img\\s2.png')
    kyanqsc = 6
    kyanq5 = pygame.image.load('img\\s1.png')
    altkyanq = True
    clock = pygame.time.Clock()
    player = pygame.image.load("img/1.png")
    game_continuse = True
    while game_continuse:   
        clock.tick(60)
        if k:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    k = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                    game_continuse = False
            if kyanqsc == 0:
                l()
                return game()
            
                
        if k:
            keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            if lastMove == "right":
                facing = 1
            else:
                facing = -1  
            if len(bullets) < 5:
                bullets.append(kr(round(x + width // 2), round(y + height // 2),
                5,(255, 0, 0), facing))       
        if keys[pygame.K_LEFT]:
            x -= speed
            left = True
            right = False
            lastMove = "left"
        elif keys[pygame.K_RIGHT]:
            x += speed
            right = True
            left = False
            lastMove = "right"
        else:
            left = False
            right = False
            animCount = 0
        if not(isJump):
            if keys[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    y += (jumpCount ** 2) / 2
                else:
                    y -= (jumpCount ** 2) / 2
                jumpCount -= 1
            else:
                isJump = False  
                jumpCount = 10

                
        
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
            
                
        if x < 0 or x > 1750:
            kyanqsc-=1
            time.sleep(1)
        if y <= 600 and y >= 550:
            if x > 100 and x < 300:
                y = 549
        if y <= 500 and y >= 450:
            if x > 600 and x < 1100:
                y = 449
        if y <= 450 and y >= 400:
            if x  > 750 and x < 950:
                x = 650
                kyanqsc -= 1
        if y <= 400 and y >= 350:
            if x > 1150 and x < 1350:
                y = 349
        if y <= 300 and y >= 250:
            if x > 1350 and x < 1550:
                y = 249
        if y <= 200 and y >= 150:
            if x > 800 and x < 1300:
                y = 149
        if y <= 500 and y >= 450:
            if x > 300 and x < 500:
                y = 449
        if  y <= 150 and y >= 100:
            if x > 950 and x < 1150:
                x = 1200
                kyanqsc -= 1
        if y <= 100 and y >= 50:
            if x > 550 and x < 750:
                y = 49
        if  y <= 100 and y >= 50:
            if x > 250 and x < 450:
                y = 49
        if altkyanq:
            if y <= 750 and y >= 700:
                if x > 1100 and x < 1200:
                    altkyanq = False
                    kyanqsc+=2
        if x < 1920:     
            if isJump == False:
                if y < 700:
                    y+=10
        if k:          
            sc2.blit(bg, (0,0))
            if kyanqsc >= 2:
                sc2.blit(kyanq1, (1200,20))
            if kyanqsc >= 4:
                sc2.blit(kyanq2, (1250,20))
            if kyanqsc >= 6: 
                sc2.blit(kyanq3, (1300,20))
            if kyanqsc == 8: 
                sc2.blit(kyanq4, (1350,20))
            if kyanqsc == 1:
                sc2.blit(kyanqkes, (1200,20))
            if kyanqsc == 3:
                sc2.blit(kyanqkes, (1250,20))
            if kyanqsc == 5:
                sc2.blit(kyanqkes, (1300,20))
            if kyanqsc == 7:
                sc2.blit(kyanqkes, (1350,20))
            if altkyanq:
                sc2.blit(kyanq5,(1200,700))
        if k:
            sc2.blit(tile2, (200,750))
            sc2.blit(tile3, (700,650))
            sc2.blit(tile4, (850,650))
            sc2.blit(tile5, (1000,650))
            sc2.blit(spike2, (850,550))
            sc2.blit(tile6, (1250,550))
            sc2.blit(tile7, (1450,450))
            sc2.blit(tile8, (900,350))
            sc2.blit(tile9, (1050,350))
            sc2.blit(tile10, (1200,350))
            sc2.blit(spike3, (1050,250))
            sc2.blit(tile11, (650,250))
            sc2.blit(tile12, (400,650))
            sc2.blit(tile13, (350,250))
        if k:
            if scmon == 0:
                sc2.blit(Money2, (x,y-50))
                sc2.blit(money, (600,850))
                if x > 600 - 100 and x < 600 + 10:
                    if y > 850 - 185 and y < 850 + 15:
                        scmon = 1 
            if scmon == 1:
                sc2.blit(Money3, (x,y-50))
                sc2.blit(money, (1300,500))
                if x > 1300 - 100 and x < 1300 + 10:
                    if y > 500 - 185 and y < 500 + 15:
                        scmon = 2
            if scmon == 2:
                sc2.blit(Money4, (x,y-50))
                sc2.blit(money, (1500,700))
                if x > 1500 - 100 and x < 1500 + 10:
                    if y > 700 - 185 and y < 700 + 15:
                        scmon = 3
            if scmon == 3:
                sc2.blit(Money5, (x,y-50))
                sc2.blit(money, (1500,400))
                if x > 1500 - 100 and x < 1500 + 10:
                    if y > 400 - 185 and y < 400 + 15:
                        scmon = 4
            if scmon == 4:
                sc2.blit(Money6, (x,y-50))
                sc2.blit(money, (450,600))
                if x > 450 - 100 and x < 450 + 10:
                    if y > 600 - 185 and y < 600 + 15:
                        scmon = 5
            if scmon == 5:
                sc2.blit(Money7, (x,y-50))
                sc2.blit(money, (1050,600))
                if x > 1050 - 100 and x < 1050 + 10:
                    if y > 600 - 185 and y < 600 + 15:
                        scmon = 6
            if scmon == 6:
                sc2.blit(Money8, (x,y-50))
                sc2.blit(money, (1250,300))
                if x > 1250 - 100 and x < 1250 + 10:
                    if y > 300 - 185 and y < 300 + 15:
                        scmon = 7
            if scmon == 7:
                sc2.blit(Money9, (x,y-50))
                sc2.blit(money, (760,600))
                if x > 760 - 100 and x < 760 + 10:
                    if y > 600 - 185 and y < 600 + 15:
                        scmon = 8
            if scmon == 8:
                sc2.blit(Money10, (x,y-50))
                sc2.blit(money, (950,300))
                if x > 950 - 100 and x < 950 + 10:
                    if y > 300 - 185 and y < 300 + 15:
                        scmon = 9
            if scmon == 9:
                sc2.blit(Money11, (x,y-50))
                sc2.blit(money, (1400,850))
                if x > 1400 - 100 and x < 1400 + 10:
                    if y > 850 - 185 and y < 850 + 15:
                        scmon = 10
            if scmon == 10:
                sc2.blit(Money12, (x,y-50))
                sc2.blit(money, (700,200))
                if x > 700 - 100 and x < 700 + 10:
                    if y > 200 - 185 and y < 200 + 15:
                        scmon = 11
            if scmon == 11:
                sc2.blit(Money13, (x,y-50))
                sc2.blit(money, (1300,500))
                if x > 1300 - 100 and x < 1300 + 10:
                    if y > 500 - 185 and y < 500 + 15:
                        scmon = 12
            if scmon == 12:
                sc2.blit(Money14, (x,y-50))
                sc2.blit(money, (450,600))
                if x > 450 - 100 and x < 450 + 10:
                    if y > 600 - 185 and y < 600 + 15:
                        scmon = 13
            if scmon == 13:
                sc2.blit(Money15, (x,y-50))
                sc2.blit(money, (1500,550))
                if x > 1500 - 100 and x < 1500 + 10:
                    if y > 550 - 185 and y < 550 + 15:
                        scmon = 14
            if scmon == 14:
                sc2.blit(Money16, (x,y-50))
                sc2.blit(money, (400,200))
                if x > 400 - 100 and x < 400 + 10:
                    if y > 200 - 185 and y < 200 + 15:
                        scmon = 15
            if scmon == 15:
                sc2.blit(Money17, (x,y-50))
                from project2 import game2
            if animCount + 1 >=30:
                animCount = 0
            elif right:
                sc2.blit(anim_right[animCount // 5], (x, y))
                animCount += 1
            elif left:
                sc2.blit(anim_left[animCount // 5], (x, y))
                animCount += 1
            else:
                sc2.blit(player, (x, y))
            pygame.display.update()
pygame.quit()

