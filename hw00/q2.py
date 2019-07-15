import sys
from PIL import Image

filename = str(sys.argv[1])

im = Image.open(filename)

out = im.transpose(Image.ROTATE_180)
out.save('result/ans2.png')
