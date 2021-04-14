#################
# Basic Pygame  #
# Jason White   #
# 13 April 2021 #
#################

#-- Import modules -------------------#
import pygame
import random
import sys

# -- Set up pygame -------------------#
from pygame.locals import *
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
background = pygame.Surface(SCREEN.get_size())
background.fill((0, 0, 0))
clock = pygame.time.Clock()

#  -- The program starts here --------#
def main():

    # -- Define the rectangle
    rect_x = 100
    rect_y = 100
    rect_width = 80
    rect_height = 40
    rect_line = 2
    rect_colour = (255, 0, 0)

    # -- Define the circle -----------#
    circle_x = 200
    circle_y = 300
    circle_radius = 100
    circle_line = 10
    circle_colour = (0, 255, 0)

    # -- Define the image ------------#
    image_x = 500
    image_y = 400

    # -- Load an image -------------------#
    image = pygame.image.load("mypic.jpg").convert()

    # ------------------------------------#
    # -- Main loop -----------------------#
    # ------------------------------------#
    while True:

        # -- Check for exit --------------#
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        # -- Draw a black background -----#
        #SCREEN.blit(background, (0, 0))

        # -- Draw the rectangle ----------#
        pygame.draw.rect(SCREEN, rect_colour, (rect_x, rect_y, rect_width, rect_height), rect_line)
        rect_x = rect_x + 1
        rect_y += 1

        # -- Draw the circle -------------#
        pygame.draw.circle(SCREEN, circle_colour, (circle_x, circle_y), circle_radius, circle_line)

        # -- Draw an image ---------------#
        SCREEN.blit(image, (image_x, image_y))

        # -- Update the screen -----------#
        pygame.display.flip()

        # -- Limit to 60 FPS -------------#
        clock.tick(60)

if __name__ == "__main__":
    main()