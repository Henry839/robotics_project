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
        self.child = None
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


    def rotate_1(self, delta):
        self.angle += delta
        if self.angle > 180:
            self.angle = 180
        if self.angle < 0:
            self.angle = 0
        
        ori_x, ori_y = self.ini_rect.x, self.ini_rect.y + self.height * 0.5
        angle = self.angle
        sin_a, cos_a = math.sin(math.radians(angle)), math.cos(math.radians(angle))
        center = (ori_x + self.width * 0.5 * cos_a, ori_y - self.width * 0.5 * sin_a)
        rotated_image = pygame.transform.rotate(self.ini_image, self.angle)
        rotated_rect = rotated_image.get_rect(center = center)
        self.image = rotated_image
        self.rect = rotated_rect
        a2 = self.child
        pad = a2.child
        a2_x = center[0]+ self.width * 0.5 * cos_a + a2.width * 0.5 * math.cos(math.radians(a2.angle))
        a2_y = center[1] - self.width * 0.5 * sin_a - a2.width * 0.5 * math.sin(math.radians(a2.angle))
        a2_center = (a2_x, a2_y)
        a2.rect = a2.image.get_rect(center = a2_center)
        pad_x = a2_center[0] + a2.width * 0.5 * math.cos(math.radians(a2.angle))
        pad_y = a2_center[1] - a2.width * 0.5 * math.sin(math.radians(a2.angle))
        pad_center = (pad_x, pad_y)
        pad.rect = pad.image.get_rect(center = pad_center)


    def rotate_2(self, delta):

        self.angle += delta
        if self.angle > 180:
            self.angle = 180
        if self.angle < 0:
            self.angle = 0
        
        a1 = self.parent
        ori_x = a1.ini_rect.x + a1.width * math.cos(math.radians(a1.angle))
        ori_y = a1.ini_rect.y + self.height * 0.5 - a1.width * math.sin(math.radians(a1.angle))
        angle = self.angle
        sin_a, cos_a = math.sin(math.radians(angle)), math.cos(math.radians(angle))
        center = (ori_x + self.width * 0.5 * cos_a, ori_y - self.width * 0.5 * sin_a)
        rotated_image = pygame.transform.rotate(self.ini_image, self.angle)
        rotated_rect = rotated_image.get_rect(center = center)
        self.image = rotated_image
        self.rect = rotated_rect
        pad = self.child
        pad_x = center[0] + self.width * 0.5 * math.cos(math.radians(self.angle))
        pad_y = center[1] - self.width * 0.5 * math.sin(math.radians(self.angle))
        pad_center = (pad_x, pad_y)
        pad.rect = pad.image.get_rect(center = pad_center)
        


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


   

