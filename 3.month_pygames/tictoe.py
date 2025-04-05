import pygame

pygame.init()
screen = pygame.display.set_mode((420, 570))
clock = pygame.time.Clock()
running = True
def map():
    pygame.draw.rect(screen, 'black', pygame.Rect(160, 0, 10, 570))
    pygame.draw.rect(screen, 'black', pygame.Rect(320, 0, 10, 570))
    pygame.draw.rect(screen, 'black', pygame.Rect(160, 0, 10, 570))
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, 'black', pygame.Rect(60, 45, 100, 50))
    
    screen.fill("white")
    
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()