import PIL
# from PIL import *
from PIL import Image

img = PIL.Image.open("F:/pics/GOEL FAMILY.JPG")
width, height = img.size

print((width, "x", height))
