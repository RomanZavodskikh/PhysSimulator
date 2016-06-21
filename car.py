#!/usr/bin/python3
# INITIALIZATON
import pygame, math, sys
from pygame.locals import *
X_RES = 1024
Y_RES = 768
CAR_SEMIWIDTH = 50
CAR_SEMIHEIGHT = 50
screen = pygame.display.set_mode((X_RES, Y_RES))
car = pygame.image.load('car.png')
car2 = pygame.image.load('car2.png')
clock = pygame.time.Clock()
k_up = k_down = k_left = k_right = 0
speed = direction = 0
position = (100, 100)
position2 = (400, 400)
TURN_SPEED = 5
ACCELERATION = 2
MAX_FORWARD_SPEED = 10
MAX_REVERSE_SPEED = -5
BLACK = (0, 164, 128)

while True:
    # USER INPUT
    clock.tick(30)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        down = event.type == KEYDOWN    # key down or up?
        if event.key == K_RIGHT: k_right = down * -5
        elif event.key == K_LEFT: k_left = down * 5
        elif event.key == K_UP: k_up = down * 2
        elif event.key == K_DOWN: k_down = down * -2
        elif event.key == K_ESCAPE: sys.exit(0)
    screen.fill(BLACK)

    # SIMULATION
    # .. new speed and direction based on acceleration and turn
    speed += (k_up + k_down)
    if speed > MAX_FORWARD_SPEED: speed = MAX_FORWARD_SPEED
    if speed < MAX_REVERSE_SPEED: speed = MAX_REVERSE_SPEED
    direction += (k_right + k_left)
    # .. new position based on current position, speed and direction
    x, y = position
    rad = direction * math.pi / 180
    x += -speed*math.sin(rad)
    y += -speed*math.cos(rad)

    if x < CAR_SEMIWIDTH or y < CAR_SEMIHEIGHT or x > X_RES-CAR_SEMIWIDTH or y > Y_RES-CAR_SEMIHEIGHT:
    # .. collision with the borders
        speed = -speed
    elif (x-400)*(x-400)+(y-400)*(y-400) <= 100*100:
        speed = -speed
    else:
        position = (x,y)

    # RENDERING
    # .. rotate the car image for direction
    rotated = pygame.transform.rotate(car, direction)
    # .. position the car on screen
    rect = rotated.get_rect()
    rect.center = position
    rect2 = car2.get_rect()
    rect2.center = position2
    # .. render the car to screen
    screen.blit(rotated, rect)
    screen.blit(car2, rect2)
    pygame.display.flip()

