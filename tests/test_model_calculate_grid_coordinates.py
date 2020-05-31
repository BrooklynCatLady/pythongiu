import pytest
import sys
sys.path.append('bin')
from bin.model import Model

def test_calculate_grid_coordinates_default():
    '''
    Are the correct values returned when there is no increment?
    '''
    canvas_width = 41   # pixles 0-40
    canvas_height = 81   # pixles 0-80
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 20, 40)
    assert len(coordinates) == 6
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (20, 0, 20, canvas_height-1) in coordinates
    assert (40, 0, 40, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 40, canvas_width-1, 40) in coordinates
    assert (0, 80, canvas_width-1, 80) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_default_increment_zero():
    '''
    Are the correct values returned when there is no increment?
    '''
    canvas_width = 41   # pixles 0-40
    canvas_height = 81   # pixles 0-80
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 20, 40, 0)
    assert len(coordinates) == 6
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (20, 0, 20, canvas_height-1) in coordinates
    assert (40, 0, 40, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 40, canvas_width-1, 40) in coordinates
    assert (0, 80, canvas_width-1, 80) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_default_uneven():
    '''
    Are the correct values returned when there is no increment and there is a half square on the right and bottom?
    '''
    canvas_width = 51   # pixles 0-50
    canvas_height = 91   # pixles 0-90
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 20, 40)
    assert len(coordinates) == 6
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (20, 0, 20, canvas_height-1) in coordinates
    assert (40, 0, 40, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 40, canvas_width-1, 40) in coordinates
    assert (0, 80, canvas_width-1, 80) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_default_zero_width():
    '''
    Are the correct values returned when there is no increment and the width is 0? THere is a minimum of 3
    '''
    canvas_width = 7  # 0-6
    canvas_height = 9  # 0-8
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 0, 4)
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (3, 0, 3, canvas_height-1) in coordinates
    assert (6, 0, 6, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 4, canvas_width-1, 4) in coordinates
    assert (0, 8, canvas_width-1, 8) in coordinates
    assert len(coordinates) == 6
    assert len(other) == 0


def test_calculate_grid_coordinates_default_zero_height():
    '''
    Are the correct values returned when there is no increment and the thickness is 0? THere is a minimum of 3
    '''
    canvas_width = 9  #0-8
    canvas_height = 7  #0-6
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 4, 0)
    assert len(coordinates) == 6
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (4, 0, 4, canvas_height-1) in coordinates
    assert (8, 0, 8, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 3, canvas_width-1, 3) in coordinates
    assert (0, 6, canvas_width-1, 6) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_default_negative_width():
    '''
    Are the correct values returned when there is no increment and the width is negative?
    '''
    canvas_width = 7   # 0-6
    canvas_height = 9   # 0-8
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, -5, 4)
    assert len(coordinates) == 6
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (3, 0, 3, canvas_height-1) in coordinates
    assert (6, 0, 6, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 4, canvas_width-1, 4) in coordinates
    assert (0, 8, canvas_width-1, 8) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_default_negative_height():
    '''
    Are the correct values returned when there is no increment and the thickness is negative?
    '''
    canvas_width = 9  #0-8
    canvas_height = 7  #0-6
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 4, -10)
    assert len(coordinates) == 6
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (4, 0, 4, canvas_height-1) in coordinates
    assert (8, 0, 8, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 3, canvas_width-1, 3) in coordinates
    assert (0, 6, canvas_width-1, 6) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_increment():
    '''
    Are the correct values returned when there is an increment?
    '''
    canvas_width = 101
    canvas_height = 201
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 10, 20, increment=5)
    assert len(coordinates) == 6
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (50, 0, 50, canvas_height-1) in coordinates
    assert (100, 0, 100, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 100, canvas_width-1, 100) in coordinates
    assert (0, 200, canvas_width-1, 200) in coordinates
    assert len(other) == 16
    assert (10, 0, 10, canvas_height-1) in other
    assert (20, 0, 20, canvas_height-1) in other
    assert (30, 0, 30, canvas_height-1) in other
    assert (40, 0, 40, canvas_height-1) in other
    assert (60, 0, 60, canvas_height-1) in other
    assert (70, 0, 70, canvas_height-1) in other
    assert (80, 0, 80, canvas_height-1) in other
    assert (90, 0, 90, canvas_height-1) in other
    assert (0, 20, canvas_width-1, 20) in other
    assert (0, 40, canvas_width-1, 40) in other
    assert (0, 60, canvas_width-1, 60) in other
    assert (0, 80, canvas_width-1, 80) in other
    assert (0, 120, canvas_width-1, 120) in other
    assert (0, 140, canvas_width-1, 140) in other
    assert (0, 160, canvas_width-1, 160) in other
    assert (0, 180, canvas_width-1, 180) in other


