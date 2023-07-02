#Import the pygame library and initialise the game engine
import pygame #Let's import the Paddle Class & the Ball Class
from paddle import Paddle
from ball import Ball
from brick import Brick
from arm_control.place_prediction import place_predicter
from arm_control.control import arm_controller
from math import sqrt
pygame.init()

# Define some colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
GREY = (220, 220, 220)

score = 0
lives = 3

# Open a new window
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

arm1 = Paddle(None, GREY, 200, 6)
arm1.rect.x = 400
arm1.rect.y = 760

arm2 = Paddle(arm1, GREY, 160, 6)
arm2.rect.x = 400+200
arm2.rect.y = 760

# trajectory predicter
predicter = place_predicter(200,160,400,763)
# arm controller
controller = arm_controller(200,160,400,763)


#Create the Paddle
paddle = Paddle(arm2, LIGHTBLUE, 100, 10)
paddle.rect.x = 600
paddle.rect.y = 760

arm1.child = arm2
arm2.child = paddle

#Create the ball sprite
ball = Ball(WHITE,10,10)
ball.rect.x = 300
ball.rect.y = 195

all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(ORANGE,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(YELLOW,80,30)
    brick.rect.x = 60 + i* 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

# Add the paddle and the ball to the list of sprites
all_sprites_list.add(paddle)
all_sprites_list.add(ball)
all_sprites_list.add(arm1)
all_sprites_list.add(arm2)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
time = 0
flag = 2
count = 0

delta_angle = 4
# -------- Main Program Loop -----------
out_flag = 0
while carryOn:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop

    #Moving the paddle when the use uses the arrow keys
#    if flag == 0:
        # predict the trajectory from the beginning

    time += clock.get_time()

    all_sprites_list.update()
    if flag == 1:
        time = 0
        flag = 0
        out_flag = 0
        next_x, next_y = predicter.get_destination(ball,all_bricks,all_sprites_list)
        alpha1,alpha2 = controller.inverse_kinematics(next_x, next_y + 10)
        
    if flag == 2:
        flag = 0
        time = 801
        next_x, next_y = predicter.get_destination(ball,all_bricks,all_sprites_list)
        alpha1,alpha2 = controller.inverse_kinematics(next_x, next_y + 10)

    ball_origin_length = sqrt((ball.rect.x - controller.x_origin)**2  + (ball.rect.y - controller.y_origin)**2)
    if ball_origin_length > 400:
        out_flag = 1

    
    if alpha1 - arm1.angle > delta_angle  and out_flag == 1:
        K_LEFT = True
        K_RIGHT = False

    elif arm1.angle - alpha1 > delta_angle  and out_flag == 1:
        K_RIGHT = True
        K_LEFT = False
    else:

        K_RIGHT = False 
        K_LEFT = False

    if alpha2 - arm2.angle > delta_angle  and out_flag == 1:
        K_UP = True
        K_DOWN = False

    elif arm2.angle - alpha2 > delta_angle  and out_flag == 1:
        K_DOWN = True
        K_UP = False
    else:
        K_DOWN = False 
        K_UP = False

    if K_LEFT:
        arm1.rotate_1(delta_angle)
    if K_RIGHT:
        arm1.rotate_1(-delta_angle)
    if K_UP:
        arm2.rotate_2(delta_angle)
    if K_DOWN:
        arm2.rotate_2(-delta_angle)

    # --- Game logic should go here

    
    #Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >=785 and ball.rect.y < 42:
        ball.velocity[0] = -ball.velocity[0]
        ball.velocity[1] = -ball.velocity[1]
    elif ball.rect.x <=5 and ball.rect.y < 42:
        ball.velocity[0] = -ball.velocity[0]
        ball.velocity[1] = -ball.velocity[1]
    else:
        if ball.rect.x>=785:
#            flag = 2
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=5:
#            flag = 2
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>790:
#            flag = 2
            ball.velocity[1] = -ball.velocity[1]
            lives -= 1
            if lives == 0:
                #Display Game Over Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                screen.blit(text, (250,300))
                pygame.display.flip()
                pygame.time.wait(3000)

                #Stop the Game
                carryOn=False
        if ball.rect.y<42:
#            flag = 2
            ball.velocity[1] = -ball.velocity[1]

    #Detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddle):
                
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        #print("*" * 20)
        #print("ball : ",ball.rect.x, " " , ball.rect.y)
        #print(next_x, next_y)

        ball.bounce()
        flag = 1


    #Check if there is the ball collides with any of bricks
    brick_collision_list = pygame.sprite.spritecollide(ball,all_bricks,False)
    for brick in brick_collision_list:
        ball.bounce()
        flag = 2
        score += 1
        brick.kill()
        if len(all_bricks)==0:
            #Display Level Complete Message for 3 seconds
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200,300))
            pygame.display.flip()
            pygame.time.wait(3000)
            #Stop the Game
            carryOn=False

    # --- Drawing code should go here
    # First, clear the screen to dark blue.
    screen.fill(DARKBLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)

    #Display the score and the number of lives at the top of the screen
    font = pygame.font.Font(None, 34)
    text = font.render("Score: " + str(score), 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Lives: " + str(lives), 1, WHITE)
    screen.blit(text, (650,10))

    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(100)

#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
