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

# Multiple Zombies 
zombieImg = []
zombieX = []
zombieY = []
zombieX_change = []
zombieY_change = []
num_of_zombies = 5

for i in range(num_of_zombies):

    # Zombie 
    zombieImg.append(pygame.image.load("zombie.png"))
    zombieX.append(random.randint(0, 735 ))
    zombieY.append(random.randint(50, 150))
    zombieX_change.append(3) 
    zombieY_change.append(30)

# Nut (Shooting) 
# Ready - You can not see the Nut on the screen 
# Fire  - The Nut is currently moving 
nutImg = pygame.image.load("nut.png")
nutX = 0
nutY = 480
nutX_change = 0 
nutY_change = 10
nut_state = "ready"

# Score 
score_value = 0
font = pygame.font.Font("cherry.ttf", 32)

textX = 10
textY = 10

# Game Over 
over_font = pygame.font.Font("cherry.ttf", 64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))

def zombie(x, y, i):
    screen.blit(zombieImg[i], (x, y))

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
    for i in range(num_of_zombies):

        # Game Over 
        if zombieY[i] > 400:
            for j in range(num_of_zombies):
                 zombieY[j] = 2000
            game_over_text()
            break


        zombieX[i] += zombieX_change[i]
        if zombieX[i] <= 0:
            zombieX_change[i] = 3
            zombieY[i] += zombieY_change[i]
        elif zombieX[i] >= 736:
            zombieX_change[i] = -3
            zombieY[i] += zombieY_change[i]
        
        # Collision
        collision = isCollision(zombieX[i], zombieY[i], nutX, nutY)
        if collision:
            nutY = 480
            nut_state = "ready"
            score_value  += 1
            zombieX[i] = random.randint(0, 735)
            zombieY[i] = random.randint(50, 150)
        
        zombie(zombieX[i], zombieY[i], i)

    
    # Nut movement 
    if nutY <= 0:
        nutY = 480
        nut_state = "ready"

    if nut_state is "fire":
        fire_nut(nutX, nutY)
        nutY -= nutY_change

    


    player(playerX, playerY)
    
    show_score(textX, textY)
    pygame.display.update()