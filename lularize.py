import sys
import os
from PIL import Image, ImageFont, ImageDraw
import random

colors = [
    (254, 209, 65),
    (255, 157, 110),
    (246, 117, 153),
    (221, 127, 211),
    (149, 149, 210),
    (139, 184, 232),
    (100, 204, 201),
    (136, 139, 141)]

styleData = {
    'joy': {'price': 60, 'sizes': ['xs', 's', 'm', 'l', 'xl']},
    'tween': {'price': 23},
    'tall_&_curvy': {'price': 25},
    'kids_s/m': {'price': 23},
    'sloan': {'price': 28, 'sizes': [2, 4, 6, 8, 10, 12, 14]},
    'sarah': {'price': 70, 'sizes': ['xs', 's', 'm', 'l', 'xl']},
    'randy': {'price': 35, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'perfect_t': {'price': 36, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'patrick': {'price': 40, 'sizes': ['m', 'l', 'xl', '2xl', '3xl']},
    'one_size': {'price': 25},
    'nicole': {'price': 48, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'monroe': {'price': 48, 'sizes': ['s', 'l']},
    'maxi': {'price': 42, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'madison': {'price': 48, 'sizes': ['xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'kids_l/xl': {'price': 23},
    'lucy': {'price': 52, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl']},
    'lola': {'price': 48, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl']},
    'lindsay': {'price': 48, 'sizes': ['s', 'm', 'l']},
    'kids_azure': {'price': 25, 'sizes': [2, 4, 6, 8, 10, 12, 14]},
    'julia': {'price': 45, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'jordan': {'price': 65, 'sizes': ['xs', 's', 'm', 'l', 'xl', '2xl']},
    'jill': {'price': 55, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl']},
    'jade': {'price': 55, 'sizes': ['xs', 's', 'm', 'l', 'xl', '2xl']},
    'irma': {'price': 35, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'gracie': {'price': 28, 'sizes': [2, 4, 6, 8, 10, 12, 14]},
    'dotdotsmile': {'price': 36, 'sizes': [2, '3/4', '5/6', 7, '8/10', '12/14']},
    'classic_t': {'price': 35, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'cassie': {'price': 35, 'sizes': ['xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'azure': {'price': 35, 'sizes': ['xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'ana': {'price': 60, 'sizes': ['xs', 's', 'm', 'l', 'xl', '2xl', '3xl']},
    'amelia': {'price': 65, 'sizes': ['xxs', 'xs', 's', 'm', 'l', 'xl', '2xl']}
}

color = colors[random.randrange(0, len(colors) - 1)]
running_total = 0
folder = sys.argv[1] + '/'
logo = Image.open('logo.jpg')

def formatStyle(styleType):
    styleType = styleType.replace('_', ' ')
    return styleType.upper()

def centerText(dim):
    return 612 + (306 - dim[0]) / 2

def filePath(style, size, i):
    return style + "_" + size + "_" + str(i) + '.jpg'

def isLularizedName(fn, style, size):
    fileName = os.path.basename(fn)

    if len(fileName) < 1:
        return False
    if fileName.count('_') != 2:
        return False
    if fileName[:fileName.find('_')] == style:
        return True
    return False

def processImage(file, style, size, folder):
    photo_increment = 1

    if isLularizedName(file, style, size):
        return

    img = Image.open(file)

    img.thumbnail((612, 816))
    newImage = Image.new("RGBA", size=(918, 816), color=(255,255,255))
    newImage.paste(img, (0, 0, 612, 816))
    newImage.paste(logo, (624, 520, 909, 805))
    draw = ImageDraw.Draw(newImage)

    font = ImageFont.truetype("MavenProLight-300.otf", 42)
    draw.text((32, 760), "LuLaRoe Stacy Leasure-Broski", (0, 0, 0), font=font)
    draw.text((30, 758), "LuLaRoe Stacy Leasure-Broski", color, font=font)

    # Style
    draw.rectangle([(612, 0), (918, 130)], fill=color)
    msg = formatStyle(style)
    font = ImageFont.truetype("steelfish rg.ttf", 100)
    draw.text((centerText(draw.textsize(msg, font=font)), 2), msg, (255, 255, 255), font=font)

    # Size
    draw.text((centerText(draw.textsize(size.upper(), font=font)), 150), size.upper(), color, font=font)

    # Price
    font = ImageFont.truetype("steelfish rg.ttf", 100)
    msg = "$" + str(styleData[style]['price'])
    draw.text((centerText(draw.textsize(msg, font=font)), 275), msg, color, font=font)

    # Save image
    while os.path.exists(folder + filePath(style, size, photo_increment)):
        photo_increment += 1

    newImage.save(folder + filePath(style, size, photo_increment))
    os.remove(file)
    running_total += 1

def processFolder(folder, style, size):
    for fn in os.listdir(folder):
        if os.path.isfile(folder + fn) and os.path.splitext(fn)[1] == '.jpg':
            print('processing ' + folder)
            processImage(folder + fn, style, size, folder)
        elif os.path.isdir(folder + fn):
            if style == '':
                style = fn
            else:
                size = fn

            processFolder(folder + fn + '/', style, size)

if __name__ == "__main__":
    print('Lularizing folder: ' + folder)
    processFolder(folder, '', '')
    print('Lularized ' + str(running_total) + ' photos.')
