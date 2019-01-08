# coding=utf-8

from PIL import Image
import numpy as np
import time
import cv2

graphVar = 2

minVal = 0.01
maxVal = 0.07

colLow = (255, 170, 130)
colHigh = (100, 40, 38)

prevData = [0] * 25


def main():

    dataFile = open("data/SeoulPollution.csv", 'r')

    baseMap = Image.open("data/SeoulTemplate.png")
    baseMap.convert("RGBA")

    #baseMap = drawRegion(baseMap, 5, (0, 255, 0))

    for i in range(169):

        baseMap = drawChunk(baseMap, dataFile)
        
        if graphVar == 2:
            baseMap.save("anim/no2/img"+str(i)+".png", "PNG")
        elif graphVar == 3:
            baseMap.save("anim/o3/img"+str(i)+".png", "PNG")
        elif graphVar == 4:
            baseMap.save("anim/co/img"+str(i)+".png", "PNG")
        elif graphVar == 5:
            baseMap.save("anim/so2/img"+str(i)+".png", "PNG")
        elif graphVar == 6:
            baseMap.save("anim/finedust/img"+str(i)+".png", "PNG")
        elif graphVar == 7:
            baseMap.save("anim/ultrafinedust/img"+str(i)+".png", "PNG")

def drawChunk(map, file):


    for i in range(25):

        line = file.readline().split(",")

        dataVal = 0

        try:
            dataVal = float(line[graphVar].replace("\"", ""))
            prevData[i] = dataVal
        except ValueError:
            dataVal = prevData[i]

        paraVal = (maxVal-dataVal)/(maxVal-minVal)

        col = (int(colLow[0]*paraVal + colHigh[0]*(1-paraVal)), \
            int(colLow[1]*paraVal + colHigh[1]*(1-paraVal)), \
            int(colLow[2]*paraVal + colHigh[2]*(1-paraVal)))

        map = drawRegion(map, korToId(line[1]), col)

    return map

def drawRegion(map, region, fill):
    
    data = np.array(map)
    r, g, b, a = data.T

    colorAreas = (r == 255) & (g == region) & (b == 255)
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
    "용산구": 25};

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