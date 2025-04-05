import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

x, y = 30, 620
speed = 0.5  

isJump = False
jumpCount = 10

image = pygame.image.load('makoknis.png')
def Background_sky(image):
    size = pygame.transform.scale(image, (150, 76))
    screen.blit(size, (50, 90))

#!!!!!!main loop!!!!!!    
while running:

    screen.fill((70, 40, 204))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #kustiba
    keys = pygame.key.get_pressed() 
    plyer = pygame.draw.rect(screen, "red", pygame.Rect(x, y, 60, 60))
    speedd = 0.5
    if x < 0:
        speed=0
    elif x>0:
        speed=0.5
    if keys[pygame.K_a]: 
        x -= speed
    if keys[pygame.K_d]: 
        x += speedd    
    #jumping
 
    if keys[pygame.K_SPACE]:
        y -=speed
    elif y <=620:
             y+=speed
    
          
    f = 0
    while f <=1240:
        pygame.draw.rect(screen, 'green', pygame.Rect(f, 680, 40, 40))
        f+=40
    Background_sky(image)
    
    pygame.display.flip()
    
pygame.quit()
