from bin.default_values import *

class Model():

    def __init__(self):
        '''
        Define starting values for the model
        '''
        self.set_new_project()

    def set_new_project(self):
        '''
        Parameters for a new default project
        '''
        self.set_canvas_parameters()
        self.set_window_parameters()
        self.set_grid_spacing()
        self.set_grid_colors()
        self.turn_grid_on()

    def set_window_parameters(self):
        '''
        Set the values used to define the window
        '''
        self.window_size = self.canvas_width + 2*EMPTY_SPACE
        self.window_color = WINDOW_COLOR


    def calculate_grid_coordinates(self, canvas_width, canvas_height, line_distance_x, line_distance_y, start_x=0, start_y=0, end_x=0, end_y=0, increment=1):
        '''
        Reuseable Function that calculates grid coordinates for any lines that make a grid
        stitch_width = the distance in pixels of the stitch's width, also the distance between the gridlines
        stitch_height = the distance in pixels of the stitch's height, also the distance between the gridlines
        stitch_increment = the nth stitch is in first list, the rest are in the second list
        '''
        # Assign minimums to parameters:
        if line_distance_x <= 3: line_distance_x = 3
        if line_distance_y <= 3: line_distance_y = 3
        if increment < 1: increment = 1

        # Define endpoints
        min_x = start_x
        min_y = start_y
        max_x = canvas_width - end_x - 1
        max_y = canvas_height - end_y - 1

        print("In calc")
        print(min_x, min_y, max_x, max_y, increment)

        # Find the coordinates
        increment_coordinates, other_coordinates = [], []
        inc_counter = 0
        for i in range(0, int((max_x-min_x)/line_distance_x)+1):
            coord_tuple = (i*line_distance_x+min_x, min_y, i*line_distance_x+min_x, max_y)
            if inc_counter//increment == inc_counter/increment:
                increment_coordinates.append(coord_tuple)
            else:
                other_coordinates.append(coord_tuple)
            inc_counter += 1
        inc_counter = 0
        for j in range(0, int((max_y-min_y)/line_distance_y)+1):
            coord_tuple = (min_x, j*line_distance_y+min_y, max_x, j*line_distance_y+min_y)
            if inc_counter//increment == inc_counter/increment:
                increment_coordinates.append(coord_tuple)
            else:
                other_coordinates.append(coord_tuple)
            inc_counter += 1
        return increment_coordinates, other_coordinates

    def set_grid_spacing(self):
        '''
        Set the spacing and thickness of the grid
        '''
        self.grid_tag_bold = GRID_TAG_BOLD
        self.grid_tag_light = GRID_TAG_LIGHT
        self.grid_spacing_width = STITCH_WIDTH
        self.grid_spacing_height = STITCH_HEIGHT
        self.grid_bold_increment = GRID_BOLD_INCREMENT
        # The grid start at the top and left of the border
        self.grid_start_x = self.canvas_border_thickness
        self.grid_start_y = self.canvas_border_thickness
        # The grid overlaps with the bottom and right of the border
        self.grid_end_x = self.canvas_border_thickness-1
        self.grid_end_y = self.canvas_border_thickness-1

    def set_grid_colors(self):
        '''
        Set the grid colors
        '''
        self.grid_color_light = GRID_COLOR_LIGHT
        self.grid_color_bold = GRID_COLOR_BOLD
        self.grid_thickness = GRIDLINE_WIDTH

    def set_canvas_parameters(self):
        '''
        Set the parameters used to define the working canvas
        '''
        self.canvas_border_thickness = 2*CANVAS_BORDER_THICKNESS_CENTER + 1
        self.canvas_border_line = CANVAS_BORDER_THICKNESS_CENTER
        self.canvas_width = STITCH_NUMBER*STITCH_WIDTH + 2*self.canvas_border_thickness
        self.canvas_height = STITCH_NUMBER * STITCH_HEIGHT + 2*self.canvas_border_thickness
        self.canvas_working_width = STITCH_NUMBER*STITCH_WIDTH + 2*self.canvas_border_line + 1
        self.canvas_working_height = STITCH_NUMBER*STITCH_HEIGHT + 2*self.canvas_border_line + 1
        self.canvas_border_color = CANVAS_BORDER_COLOR
        self.canvas_border_tag = CANVAS_BORDER_TAG
        self.canvas_color = CANVAS_COLOR

    def grid_toggle_state(self):
        '''
        Change the state of the grid on & off
        '''
        if self.is_grid_on is True:
            self.turn_grid_off()
        else:
            self.turn_grid_on()

    def turn_grid_on(self):
        '''
        Do all the things that turn a grid on
        '''
        self.is_grid_on = True
        self.button_grid_toggle_text = BUTTON_TEXT_GRID_ON

    def turn_grid_off(self):
        '''
        Do all the things that turn a grid off
        '''
        self.is_grid_on = False
        self.button_grid_toggle_text = BUTTON_TEXT_GRID_OFF
