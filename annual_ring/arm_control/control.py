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
#        print(x,y)
        length = sqrt(x**2 + y**2)
        l1 = self.l1
        l2 = self.l2
#        epsilon = 1e-3
        psi = (x**2 + y**2 - l1**2 -l2**2)/(2 * l1 * l2)
        if(psi < -1):
            psi = -1
        elif(psi > 1):
            psi = 1
        alpha2 = acos(psi)
        psi2 = (x**2 + y**2 + l1**2 - l2**2)/(2 * sqrt(x**2 + y**2) * l1)
        if(psi2 < -1):
            psi2 = -1
        elif(psi2 > 1):
            psi2 = 1

        gamma = acos(psi2)
        

        beta = atan2(y,x)
        beta = math.degrees(beta)
        gamma = math.degrees(gamma)
        
        alpha1 = beta - gamma
        alpha1 = math.degrees(alpha1)
        alpha2 = math.degrees(alpha2)
        if alpha1 < 0:
            alpha1 = beta + gamma
            alpha2 = alpha1 + (-alpha2)
        else:
            alpha1 = beta - gamma
            alpha2 = alpha1 + alpha2

        return alpha1, alpha2





    def trivial_inverse_kinematics(self, x_paddle, y_paddle):
        length = sqrt(pow(x_paddle - self.x_origin,2) + pow(y_paddle - self.y_origin,2))
        alpha = acos((x_paddle - self.x_origin)/length)
        alpha = math.degrees(alpha)
        return alpha
        

        
        


        

        



