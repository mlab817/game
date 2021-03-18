# tutorial can be found here: https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

# import library
import pygame
import math
from pygame.locals import *

# initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# declare keys
keys = [False, False, False, False]
playerpos = [100, 100]
acc = [0, 0]
arrows = []

# load images
player = pygame.image.load('resources/images/dude.png')
grass = pygame.image.load('resources/images/grass.png')
castle = pygame.image.load('resources/images/castle.png')
arrow = pygame.image.load('resources/images/bullet.png')

# loop through
while 1:
    # clear screen before drawing
    screen.fill(0)

    for x in range(int(width / grass.get_width() + 1)):
        for y in range(int(height / grass.get_height() + 1)):
            screen.blit(grass, (x * 100, y * 100))
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # get mouse position
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width/2, playerpos[1] - playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0]) * 10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1] < -64 or bullet[1]>640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        index+=1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # update the screen
    pygame.display.flip()

    # loop through events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32), position[0] - (playerpos1[0] +26)), playerpos1[0]+32, playerpos1[1]+32])

        # check if the event is the X button
        if event.type==pygame.QUIT:
            # quit the game
            pygame.quit()
            exit(0)

    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    elif keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5