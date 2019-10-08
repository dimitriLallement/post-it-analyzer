import yaml
import post_it_color
from PIL import Image

def nearest_color(file, configFile = "test/color_config.yml"):
    """Return an PostItColor instance corresponding at the input post-it image"""
    image = Image.open(file)
    main_color = most_frequent_color(image)
    configured_colors = load_config(configFile)
    min_color = {}
    #Compute the Euclidean distance for each color
    for colors in configured_colors:
        red_distance = (colors.rgb[0] - main_color[0]) ** 2
        green_distance = (colors.rgb[1] - main_color[1]) ** 2
        blue_distance = (colors.rgb[2] - main_color[2]) ** 2
        min_color[red_distance + green_distance + blue_distance] = colors
    detected_color = min_color[min(min_color.keys())]
    print("[Debug] - Reference detected color: {0} (RGB: {1}) - Type: {2}".format(detected_color.color, detected_color.rgb, detected_color.type))
    return(detected_color)


def most_frequent_color(image):
    """Return the RGB code corresponding at the most frequent color in the input image. 
    It allows to retrieve the real color of the post-it"""
    w, h = image.size
    pixels = image.getcolors(w * h)
    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

    print("[Debug] - Real post-it color (RGB): {0}".format(most_frequent_pixel[1]))
    return most_frequent_pixel[1]


def load_config(config_file):
    """Open the YAML configuration file given in parameter"""
    with open(config_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("[Error] - Error while opening the YAML conf file: {}".format(exc))
