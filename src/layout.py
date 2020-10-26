import math

# Start with an arbitrarily large font and reduce until we make the content fit.
STARTING_FONT_SIZE = 24

def fit_text(text, font_size, height, width, estimate_text_size):
    estimated_width, estimated_height = estimate_text_size(text, font_size)
    if estimated_height > height or estimated_width > width:
        # naive implementation, use divide and conquer instead.
        return fit_text(text, font_size - 1, height, width, estimate_text_size)
    else:
        return font_size, estimated_height, estimated_width

def get_positioned_coordinate(point, full_size, content_size, position):
    print(point, full_size, content_size)
    if position == "start":
        return point
    if position == "center":
        return point + math.ceil(full_size / 2 - content_size / 2)
    if position == "end":
        return point + (full_size - content_size)

def convert(content_obj, options):
    start_x = math.ceil(options["display_width"] * content_obj["x"])
    start_y = math.ceil(options["display_height"] * content_obj["y"])
    width = math.floor(options["display_width"] * content_obj["w"]) - start_x
    height = math.floor(options["display_height"] * content_obj["h"]) - start_y
    content_height = height
    content_width = width
    
    res = { "content": content_obj["content"], "type": content_obj["type"] }
    if content_obj ["type"] == "text":
        font_size, content_height, content_width = fit_text(
            content_obj["content"],
            content_obj["font_size"] if "font_size" in content_obj else STARTING_FONT_SIZE, 
            height, 
            width, 
            options["estimate_text_size"]
            )
        res["font_size"] = font_size

    x = get_positioned_coordinate(start_x, width, content_width, content_obj["justify"])
    y = get_positioned_coordinate(start_y, height, content_height, content_obj["align"])
    res["x"] = x
    res["y"] = y

    return res
    
def calculate_layout(content, options):
    return list(map(lambda entry: convert(entry, options), content))
    