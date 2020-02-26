import shapes
import basic_matrix as bm
import math
def main():
    squre = shapes.Square()
    squre.gen_shape_point_clockwise()
    transformer = bm.matrix_transform()
    rotate_45 = transformer.Rotate(squre.point_matrix, math.pi/4)
    squre.point_matrix = rotate_45
    squre.draw_shape()

if __name__ == "__main__":
    main()