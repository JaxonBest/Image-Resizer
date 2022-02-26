from argparse import ArgumentParser
import os.path

# Make a function to resize and image in pillow
from PIL import Image

CM_PIXEL = 37.7952755906

def cm_to_pix(cm: float):
    return cm * CM_PIXEL
    
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

args.x = cm_to_pix(args.x)
args.y = cm_to_pix(args.y)

i = Image.open(args.f)
ii = i.resize((args.x, args.y))
ii.save(args.o)