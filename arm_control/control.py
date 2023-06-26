import math
from math import sqrt, asin, acos
class arm_controller():
    def __init__(self, arm1_length, arm2_length):
        self.arm1_length = arm1_length
        self.arm2_length = arm2_length

    def inverse_kinematics(x_paddle, y_paddle, x_origin, y_origin):
        # x_paddle: x coordinate of target place of the paddle's center
        # y_paddle: y coordinate of target place of the paddle's center
        # x_origin: x coordinate of the base of arm
        # y_origin: y coordinate of the base of arm
        length = sqrt(pow(x_paddle - x_origin) + pow(y_paddle - y_origin))
        if(length != (self.arm1_length + self.arm2_length)):
            print("ERROR: x_paddle and y_paddle error")
            raise ValueError

        # calculate the angle
        alpha = acos((x_paddle - x_origin)/length))
        alpha = math.degrees(alpha)
        return alpha
        

        
        


        

        



