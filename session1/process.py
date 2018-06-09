
import os
import os.path
import sys
from PIL import Image

directory = 'capture9'
processedDirectory = directory + "_processed"

if not os.path.exists(processedDirectory):
    os.mkdir(directory + "_processed")


files = os.listdir(directory)

storeMap = Image.open('storemap.png')

for file in files:
    if 'jpg' in file:
        fullInputPath = os.path.join(directory, file)
        fullOutputPath = os.path.join(processedDirectory, file)

        image = Image.open(fullInputPath)

        newImage = Image.new('RGB', (1280, 1491))

        newImage.paste((255,255,255), (0, 0, 1280, 1491))
        newImage.paste(image, (0, 0))
        newImage.paste(storeMap, (0, 480))

        newImage.save(fullOutputPath)

