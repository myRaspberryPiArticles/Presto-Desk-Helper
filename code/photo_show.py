import picographics
import jpegdec
from presto import Presto

presto = Presto()

display = presto.display

# Create a new JPEG decoder for our PicoGraphics
j = jpegdec.JPEG(display)

# Open the JPEG file
j.open_file("moon.jpeg")

# Decode the JPEG
j.decode(0, 0, jpegdec.JPEG_SCALE_FULL, dither=False)

# Display the result
presto.update()