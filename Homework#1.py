antigravity = "\t\timport antigravity"
helloString = "\n\t\timport__hello__"
futureString = "\n\t\tfrom __future__ import braces"
print(antigravity + helloString + futureString)

from PIL import Image, ImageDraw

im = Image.new('1', (80, 24), color=1)
draw = ImageDraw.Draw(im)
draw.text((5, 5), 'V L A D')
for i in range(im.height):
    for j in range(im.width):
        print('* '[im.getpixel((j, i))], end='')
    print()



