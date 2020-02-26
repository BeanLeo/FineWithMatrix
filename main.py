import shapes
import basic_matrix as bm
import animation as an
import math
import numpy as np
def main():
    squre = shapes.Square()
    squre.gen_shape_point_clockwise()
    transformer = bm.matrix_transform()
    anshow = an.ShowAnimation(squre.point_matrix)
    f_range = np.linspace(0, 2*np.pi,128)
    anshow.draw_transform(transformer,f_range)    
    #rotate_45 = transformer.Rotate(squre.point_matrix, math.pi/4)
    #squre.point_matrix = rotate_45
    #squre.draw_shape()

if __name__ == "__main__":
    main()