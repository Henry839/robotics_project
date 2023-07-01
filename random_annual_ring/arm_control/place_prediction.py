import math
import pygame
from math import sqrt
class place_predicter():
    def __init__(self, arm1_length, arm2_length, x_origin, y_origin):
        # l1: length of the first stick (the one closest to the origin) # l2: length of the second stick
        # x_origin: x coordinate of the base of arm
        # y_origin: y coordinate of the base of arm

        self.l1 = arm1_length
        self.l2 = arm2_length
        self.x_origin = x_origin 
        self.y_origin = y_origin
        #print(self.y_origin)
        #print(self.x_origin)
    def get_destination(self, ball, all_bricks, all_sprite_list):
        # x_0, y_0: the place where the ball and the paddle crash
        # v_x, v_y: velocity after crash
        
        initial_x = ball.rect.x
        initial_y = ball.rect.y
        initial_velocity_x = ball.velocity[0]
        initial_velocity_y = ball.velocity[1]
        available_paddle_x = []
        available_paddle_y = []
        score_list = []
        new_all_bricks = all_bricks.copy()

        new_all_sprites_list = pygame.sprite.Group()
        new_all_sprites_list.add(ball)
        new_all_sprites_list.add(new_all_bricks)
        count = 0;
        epsilon = 10
        dead_brick_list = pygame.sprite.Group()
        simulate_dead_brick_list = pygame.sprite.Group()
        ball_origin_length = 0;
        bound_length = self.l1 + self.l2
        min_length = abs(self.l1 - self.l2)
        count = 0
        print("-"* 20)
        while(True):
            print(f"ball trajectory : {ball.rect.x}, {ball.rect.y}")


            new_all_sprites_list.update()
            count += 1
            if ball.rect.x>=790:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.x<=0:
                ball.velocity[0] = -ball.velocity[0]
            if ball.rect.y>790:
#                ball.velocity[1] = -ball.velocity[1]
                break
            if ball.rect.y<40:
                ball.velocity[1] = -ball.velocity[1]

            #Detect collisions between the ball and the paddles
            #Check if there is the ball collides with any of bricks

            brick_collision_list = pygame.sprite.spritecollide(ball,new_all_bricks,False)

            for brick in brick_collision_list:
                ball.bounce()
                brick.kill()
                dead_brick_list.add(brick)
            # the ball will reach here, try to hit the ball

            ball_origin_length = sqrt((ball.rect.x - self.x_origin)**2  + (ball.rect.y - self.y_origin)**2)
            if(ball_origin_length <= bound_length and ball.velocity[1] > 0 and ball_origin_length >= min_length):
                # hit the ball
                ball0_x = ball.rect.x
                ball0_y = ball.rect.y
                ball0_vx = ball.velocity[0]
                ball0_vy = ball.velocity[1]
                simulate_dead_brick_list.empty()


                
                ball.bounce()
                flag = 1
                score = 0
                while(True):
                    if(sqrt((ball.rect.x - self.x_origin)**2  + (ball.rect.y - self.y_origin)**2) < self.l1 + self.l2 and ball.velocity[1] > 0 and sqrt((ball.rect.x - self.x_origin)**2  + (ball.rect.y - self.y_origin)**2) > min_length):
                        break
                    new_all_sprites_list.update()
                    if ball.rect.x>=790:
                        ball.velocity[0] = -ball.velocity[0]
                    if ball.rect.x<=0:
                        ball.velocity[0] = -ball.velocity[0]
                    if ball.rect.y>790:
                        ball.velocity[1] = -ball.velocity[1]
                        flag = 0 # hit the bottom
                        break
                    if ball.rect.y<40:
                        ball.velocity[1] = -ball.velocity[1]

                    #Detect collisions between the ball and the paddles
                    #Check if there is the ball collides with any of bricks

                    brick_collision_list = pygame.sprite.spritecollide(ball,new_all_bricks,False)

                    for brick in brick_collision_list:
                        ball.bounce()
                        score += 1
                        brick.kill()
                        simulate_dead_brick_list.add(brick)
                if(flag == 1):
                    available_paddle_x.append(ball0_x)
                    available_paddle_y.append(ball0_y)
                    score_list.append(score)
                #initialize for this hit
                ball.rect.x = ball0_x
                ball.rect.y = ball0_y
                ball.velocity[0] = ball0_vx
                ball.velocity[1] = ball0_vy
                for dead_brick in simulate_dead_brick_list:
                    all_bricks.add(dead_brick)
                    new_all_sprites_list.add(dead_brick)
                    all_sprite_list.add(dead_brick)
                bound_length -= 2
                if(bound_length <= min_length):
                    break
        max_i = score_list.index(max(score_list))

        final_x = available_paddle_x[max_i]
        final_y = available_paddle_y[max_i]
        ball.rect.x = initial_x
        ball.rect.y = initial_y
        ball.velocity[0] = initial_velocity_x
        ball.velocity[1] = initial_velocity_y
        for dead_brick in dead_brick_list:
            all_bricks.add(dead_brick)
            all_sprite_list.add(dead_brick)
        return final_x, final_y



