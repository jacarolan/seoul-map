# coding=utf-8

from PIL import Image
import numpy as np
import time
import cv2

graphVar = 5
startLine = 0

minVal = 0
maxVal = 100

colLow = (150, 150, 150)
colHigh = (0, 200, 255)

global prevData
prevData = [0] * 25

global prevLine
prevLine = []

def main():

    dataFile = open("data/SeoulClimate.csv", 'r')

    global prevLine
    prevLine = dataFile.readline().split(",")

    for i in range(startLine):
        dataFile.readline();

    baseMap = Image.open("data/SeoulTemplateClean.png")
    baseMap.convert("RGBA")

    #baseMap = drawRegion(baseMap, 5, (0, 255, 0))

    for i in range(365):

        dayMap = drawDay(baseMap, dataFile)
        #dayMap.show()
        print "Writing date", prevLine[0],"to file"
        
        if graphVar == 2:
            dayMap.save("anim/avgtemp/img"+str(i)+".png", "PNG")
        elif graphVar == 5:
            dayMap.save("anim/avghum/img"+str(i)+".png", "PNG")

def drawDay(map, file):

    day = prevLine[0][1:9]

    readingDay = True

    while readingDay:

        line = file.readline().split(",")

        if line[0][1:9] != day:
            global prevLine
            prevLine = line
            readingDay = False

        distId = 0

        try:
            distId = korToId(line[1])
        except KeyError:
            continue

        try:
            global prevData
            prevData[distId-1] = float(line[graphVar].replace("\"", ""))
        except ValueError:
            pass

    for distId in range(25):

        paraVal = (maxVal-prevData[distId])/(maxVal-minVal)


        red = int(colLow[0]*paraVal + colHigh[0]*(1-paraVal))
        blue = int(colLow[1]*paraVal + colHigh[1]*(1-paraVal))
        green = int(colLow[2]*paraVal + colHigh[2]*(1-paraVal))

        if red < 0:
            red = 0
        elif red > 255:
            red = 255

        if blue < 0:
            blue = 0
        elif blue > 255:
            blue = 255

        if green < 0:
            green = 0
        elif green > 255:
            green = 255

        col = (red, blue, green)

        map = drawRegion(map, distId+1, col)

    return map

def drawRegion(map, region, fill):
    
    data = np.array(map)
    r, g, b, a = data.T

    colorAreas = (r == 255) & (g == 127) & (b == region)
    data[..., :-1][colorAreas.T] = fill

    return Image.fromarray(data)

def engToId(district):

    engIdDict = {"Dobong": 1, \
    "Dongdaemun": 2, \
    "Dongjak": 3, \
    "Eunpyeong": 4, \
    "Gangbuk": 5, \
    "Gangdong": 6, \
    "Gangnam": 7, \
    "Gangseo": 8, \
    "Geumcheon": 9, \
    "Guro": 10, \
    "Gwanak": 11, \
    "Gwangjin": 12, \
    "Jongno": 13, \
    "Jung": 14, \
    "Jungnang": 15, \
    "Mapo": 16, \
    "Nowon": 17, \
    "Seocho": 18, \
    "Seodaemun": 19, \
    "Seongbuk": 20, \
    "Seongdeong": 21, \
    "Songpa": 22, \
    "Yangcheon": 23, \
    "Yeongdeungpo": 24, \
    "Yongsan": 25};

    return engIdDict[district];

def korToId(district):

    korIdDict = {"도봉구": 1, \
    "동대문구": 2, \
    "동작구": 3, \
    "은평구": 4, \
    "강북구": 5, \
    "강동구": 6, \
    "강남구": 7, \
    "강서구": 8, \
    "금천구": 9, \
    "구로구": 10, \
    "관악구": 11, \
    "광진구": 12, \
    "종로구": 13, \
    "중구": 14, \
    "중랑구": 15, \
    "마포구": 16, \
    "노원구": 17, \
    "서초구": 18, \
    "서대문구": 19, \
    "성북구": 20, \
    "성동구": 21, \
    "송파구": 22, \
    "양천구": 23, \
    "영등포구": 24, \
    "용산구": 25, \
    "도봉": 1, \
    "동대문": 2, \
    "동작": 3, \
    "은평": 4, \
    "강북": 5, \
    "강동": 6, \
    "강남": 7, \
    "강서": 8, \
    "금천": 9, \
    "구로": 10, \
    "관악": 11, \
    "광진": 12, \
    "종로": 13, \
    "중": 14, \
    "중랑": 15, \
    "마포": 16, \
    "노원": 17, \
    "서초": 18, \
    "서대문": 19, \
    "성북": 20, \
    "성동": 21, \
    "송파": 22, \
    "양천": 23, \
    "영등포": 24, \
    "용산": 25};

    return korIdDict[district.replace("\"", "")]

def toName(distId):

    districtDict = {1:"Dobong", \
    2: "Dongdaemun", \
    3: "Dongjak", \
    4: "Eunpyeong", \
    5: "Gangbuk", \
    6: "Gangdong", \
    7: "Gangnam", \
    8: "Gangseo", \
    9: "Geumcheon", \
    10: "Guro", \
    11: "Gwanak", \
    12: "Gwangjin", \
    13: "Jongno", \
    14: "Jung", \
    15: "Jungnang", \
    16: "Mapo", \
    17: "Nowon", \
    18: "Seocho", \
    19: "Seodaemun", \
    20: "Seongbuk", \
    21: "Seongdeong", \
    22: "Songpa", \
    23: "Yangcheon", \
    24: "Yeongdeungpo", \
    25: "Yongsan"};

    return districtDict[distId]


main()