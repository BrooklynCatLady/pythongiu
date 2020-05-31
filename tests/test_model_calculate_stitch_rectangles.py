import pytest
import sys
sys.path.append('bin')
from bin.model import Model

def test_calculate_grid_coordinates_default():
    '''
    Are the correct values returned when there is no border?
    '''
    canvas_width = 41   # pixles 0-40
    canvas_height = 81   # pixles 0-80
    stitch_width = 20
    stitch_height = 40
    model = Model()
    stitches = model.calculate_stitch_rectangles(canvas_width, canvas_height, stitch_width, stitch_height)
    assert len(stitches) == 4
    assert (0, 0, 20, 40) in stitches
    assert (20, 0, 40, 40) in stitches
    assert (0, 40, 20, 80) in stitches
    assert (20, 40, 40, 80) in stitches

def test_calculate_grid_coordinates_border():
    '''
    Are the correct values returned when there is a border?
    '''
    canvas_width = 47
    canvas_height = 86
    stitch_width = 20
    stitch_height = 40
    start_x = 2
    start_y = 3
    end_x = 4
    end_y = 2

    model = Model()
    stitches = model.calculate_stitch_rectangles(canvas_width, canvas_height, stitch_width, stitch_height,
                                                 start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y)
    assert len(stitches) == 4
    assert (2, 3, 22, 43) in stitches
    assert (22, 3, 42, 43) in stitches
    assert (2, 43, 22, 83) in stitches
    assert (22, 43, 42, 83) in stitches
