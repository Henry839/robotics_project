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
 #       self.parent.blit(self.image, (0,0))

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.width = width
        self.height = height

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.ini_image = self.image
        self.ini_rect = self.rect
        self.angle = 0



    def moveLeft(self, pixels):

        self.angle += 5
        if self.angle > 180:
            self.angle = 180
        ori_x, ori_y = self.ini_rect.x, self.ini_rect.y + self.height * 0.5
        angle = self.angle
        
        sin_a, cos_a = math.sin(math.radians(angle)), math.cos(math.radians(angle))
        center = (ori_x + self.width * 0.5 * cos_a, ori_y - self.width * 0.5 * sin_a)

        rotated_image = pygame.transform.rotate(self.ini_image, self.angle)
        rotated_rect = rotated_image.get_rect(center = center)
#        self.parent.blit(rotated_image, rotated_rect)
        self.image = rotated_image
        self.rect = rotated_rect
    def moveRight(self, pixels):
        self.angle -= 5
        if self.angle < 0:
            self.angle = 0
        ori_x, ori_y = self.ini_rect.x, self.ini_rect.y + self.height * 0.5
        angle = self.angle
        
        sin_a, cos_a = math.sin(math.radians(angle)), math.cos(math.radians(angle))
        center = (ori_x + self.width * 0.5 * cos_a, ori_y - self.width * 0.5 * sin_a)

        rotated_image = pygame.transform.rotate(self.ini_image, self.angle)
        rotated_rect = rotated_image.get_rect(center = center)
#        self.parent.blit(rotated_image, rotated_rect)
        self.image = rotated_image
        self.rect = rotated_rect


   

