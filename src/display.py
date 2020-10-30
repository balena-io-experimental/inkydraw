import logging
from PIL import Image, ImageFont, ImageDraw
from font_source_sans_pro import SourceSansPro
import layout

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


class Display:
    def __init__(self, display_type, rotate = False):
        self.display_type = display_type
        self.default_font = SourceSansPro
        self.rotate = rotate

        if self.display_type == "WAVESHARE":
            logging.info("Display type: Waveshare")
            import lib.epd2in13_V2
            dsp = lib.epd2in13_V2.EPD()
            dsp.init(dsp.FULL_UPDATE)
            dsp.Clear(0xFF)
            # These are the opposite of what InkyPhat uses.
            self.display_width = dsp.height # yes, height
            self.display_height = dsp.width # yes, width
            self.color_black = "black"
            self.color_white = "white"
            self.display = dsp
        else:
            import inky
            dsp = inky.auto()
            logging.info("Display type: " + type(dsp).__name__)
            dsp.set_border(dsp.WHITE)

            self.display_width = dsp.WIDTH
            self.display_height = dsp.HEIGHT
            self.color_black = dsp.BLACK
            self.color_white = dsp.WHITE
            self.display = dsp

        logging.info("Display dimensions: W %s x H %s", self.display_width, self.display_height)

    def draw(self, content):
        img = self.get_image(content)
        if self.display_type == "WAVESHARE":
            # epd does not have a set_image method.
            self.display.dsp(dsp.getbuffer(img))
        else:
            self.display.set_image(img)
            self.display.show()

    def get_image(self, content):
        img = self.get_empty_image()
        draw = ImageDraw.Draw(img)

        def estimate_text_size(text, font_size):
            font = ImageFont.truetype(self.default_font, font_size)
            return draw.multiline_textsize(text, font=font, spacing=0)

        # TODO: There is some white-space when you draw a font at `y=0`, and tail of characters like `y` is cut off when drawn at the end of the screen, resolve it.
        def draw_calculated_entry(entry):
            if entry["type"] == "text":
                font = ImageFont.truetype(self.default_font, entry["font_size"])
                draw.multiline_text((entry["x"],entry["y"]), entry["content"], self.color_black, font=font, spacing=0)

        calculated_layout = layout.calculate_layout(content, {
            "estimate_text_size": estimate_text_size,
            "display_width": self.display_width,
            "display_height": self.display_height,
        })

        for entry in calculated_layout:
            draw_calculated_entry(entry)
        return img
    
    def get_empty_image(self):
        img = Image.new("P", (self.display_width, self.display_height))
        if self.display_type == "WAVESHARE":
            img = Image.new('1', (self.display_width, self.display_height), 255)
        if self.rotate is True:
            img = img.rotate(180)
        return img
