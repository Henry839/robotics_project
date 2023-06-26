import math
from math import sqrt, asin, acos
class arm_controller():
    def __init__(self, arm1_length, arm2_length, x_origin, y_origin):

        # x_origin: x coordinate of the base of arm
        # y_origin: y coordinate of the base of arm
        self.arm1_length = arm1_length
        self.arm2_length = arm2_length
        self.x_origin = x_origin
        self.y_origin = y_origin

    def inverse_kinematics(self, x_paddle, y_paddle):
        # x_paddle: x coordinate of target place of the paddle's center
        # y_paddle: y coordinate of target place of the paddle's center
        length = sqrt(pow(x_paddle - self.x_origin,2) + pow(y_paddle - self.y_origin,2))
        if(length != (self.arm1_length + self.arm2_length)):
            print("ERROR: x_paddle and y_paddle error")
            raise ValueError

        # calculate the angle
        alpha = acos((x_paddle - self.x_origin)/length)
        alpha = math.degrees(alpha)
        return alpha
        

        
        


        

        



