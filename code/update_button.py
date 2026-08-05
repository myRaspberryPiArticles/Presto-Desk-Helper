from presto import Presto
from touch import Button
import time

presto = Presto()
display = presto.display

TEXT_BLUE = display.create_pen(34, 36, 91)
LIGHT_BLUE = display.create_pen(234, 248, 251)
BLACK = display.create_pen(0, 0, 0)

display.set_pen(LIGHT_BLUE)
display.text("┃┃┃┏━┛┃  ┏━┛┏━┃┏┏ ┏━┛", 30, 50, scale=2)