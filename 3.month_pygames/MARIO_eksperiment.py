import pygame, sys

pygame.init()

window_size = ( 400, 400 )

white = ( 255, 255, 255 )

screen = pygame.display.set_mode( window_size )

done = False
x, y, =30 ,30
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.draw.rect(screen, "red", pygame.Rect(x, y, 20, 20))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -=0.1
            if event.key == pygame.K_RIGHT:
                move = ( 10, 0 )
                x+=0.1
            if event.key == pygame.K_UP:
                y-=0.1
            if event.key == pygame.K_DOWN:
                y+=0.1  
    screen.fill( white )
    
    pygame.display.flip()