def test_calculate_grid_coordinates_increment_uneven():
    '''
    Are the correct values returned when there is an increment when there is unevenly divisible number of gridlines?
    '''
    canvas_width = 101
    canvas_height = 201
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 10, 20, increment=3)
    assert len(coordinates) == 8
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (30, 0, 30, canvas_height-1) in coordinates
    assert (60, 0, 60, canvas_height-1) in coordinates
    assert (90, 0, 90, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 60, canvas_width-1, 60) in coordinates
    assert (0, 120, canvas_width-1, 120) in coordinates
    assert (0, 180, canvas_width-1, 180) in coordinates
    assert len(other) == 14
    assert (10, 0, 10, canvas_height-1) in other
    assert (20, 0, 20, canvas_height-1) in other
    assert (40, 0, 40, canvas_height-1) in other
    assert (50, 0, 50, canvas_height-1) in other
    assert (70, 0, 70, canvas_height-1) in other
    assert (80, 0, 80, canvas_height-1) in other
    assert (100, 0, 100, canvas_height-1) in other
    assert (0, 20, canvas_width-1, 20) in other
    assert (0, 40, canvas_width-1, 40) in other
    assert (0, 80, canvas_width-1, 80) in other
    assert (0, 100, canvas_width-1, 100) in other
    assert (0, 140, canvas_width-1, 140) in other
    assert (0, 160, canvas_width-1, 160) in other
    assert (0, 200, canvas_width-1, 200) in other


def test_calculate_grid_coordinates_increment_negative():
    '''
    Are the correct values returned when there is an increment that is negative?
    '''
    canvas_width = 73
    canvas_height = 85
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 10, 20, increment=-4)

    print(coordinates)
    assert len(coordinates) == 13
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (10, 0, 10, canvas_height-1) in coordinates
    assert (20, 0, 20, canvas_height-1) in coordinates
    assert (30, 0, 30, canvas_height-1) in coordinates
    assert (40, 0, 40, canvas_height-1) in coordinates
    assert (50, 0, 50, canvas_height-1) in coordinates
    assert (60, 0, 60, canvas_height-1) in coordinates
    assert (70, 0, 70, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert (0, 20, canvas_width-1, 20) in coordinates
    assert (0, 40, canvas_width-1, 40) in coordinates
    assert (0, 60, canvas_width-1, 60) in coordinates
    assert (0, 80, canvas_width-1, 80) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_increment_large():
    '''
    Are the correct values returned when there is an increment and it is larger than the max value?
    '''
    canvas_width = 101
    canvas_height = 201
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 10, 20, increment=25)
    assert len(coordinates) == 2
    assert (0, 0, 0, canvas_height-1) in coordinates
    assert (0, 0, canvas_width-1, 0) in coordinates
    assert len(other) == 20
    assert (10, 0, 10, canvas_height-1) in other
    assert (20, 0, 20, canvas_height-1) in other
    assert (30, 0, 30, canvas_height-1) in other
    assert (40, 0, 40, canvas_height-1) in other
    assert (50, 0, 50, canvas_height-1) in other
    assert (60, 0, 60, canvas_height-1) in other
    assert (70, 0, 70, canvas_height-1) in other
    assert (80, 0, 80, canvas_height-1) in other
    assert (90, 0, 90, canvas_height-1) in other
    assert (100, 0, 100, canvas_height-1) in other
    assert (0, 20, canvas_width-1, 20) in other
    assert (0, 40, canvas_width-1, 40) in other
    assert (0, 60, canvas_width-1, 60) in other
    assert (0, 80, canvas_width-1, 80) in other
    assert (0, 100, canvas_width-1, 100) in other
    assert (0, 120, canvas_width-1, 120) in other
    assert (0, 140, canvas_width-1, 140) in other
    assert (0, 160, canvas_width-1, 160) in other
    assert (0, 180, canvas_width-1, 180) in other
    assert (0, 200, canvas_width-1, 200) in other


