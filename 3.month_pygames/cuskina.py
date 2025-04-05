import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

x, y = 30, 30
speed = 0.3
width, height = 30, 30
edX, edY = random.randint(0, 1240), random.randint(0, 680)

#keydown
def move(x, y, speed):
    """ keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed """
    

    x = max(0, min(1250, x))
    y = max(0, min(690, y))

    return x, y

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
               
            # checking if key "A" was pressed
            if event.key == pygame.K_a:
                print(" j=huh")
                x -= speed
               
            # checking if key "J" was pressed
            if event.key == pygame.K_s:
                y += speed
               
            # checking if key "P" was pressed
            if event.key == pygame.K_d:
                x += speed
             
            # checking if key "M" was pressed
            if event.key == pygame.K_w:
                y -= speed

    screen.fill("gray")

    # Move player and redraw it
    x, y = move(x, y, speed)
    player = pygame.draw.rect(screen, "red", pygame.Rect(x, y, width, height))

    food = pygame.draw.rect(screen, "white", pygame.Rect(edX, edY, 30, 30))

    if player.colliderect(food):
        edX, edY = random.randint(0, 1240), random.randint(0, 680)
        height += 10 

    pygame.display.flip()

pygame.quit()
