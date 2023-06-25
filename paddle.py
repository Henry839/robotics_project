import pygame
import math
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, parent, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.color = color
        self.parent = parent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.width = width
        self.height = height
 #       self.parent.blit(self.image, (0,0))

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


    def moveLeft(self, pixels):
        rotated_image = pygame.transform.rotate(self.image, 5)
        rotated_rect = rotated_image.get_rect(center = (350, 560))
        #self.parent.blit(rotated_image, rotated_rect)
        self.image = rotated_image
        self.rect = rotated_rect


        #if self.rect.x < 0:
        #  self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        #Check that you are not going too far (off the screen)
        if self.rect.x > 700:
          self.rect.x = 700
