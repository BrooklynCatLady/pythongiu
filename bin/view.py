import tkinter  as tk

class View():

    def __init__(self, tkwindow, window_color, window_size):
        '''
        Initialize the window
        '''
        self.tkwindow = tkwindow
        self.window_color = window_color
        self.window_size_dim = '{0}x{0}'.format(window_size)

    def draw_window(self):
        '''
        Draw the window
        '''
        self.tkwindow.configure(bg=self.window_color)
        self.tkwindow.geometry(self.window_size_dim)

    def draw_toolbar(self, button_grid_toggle_text):
        '''
        Generate the canvas toolbar
        '''
        self.canvas_toolbar = tk.Frame(self.tkwindow, bd=1, relief=tk.RAISED)
        self.button_grid_toggle = tk.Button(self.canvas_toolbar, relief=tk.FLAT, text=button_grid_toggle_text)
        self.button_grid_toggle.pack(side=tk.LEFT, padx=2, pady=2)
        self.canvas_toolbar.pack(side=tk.TOP, fill=tk.X)

    def draw_canvas(self, width, height, color):
        '''
        Create the canvas to draw the pattern on
        '''
        self.canvas = tk.Canvas(self.tkwindow, width=width, height=height, background=color, highlightthickness=0)
        self.canvas.pack()

    def draw_lines(self, position_tuples, line_color, line_thickness, tag_name):
        '''
        Draw the actual gridlines in the correct places
        '''
        line_list = []
        for positions in position_tuples:
            x0 = positions[0]
            y0 = positions[1]
            x1 = positions[2]
            y1 = positions[3]
            line_list.append(self.canvas.create_line(x0, y0, x1, y1, fill=line_color, width=line_thickness, tag=tag_name))
        return line_list

    def toggle_grid(self, is_grid_on, button_text, tag_list):
        '''
        Toggle the grid on and off
        '''
        self.button_grid_toggle.config(text=button_text)
        for tag in tag_list:
            if is_grid_on:
                self.canvas.itemconfig(tag, state=tk.NORMAL)
            else:
                self.canvas.itemconfig(tag, state=tk.HIDDEN)
