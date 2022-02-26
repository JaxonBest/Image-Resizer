from argparse import ArgumentParser
import os.path

# Make a function to resize and image in pillow
from PIL import Image

def resize_img(img: Image, x: float, y: float):
    resized = img.resize((x, y))
    return resized

# Add argument x and y which are floats & required.
parser = ArgumentParser(description='hello!')
parser.add_argument("x", type=float, help="x value", required=True)
parser.add_argument("y", type=float, help="y value", required=True)
parser.add_argument("f", type=float, help="file path", required=True)
parser.add_argument("o", type=float, help="out file path", required=True)
parser.add_argument('O', 'override', help='override out file', required=True, action='store_true')

args = parser.parse_args()

if os.path.isfile(args.o):
    print("File already exists")
    if not args.override:
        print('Exiting')
        exit(1)
    else:
        print('Overriding file.')

i = Image.open(args.f)
ii = i.resize((args.x, args.y))
ii.save(args.o)