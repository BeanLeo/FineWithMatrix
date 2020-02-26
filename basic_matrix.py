import numpy as np
import math
class matrix_transform:

    def __init__(self):
        pass

    def Rotate(self, input_matrix, theta):
        """Roate 2-D matrix from with theta"""
        rotate_matrix = np.matrix([[math.sin(theta),math.cos(theta)],\
                                [math.cos(theta), -math.sin(theta)]])
        
        return rotate_matrix*input_matrix