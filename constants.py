import curses

stdscr = curses.initscr()

MIDDLE_SCREEN = int(curses.LINES // 2), int(curses.COLS // 2)

# X

MIN_X = 0
MAX_X = curses.COLS - 1
MIDDLE_X = MAX_X // 2
ONE_THIRD_X = MAX_X // 3
THREE_THIRDS_X = MAX_X - MAX_X // 3
QUARTER_X = MAX_X // 4
FIFTH_X = MAX_X // 5

# Y

MIN_Y = 0
MAX_Y = curses.LINES - 1
MIDDLE_Y = MAX_Y // 2
ONE_THIRD_Y = MAX_Y // 3
THREE_THIRDS_Y = MAX_Y - MAX_Y // 3
QUARTER_Y = MAX_Y // 4
FIFTH_Y = MAX_Y // 5

# Colors

GREEN = 1
RED = 2
WHITE = 3
YELLOW = 4
ORANGE = 5
CYAN = 6
WRONG_SPACE = 7

# Terminal

LINES = 15
SECURITY_COLS = 5
