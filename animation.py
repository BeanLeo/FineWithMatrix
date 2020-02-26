from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import numpy as np
class ShowAnimation:
    def __init__(self, original_matrix):
        self.point_matrix = original_matrix

    def _set_axis_in_middle(self, ax):
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left') 

        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        ax.set_aspect(1)
    
    def _show_stage_init(self, x_range, y_range):
        figure, ax = plt.subplots()
        self._set_axis_in_middle(ax)
        ax.set_xlim(x_range[0], x_range[1])
        ax.set_ylim(y_range[0], y_range[1])
        line, = ax.plot([], [], animated=False)
        self.figure = figure
        self.ax = ax
        self.line = line
    
    def _update(self,frame):
        self.point_matrix = self.transform.Rotate(self.point_matrix, frame)
        self.line.set_data(self.point_matrix[0,:], self.point_matrix[1,:])
        return self.line

    def draw_transform(self, transform, f_range):
        self.transform = transform
        self._show_stage_init((-3,3),(-3,3))
        self.ani = FuncAnimation(self.figure, self._update, \
            frames = f_range\
            )
        plt.show()