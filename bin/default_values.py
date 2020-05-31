# Canvas default values
EMPTY_SPACE = 5  # Empty space around the canvas in the window
STITCH_COUNT = 14   # stitch count of fabric
STITCH_WIDTH = 20   # number of pixels of a single stitch
STITCH_HEIGHT = 20   # number of pixels of a single stitch
STITCH_NUMBER = 20   # number of stitches on the canvas

GRIDLINE_WIDTH = 1   # number of pixels in a gridline
CANVAS_BORDER_THICKNESS_CENTER = 2   # Number of pixels for the canvas' border
GRID_BOLD_INCREMENT = 10   # Every nth gridline is bold

# Item tags
GRID_TAG_BOLD = 'gridline_bold'
GRID_TAG_LIGHT = 'gridline_light'
CANVAS_BORDER_TAG = 'canvas_tag'

# Colors
GRID_COLOR_LIGHT = '#d3d3d3'
GRID_COLOR_BOLD = '#000000'
SYMBOL_COLOR = '#000000'
WINDOW_COLOR = '#a9a9a9'
CANVAS_COLOR = '#ffffff'
CANVAS_BORDER_COLOR = '#ff0000'
STITCH_COLOR = ''

# Thread colors (placeholder until there is a DB)
THREAD_BLACK = {'id': 1, 'name': 'Black', 'code': 'KLM 1', 'hexcode': '#ffffff'}
THREAD_GRAY = {'id': 2, 'name': 'Gray', 'code': 'KLM 2', 'hexcode': '#a9a9a9'}
THREAD_RED = {'id': 3, 'name': 'Red', 'code': 'KLM 3', 'hexcode': '#ff0000'}
THREAD_ORANGE = {'id': 4, 'name': 'Orange', 'code': 'KLM 4', 'hexcode': '#ff6600'}
THREAD_YELLOW = {'id': 5, 'name': 'Yellow', 'code': 'KLM 5', 'hexcode': '#ffff00'}
THREAD_GREEN = {'id': 6, 'name': 'Green', 'code': 'KLM 6', 'hexcode': '#00ff00'}
THREAD_BLUE = {'id': 7, 'name': 'Blue', 'code': 'KLM 7', 'hexcode': '#0000ff'}
THREAD_PURPLE = {'id': 8, 'name': 'Purple', 'code': 'KLM 8', 'hexcode': '#6600ff'}

# Palette (placeholder until there is a DB)
PALETTE = [
    THREAD_BLACK,
    THREAD_GRAY,
    THREAD_RED,
    THREAD_ORANGE,
    THREAD_YELLOW,
    THREAD_GREEN,
    THREAD_BLUE,
    THREAD_PURPLE
]

# Button Messages
BUTTON_TEXT_GRID_ON = 'Turn Grid Off'
BUTTON_TEXT_GRID_OFF = 'Turn Grid On'