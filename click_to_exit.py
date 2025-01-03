import pygame
import sys
import math
import random

# Initialize pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption("Click to Exit")

# Define game variables
rect_size = 100
white = (255, 255, 255)
blue = (65, 105, 225)
clock = pygame.time.Clock()  # Used for controlling the frame rate
bigcirc = pygame.rect.Rect(0, 0, rect_size, rect_size)
lilcirc = pygame.rect.Rect(0, 0, (rect_size // 1.5), (rect_size // 1.5))
silly_circle = pygame.draw.ellipse(screen, white, bigcirc)
silly_incircle = pygame.draw.ellipse(screen, blue, lilcirc)
mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
click_status = False
dist_x = bigcirc.x - mouse_pos_x
dist_y = bigcirc.y - mouse_pos_y
dist = math.sqrt((dist_x * dist_x) + (dist_y * dist_y))
det_range = 100
goal_x, goal_y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)

# Game loop
while True:
    
    # Handle events (e.g., closing the window)
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect.collidepoint(bigcirc, mouse_pos_x, mouse_pos_y):
                pygame.quit()
                sys.exit()

    # Game logic (update game state, positions, etc.)

    # Drawing on the screen (background, sprites, etc.)
    screen.fill(blue)  # Fill the screen with black
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()


    dist_x = bigcirc.x - mouse_pos_x
    dist_y = bigcirc.y - mouse_pos_y
    dist = math.sqrt((dist_x * dist_x) + (dist_y * dist_y))


    goal_x_dist = abs(goal_x - bigcirc.x)
    goal_y_dist = abs(goal_y - bigcirc.y)

    goal_dist = math.sqrt((goal_x_dist * goal_x_dist) + (goal_y_dist * goal_y_dist))


    print(goal_dist)
    if goal_dist < 200:
        if dist < det_range:
            goal_x, goal_y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
    

    goal_x_dist = abs(goal_x - bigcirc.x)
    goal_y_dist = abs(goal_y - bigcirc.y)

    bigcirc.x += (goal_x - bigcirc.x) // 8
    bigcirc.y += (goal_y - bigcirc.y) // 8

    # drawing the circs
    lilcirc.center = bigcirc.center
    pygame.draw.ellipse(screen, white, bigcirc)
    pygame.draw.ellipse(screen, blue, lilcirc)

    # Update the screen
    pygame.display.flip()

    # Control the frame rate (e.g., 60 FPS)
    clock.tick(60)

# Clean up and exit
pygame.quit()
sys.exit()
