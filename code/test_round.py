from presto import Presto
from picovector import PicoVector, Polygon

presto = Presto()
vector = PicoVector(presto.display)
display = presto.display

my_shape = Polygon()

LIGHT_BLUE = display.create_pen(234, 248, 251)
display.set_pen(LIGHT_BLUE)
vector.draw(update_button.rectangle(5, 5, 40, 20, corners=(7, 7, 7, 7), stroke=0))
presto.update()