def test_calculate_grid_coordinates_end():
    '''
    Are the correct values returned when there is no increment but starting and ending positions?
    '''
    canvas_width = 50    # pixles 0-49, 0-1 | 2-42 | 43-49
    canvas_height = 89   # pixles 0-86, 0-2 | 3-83 | 84-88
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 20, 40,
                                                          start_x=2, start_y=3, end_x=7, end_y=5)
    assert len(coordinates) == 6
    assert (2, 3, 2, 83) in coordinates
    assert (22, 3, 22, 83) in coordinates
    assert (42, 3, 42, 83) in coordinates
    assert (2, 3, 42, 3) in coordinates
    assert (2, 43, 42, 43) in coordinates
    assert (2, 83, 42, 83) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_end_thick_border():
    '''
    Are the correct values returned when there is no increment but starting and ending positions and a very thick border?
    '''
    canvas_width = 101    # pixles 0-49, 0-1 | 2-42 | 43-100
    canvas_height = 401   # pixles 0-86, 0-2 | 3-83 | 84-400
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 20, 40,
                                                          start_x=2, start_y=3, end_x=58, end_y=317)
    assert len(coordinates) == 6
    assert (2, 3, 2, 83) in coordinates
    assert (22, 3, 22, 83) in coordinates
    assert (42, 3, 42, 83) in coordinates
    assert (2, 3, 42, 3) in coordinates
    assert (2, 43, 42, 43) in coordinates
    assert (2, 83, 42, 83) in coordinates
    assert len(other) == 0


def test_calculate_grid_coordinates_start_increment():
    '''
    Are the correct values returned when there is an increment and a starting position?
    '''
    canvas_width = 101
    canvas_height = 148
    model = Model()
    coordinates, other = model.calculate_grid_coordinates(canvas_width, canvas_height, 10, 20, start_x=4, start_y=6, increment=3)
    assert len(coordinates) == 7

    print(coordinates)
    print(other)

    assert (4, 6, 4, canvas_height-1) in coordinates
    assert (34, 6, 34, canvas_height-1) in coordinates
    assert (64, 6, 64, canvas_height-1) in coordinates
    assert (94, 6, 94, canvas_height-1) in coordinates
    assert (4, 6, canvas_width-1, 6) in coordinates
    assert (4, 66, canvas_width-1, 66) in coordinates
    assert (4, 126, canvas_width-1, 126) in coordinates
    assert len(other) == 11
    assert (14, 6, 14, canvas_height-1) in other
    assert (24, 6, 24, canvas_height-1) in other
    assert (44, 6, 44, canvas_height-1) in other
    assert (54, 6, 54, canvas_height-1) in other
    assert (74, 6, 74, canvas_height-1) in other
    assert (84, 6, 84, canvas_height-1) in other
    assert (4, 26, canvas_width-1, 26) in other
    assert (4, 46, canvas_width-1, 46) in other
    assert (4, 86, canvas_width-1, 86) in other
    assert (4, 106, canvas_width-1, 106) in other
    assert (4, 146, canvas_width-1, 146) in other
