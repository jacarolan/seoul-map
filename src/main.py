from PIL import Image
import numpy as np


def main():

    baseMap = Image.open("data/SeoulTemplate.png")
    baseMap.convert("RGBA")

    baseMap = drawRegion(baseMap, 5, (0, 255, 0))

    baseMap.show()

def drawRegion(map, region, fill):
    
    data = np.array(map)
    r, g, b, a = data.T

    colorAreas = (r == 255) & (g == region) & (b == 255)
    data[..., :-1][colorAreas.T] = fill

    return Image.fromarray(data)


main()