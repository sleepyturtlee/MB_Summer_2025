from PIL import Image, ImageDraw
import random
# module to help convert hsl --> rgb
import colorsys


class Canvas:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.elements = []
        self.image = Image.new("RGB", (width, height), background_color)

    def add_element(self, element):
        self.elements.append(element)

    def render(self):
        draw = ImageDraw.Draw(self.image)
        for element in self.elements:
            element.draw(draw)
        #TODO:flip the image
        self.image = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        self.image.show()
        self.image.save("output.png")

class Circle:
    def __init__(self, attributes:dict):
        self.attributes = attributes # store the dictionary

    def draw(self, draw_context):
        x, y = self.attributes['position']
        r = self.attributes['radius']
        color = self.attributes['color']
        draw_context.ellipse([(x - r, y - r), (x + r, y + r)],
        fill=color
        )

class Rectangle:
    def __init__(self, attributes:dict):
        self.attributes = attributes # store the dictionary
    
    def draw (self, draw_context):
        x, y = self.attributes['position']
        # size = self.attributes['size']
        l = self.attributes['length']
        w = self.attributes['width']
        color = self.attributes['color']
        draw_context.rectangle((x, y, x + w, y + l, ), fill=color)
# end of classes

def rand_255():
    return random.randint(0, 256)

# normalizes color values for colorsys module and converts HSL to RgB
def to_rgb(hue_deg, lightness_percent, saturation_percent):
    h = hue_deg / 360.0
    l = lightness_percent / 100.0
    s = saturation_percent / 100.0
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r), int(g), int(b)

def main():
    # create the canvas
    canvas = Canvas(500, 500, (8, 3, 51))

    # stars
    for i in range(100):
        attrs = {
            "shape":"circle",
            "position":(random.randint(0, 500), random.randint(150, 500)),
            "radius":.1,
            "color":(255, 255, 255)
        }
        star = Circle(attrs)
        canvas.add_element(star)

    # full moon x position (this var is declared first 
    # and in scope of whole function because I need to use it multiple times)
    full_moon_x_pos = random.randint(50, 450)
    full_moon_y_pos = random.randint(350, 430)

    # create a crescent moon
    # first make a full moon..
    full_moon_attrs = {
        "shape":"circle",
        "position":(full_moon_x_pos, full_moon_y_pos),
        "radius":50,
        "color":(255, 250, 117)
    }
    full_moon = Circle(full_moon_attrs)
    canvas.add_element(full_moon)

    # create a dark patch (the same color as the sky) to cover some of the moon to make a crescent shape
    dark_patch_attrs = {
        "shape":"circle",
        "position":(full_moon_x_pos+10, full_moon_y_pos+5),
        # 43 radius just looks good to me, change however you like
        "radius":43,
        "color":(8, 3, 51)
    }
    dark_patch = Circle(dark_patch_attrs)
    canvas.add_element(dark_patch)

    # generate the buildings
    # create back row of buildings (darkest)
    for i in range(30):
        attrs = {
        "shape":"rectangle",
        "position":(random.randint(0, canvas.width), 0),
        # controls the height of the buildings
        "length":random.randint(5, 330),
        # width of the buildings
        "width":random.randint(20, 100),
        # color of the buildings
        "color": (32, 34, 69)# randomized rgb
        }
        element = Rectangle(attrs)
        canvas.add_element(element)
    
    # create middle row of buildings (mid-light)
    for i in range(20):
        attrs = {
        "shape":"rectangle",
        "position":(random.randint(0, canvas.width), 0),
        # controls the height of the buildings
        "length":random.randint(5, 270),
        # width of the buildings
        "width":random.randint(20, 100),
        # color of the buildings
        "color": (67, 71, 145)# randomized rgb
        }
        element = Rectangle(attrs)
        canvas.add_element(element)
    
    # create front row of buildings (lightest)
    for i in range(10):
        attrs = {
        "shape":"rectangle",
        "position":(random.randint(0, canvas.width), 0),
        # controls the height of the buildings
        "length":random.randint(5, 250),
        # width of the buildings
        "width":random.randint(20, 100),
        # color of the buildings
        "color": (93, 98, 201)# randomized rgb
        }
        element = Rectangle(attrs)
        canvas.add_element(element)
            

    canvas.render() # render canvas

main()

"""
NOTE: The canvas is flipped upside down, and therefore so are the coordinates
left to right: still 0 --> 400
up to down: 400 --> 0
"""