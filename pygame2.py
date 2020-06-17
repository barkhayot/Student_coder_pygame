import pygame
from pygame import *

# Intialize the pygame
pygame.init()

# Create the screen 
screen = pygame.display.set_mode((800, 600))

# Creating the Title and setting the Icon
pygame.display.set_caption("Student Coder")
icon = pygame.image.load("globe.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("person.png")
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True 

while running:
    # RGB
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checking the keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                playerX_change = -3
            if event.key == K_RIGHT:
                playerX_change = 3
            if event.key == K_UP:
                playerY_change = -3
            if event.key == K_DOWN:
                playerY_change = 3
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_DOWN or event.key == K_UP :
                playerX_change = 0
                playerY_change = 0

    
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()