import pygame
from pygame import *
import random
import math
from math import *


# Intialize the pygame
pygame.init()

# Create the screen 
screen = pygame.display.set_mode((800, 600))

# Background 
background = pygame.image.load("grass.jpg")



# Creating the Title and setting the Icon
pygame.display.set_caption("Student Coder")
icon = pygame.image.load("globe.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("person.png")
playerX = 370
playerY = 480
playerX_change = 0

# Zombie 
zombieImg = pygame.image.load("zombie.png")
zombieX = random.randint(0, 735 )
zombieY = random.randint(50, 150)
zombieX_change = 3 
zombieY_change = 30

# Nut (Shooting) 
# Ready - You can not see the Nut on the screen 
# Fire  - The Nut is currently moving 
nutImg = pygame.image.load("nut.png")
nutX = 0
nutY = 480
nutX_change = 0 
nutY_change = 10
nut_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))

def zombie(x, y):
    screen.blit(zombieImg, (x, y))

def fire_nut(x, y):
    global nut_state
    nut_state = "fire"
    screen.blit(nutImg, (x + 16, y + 10 ))

def isCollision(zombieX, zombieY, nutX, nutY):
    distance = math.sqrt((math.pow(zombieX - nutX,2)) + (math.pow(zombieY - nutY,2)))
    if distance < 27:
        return True
    else:
        False

# Game Loop
running = True 

while running:
    # RGB
    screen.fill((255, 255, 255))

    # Background Image 
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checking the keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                playerX_change = -3
            if event.key == K_RIGHT:
                playerX_change = 3
            if event.key == K_SPACE:
                if nut_state is "ready":
                    # Get the current cordiante of student 
                    nutX = playerX
                    fire_nut(nutX, nutY)
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT :
                playerX_change = 0
                

    # Checking for boundaries of spaceship so it does not go out of bounds
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    

    # Zombie movement
    zombieX += zombieX_change
    
    if zombieX <= 0:
        zombieX_change = 3
        zombieY += zombieY_change
    elif zombieX >= 736:
        zombieX_change = -3
        zombieY += zombieY_change
    
    # Nut movement 
    if nutY <= 0:
        nutY = 480
        nut_state = "ready"

    if nut_state is "fire":
        fire_nut(nutX, nutY)
        nutY -= nutY_change

    # Collision
    collision = isCollision(zombieX, zombieY, nutX, nutY)
    if collision:
        nutY = 480
        nut_state = "ready"
        score += 1
        print(score)
        zombieX = random.randint(0, 735)
        zombieY = random.randint(50, 150)



    player(playerX, playerY)
    zombie(zombieX, zombieY)
    pygame.display.update()