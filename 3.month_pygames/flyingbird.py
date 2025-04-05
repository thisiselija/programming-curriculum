import pygame
import random
from pygame import mixer 

pygame.init()
screen = pygame.display.set_mode((1280, 620))
running = True
x, y = 30, 330
speed = 0.3 
mapX = 400   
blockH = []
r = 5
mixer.init()
mixer.music.load("Billie Eilish - Lost Cause (Official Music Video).mp3") 
mixer.music.set_volume(0.5)
mixer.music.play()
for v in range(r):
    blockH.append(random.randrange(20, 490)) 
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #mixer.music.stop()
    screen.fill((22, 32, 220))
    keys = pygame.key.get_pressed() 
    
    plyer = pygame.draw.rect(screen, "red", pygame.Rect(x, y,35, 35))

    if keys[pygame.K_SPACE]:
        y -=speed
        mapX -=0.1
    else:
        y+=speed
        mapX -=0.1
    #pamatne
    m = mapX
    
    for k in range(r):           
        #mapY = blockH + 130
        
        mapY = blockH[k] + 130
        uperBlock = pygame.draw.rect(screen, "green", pygame.Rect(mapX + m, 0, 40, blockH[k]))
        downBlock = pygame.draw.rect(screen, "green", pygame.Rect(mapX + m, mapY , 40, 30000))
        m +=250
        if x+30 >= mapX and y <= blockH[k] and x <=mapX:
            y+=2
    pygame.display.flip()

pygame.quit()