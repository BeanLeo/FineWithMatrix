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
        line_base_neg = [-1]*100
        x = (line_range + line_base + line_range + line_base_neg)
        y = (line_base + line_range + line_base_neg + line_range)
        xy_list = [x,y]
        self.point_matrix = np.matrix(xy_list)
        return self.point_matrix
    def set_axis_in_middle(self, ax):
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left') 

        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        ax.set_aspect(1)

    def draw_shape(self):
        plt.title(self.name)
        ax = plt.gca()
        self.set_axis_in_middle(ax)
        plt.xlim(-3,3)
        plt.ylim(-3,3)
        plt.grid(True)
        plt.plot(self.point_matrix[0,:], self.point_matrix[1,:], 'bo')
        plt.savefig('tmp.png')


        