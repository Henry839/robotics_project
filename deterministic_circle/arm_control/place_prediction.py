import math
import pygame
from math import sqrt
class place_predicter():
    def __init__(self, arm1_length, arm2_length, x_origin, y_origin):
        # l1: length of the first stick (the one closest to the origin)
        # l2: length of the second stick
        # x_origin: x coordinate of the base of arm
        # y_origin: y coordinate of the base of arm

        self.l1 = arm1_length
        self.l2 = arm2_length
        self.x_origin = x_origin 
        self.y_origin = y_origin
    def get_destination(self, ball, all_bricks, all_sprite_list):
        # x_0, y_0: the place where the ball and the paddle crash
        # v_x, v_y: velocity after crash
        
        initial_x = ball.rect.x
        initial_y = ball.rect.y
        initial_velocity_x = ball.velocity[0]
        initial_velocity_y = ball.velocity[1]
        #print(type(ball.velocity))
        #print("initial_velocity",ball.velocity)
        new_all_bricks = all_bricks.copy()

        new_all_sprites_list = pygame.sprite.Group()
        new_all_sprites_list.add(ball)
        new_all_sprites_list.add(new_all_bricks)
        count = 0;
        epsilon = 5
        dead_brick_list = pygame.sprite.Group()

        while(abs(sqrt((ball.rect.x - self.x_origin)**2  + (ball.rect.y - self.y_origin)**2) - (self.l1 + self.l2)) > epsilon or ball.velocity[1] < 0):
            # when not reaching the circle
#            print(f"error : {sqrt((ball.rect.x - self.x_origin)**2  + (ball.rect.y - self.y_origin)**2) - (self.l1 + self.l2)}")
#            print(f"velocity : {ball.velocity[1]}")

            if(count > 1000):
                print("TOO LONG")
                break
            new_all_sprites_list.update()
            count += 1
#            print(f"count : {count}")
#            print(f" x  : {ball.rect.x}, y : {ball.rect.y}")
            if ball.rect.x>=790:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x<=0:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y>790:
                ball.velocity[1] = -ball.velocity[1]
            if ball.rect.y<40:
                ball.velocity[1] = -ball.velocity[1]

            #Detect collisions between the ball and the paddles
            #Check if there is the ball collides with any of bricks

            brick_collision_list = pygame.sprite.spritecollide(ball,new_all_bricks,False)

            for brick in brick_collision_list:
                ball.bounce()
                brick.kill()
                dead_brick_list.add(brick)

        final_x = ball.rect.x
        final_y = ball.rect.y
        ball.rect.x = initial_x
        ball.rect.y = initial_y
        ball.velocity[0] = initial_velocity_x
        ball.velocity[1] = initial_velocity_y
        for dead_brick in dead_brick_list:
            all_bricks.add(dead_brick)
            all_sprite_list.add(dead_brick)
        return final_x, final_y



