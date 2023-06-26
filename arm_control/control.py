import math
from math import sqrt, asin, acos, atan2, sin, cos 
class arm_controller():
    def __init__(self, arm1_length, arm2_length, x_origin, y_origin):

        # x_origin: x coordinate of the base of arm
        # y_origin: y coordinate of the base of arm
        self.l1 = arm1_length
        self.l2 = arm2_length
        self.x_origin = x_origin
        self.y_origin = y_origin

    def inverse_kinematics(self, x_paddle, y_paddle):
        # x_paddle: x coordinate of target place of the paddle's center
        # y_paddle: y coordinate of target place of the paddle's center
        # return alpha1, alpha2(list)
        # calculate the angle
        x = x_paddle - self.x_origin
        y = -(y_paddle - self.y_origin)
        length = sqrt(x**2 + y**2)
        l1 = self.l1
        l2 = self.l2
        epsilon = 1e-3
        if abs(l1 + l2 - length) < epsilon:
            f = 0
        else:
            f = acos((x**2 + y**2 - l1**2 -l2**2) / 2*l1*l2)
        f1 = (l1**2 + (x**2 + y**2) - l2**2)/(2*l1*sqrt(x**2 + y**2))
        alpha1 = [math.degrees(atan2(y,x) - acos(f1)), math.degrees(atan2(y,x) + acos(f1))]
        alpha2 = [alpha1[0] + math.degrees(f),alpha1[1] + math.degrees(-f)]


        return alpha1, alpha2
        

        
        


        

        



