# -*- coding: utf-8 -*-
# image=image.point(lambda x: 0 if x<50 else 255)这是关键！#
# 关乎识别的准确率#
url = 'http://web.hunanjz.com/Action/VerifyCode.ashx'

from urllib.request import urlopen
path = urlopen(url)
from PIL import Image
from PIL import ImageOps
import tesserocr

def cleanImage(imagePath):

    imagex = Image.open(imagePath)
    imgry = imagex.convert('L')

    table = get_bin_table()
    out = imgry.point(table,'1')

    imgry.show()
    #imgry = imgry.point(lambda x: 0 if x < 50 else 255)
    borderImage = ImageOps.expand(imgry, border=5, fill=255)
    borderImage.save("./1.png")
    y = Image.open('1.png')
    x = tesserocr.image_to_text(y)
    return x

def get_bin_table(threshold = 160):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


x = cleanImage(path)
print(x)