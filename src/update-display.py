# import json
import logging
# import math
# from pathlib import Path
import os
import sys
import time
# import textwrap
from display import Display

# Read the preset environment variables and overwrite the default ones
if "DEBUG" in os.environ:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

# def create_mask(source):
#     """Create a transparency mask to draw images in grayscale
#     """
#     logging.info("Creating a transparency mask for the image")
#     mask_image = Image.new("1", source.size)
#     w, h = source.size
#     for x in range(w):
#         for y in range(h):
#             p = source.getpixel((x, y))
#             if p in [BLACK, WHITE]:
#                 mask_image.putpixel((x, y), 255)
#     return mask_image

content=[]

content.append({
    "x": 0,
    "y": 0,
    "w": 0.5,
    "h": 0.5,
    "type": "text",
    "align": "center", # start | center | end
    "justify": "center", # start | center | end
    "content": "Hey there"
})


display = Display("INKYPHAT", "ROTATE" in os.environ)
display.draw(content)
time.sleep(6000)
logging.info("Done drawing")
sys.exit(0)
