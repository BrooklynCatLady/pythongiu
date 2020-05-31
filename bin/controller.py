from tkinter import Tk as tktk
from bin.model import Model
from bin.view import View


class Controller():

    def __init__(self):
        '''
        Initial state and parameters/objects that don't change over time
        '''
        self.root = tktk()
        self.model = Model()
        self.view = View(self.root, self.model.window_color, self.model.window_size)
        self.view.draw_window()
        # Make menus
        self.view.draw_toolbar(self.model.button_grid_toggle_text)
        # Add commands
        self.new_project()
        self.view.button_grid_toggle.configure(command=self.toggle_grid)


    def run(self):
        self.root.title("Cool Stitch Program")
        self.root.mainloop()

    def new_project(self):
        '''
        Run the functions to start a new project
        '''
        self.new_canvas()
        self.generate_stitches()
        self.generate_grid()
        self.starting_palette()

    def generate_toolbar(self):
        '''
        Generate the toolbar
        '''
        self.view.draw_toolbar(self.model.button_grid_toggle_text)

    def new_canvas(self):
        '''
        Create a new canvas to work on
        '''
        # Clear canvas id one is there???
        self.view.draw_canvas(self.model.canvas_width, self.model.canvas_height, self.model.canvas_color)
        egde_lines, other = self.model.calculate_grid_coordinates(self.model.canvas_width, self.model.canvas_height,
                                                           self.model.canvas_working_width, self.model.canvas_working_height,
                                                           start_x=self.model.canvas_border_line, start_y=self.model.canvas_border_line,
                                                           end_x=self.model.canvas_border_line, end_y=self.model.canvas_border_line)
        self.view.draw_lines(egde_lines, self.model.canvas_border_color, self.model.canvas_border_thickness, self.model.canvas_border_tag)

    def generate_grid(self):
        '''
        Generate the grid
        '''
        # Set the colors and positions before building the grid
        self.model.set_grid_colors()
        gridlines_bold, gridlines_light = self.model.calculate_grid_coordinates(self.model.canvas_width, self.model.canvas_height,
                                                                                self.model.grid_spacing_width, self.model.grid_spacing_height,
                                                                                start_x=self.model.grid_start_x, start_y=self.model.grid_start_y,
                                                                                end_x=self.model.grid_end_x, end_y=self.model.grid_end_y,
                                                                                increment=self.model.grid_bold_increment)
        # Pass these to the view where the gridlines are drawn
        self.view.draw_lines(gridlines_light, self.model.grid_color_light, self.model.grid_thickness, self.model.grid_tag_light)
        self.view.draw_lines(gridlines_bold, self.model.grid_color_bold, self.model.grid_thickness, self.model.grid_tag_bold)

    def toggle_grid(self):
        '''
        Turn the grid on and off when clicking it
        '''
        self.model.grid_toggle_state()
        self.view.toggle_grid(self.model.is_grid_on, self.model.button_grid_toggle_text, [self.model.grid_tag_light, self.model.grid_tag_bold])

    def generate_stitches(self):
        '''
        Generate the stitches
        '''
        rectangle_coordinates = self.model.calculate_stitch_rectangles(self.model.canvas_width, self.model.canvas_height,
                                                                       self.model.grid_spacing_width, self.model.grid_spacing_height,
                                                                       start_x=self.model.grid_start_x, start_y=self.model.grid_start_y,
                                                                       end_x=self.model.grid_end_x, end_y=self.model.grid_end_y)
        self.stitch_dict = self.view.draw_new_stitches(rectangle_coordinates, self.model.stitch_color)

    def starting_palette(self):
        '''
        Get a new color from the palette ready in the stitches
        '''
        self.model.set_palette_color()
        self.view.set_stitch_color(self.model.stitch_color)



