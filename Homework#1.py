antigravity = "\t\timport antigravity"
helloString = "\n\t\timport __hello__"
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

print("Escape sequences")

data1 = ("\\a\t\tBell(alert)\n\\b\t\tBackspace\n\\n\t\tNew line\n\\t\t\tHorizontal tab")

data2 = ('\n\ \t\tBacklash(\)\n\ "\t\tDouble quotation mark " ')

data3 = ("\n\ '\t\tSingle quotation mark ' ")

print(data1 + data2 + data3)
