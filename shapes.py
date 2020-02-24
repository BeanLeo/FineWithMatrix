import numpy as np
from matplotlib import pyplot as plt

class shape:
    def __init__(self):
        self.name = "shape_basic"
        self.point_matrix = np.matrix([])
    
    def gen_shape_point_clockwise(self):
        raise NotImplementedError

    def draw_shape(self):
        raise NotImplementedError

    def draw_slide(self):
        raise NotImplementedError

class Square(shape):
    def __init__(self):
        super(Square,self).__init__()
        self.name = "square"

    def gen_shape_point_clockwise(self):
        line_range = list(np.linspace(-1,1,100))
        line_base = [1]*100
        x = (line_range + line_base)*2
        y = (line_base + line_range)*2
        xy_list = [x,y]
        self.point_matrix = np.matrix(xy_list)
        return self.point_matrix
    
    def draw_shape(self):
        plt.title(self.name)
        plt.
        plt.plot(self.point_matrix[0,:], self.point_matrix[1:])
        plt.show()


        